from django.db import models

class Email(models.Model):
    recipient = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    cc = models.CharField(max_length=255)
    bcc = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    html_body = models.TextField()
    date = models.DateTimeField()

    positive = models.DecimalField(decimal_places=4, max_digits=5)
    neutral = models.DecimalField(decimal_places=4, max_digits=5)
    negative = models.DecimalField(decimal_places=4, max_digits=5)

    hash = models.CharField(max_length=64)

    def __str__(self):
        return self.body