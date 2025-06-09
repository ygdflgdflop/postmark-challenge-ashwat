from django.shortcuts import render
import json
import hashlib
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import asyncio
from .sentiment import *
from .models import Email

@csrf_exempt
def postmark_inbound_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            body = data.get('TextBody')

            text = asyncio.run(get_sentiment(body))
            vals = text.strip().split(',')
            for i in range(len(vals)):
                if(vals[i][0] == "["):
                    vals[i] = float(vals[i][1:])
                elif(vals[i][-1] == "]"):
                    vals[i] = float(vals[i][:-1])
                else:
                    vals[i] = float(vals[i])
            
            pos, neu, neg = vals
            print("pos:", pos)
            print("neu:", neu)
            print("neg:", neg)
            
            email = Email.objects.create(recipient = data.get('To'),
                                         sender = data.get('From'),
                                         cc = data.get('Cc'),
                                         bcc = data.get('Bcc'),
                                         subject = data.get('Subject'),
                                         body = body,
                                         html_body = data.get('HtmlBody'),
                                         date = datetime.strptime(data.get('Date'), "%a, %d %b %Y %H:%M:%S %z"),
                                         positive = pos,
                                         neutral = neu,
                                         negative = neg,
                                         hash = hashlib.sha256((data.get('From') + data.get('Date')).encode()).hexdigest())

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)

def list(request):
    emails = Paginator(Email.objects.all().order_by("-date"), 6)
    pg = request.GET.get("pg")
    page = emails.get_page(pg)
    return render(request, 'webhook/list.html', {'page': page})

def display(request, hash):
    email = Email.objects.filter(hash=hash)[0]
    argmax = lambda a: max(range(len(a)), key=lambda x: a[x])
    match argmax([email.neutral, email.positive, email.negative]):
        case 0:
            sentiment = "neutral"
        case 1:
            sentiment = "positive"
        case 2:
            sentiment = "negative"

    response = asyncio.run(get_response(email.body, sentiment))
    return render(request, 'webhook/display.html', {'email': email, 'sentiment': sentiment, 'response': response})