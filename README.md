This app parses incoming emails, performs sentiment analysis, and offers possible responses.

To use:
Create a .env file in the root directory with this format:
```
GOOGLE_API_KEY=[your API key here]
MODEL=[Gemini model name here]
```

This app was built for the Postmark inbound email parsing, which returns a JSON of the following format. The code uses the To, From, Cc, Bcc, Subject, TextBody, HtmlBody, and Date fields, so format your input accordingly.
```
{
  "FromName": "",
  "MessageStream": "",
  "From": "",
  "FromFull": {
    "Email": "",
    "Name": "",
    "MailboxHash": ""
  },
  "To": "",
  "ToFull": [
    {
      "Email": "",
      "Name": "",
      "MailboxHash": ""
    }
  ],
  "Cc": "",
  "CcFull": [],
  "Bcc": "",
  "BccFull": [],
  "OriginalRecipient": "",
  "Subject": "",
  "MessageID": "",
  "ReplyTo": "",
  "MailboxHash": "",
  "Date": "Tue, 3 Jun 2025 01:48:37 -0400",
  "TextBody": "",
  "HtmlBody": "",
  "StrippedTextReply": "",
  "Tag": "",
  "Headers": [
    {
      "Name": "Return-Path",
      "Value": ""
    },
    {
      "Name": "Received",
      "Value": ""
    },
    {
      "Name": "X-Spam-Checker-Version",
      "Value": ""
    },
    {
      "Name": "X-Spam-Status",
      "Value": ""
    },
    {
      "Name": "X-Spam-Score",
      "Value": ""
    },
    {
      "Name": "X-Spam-Tests",
      "Value": ""
    },
    {
      "Name": "Received-SPF",
      "Value": ""
    },
    {
      "Name": "Received",
      "Value": ""
    },
    {
      "Name": "Received",
      "Value": ""
    },
    {
      "Name": "DKIM-Signature",
      "Value": ""
    },
    {
      "Name": "X-Google-DKIM-Signature",
      "Value": ""
    },
    {
      "Name": "X-Gm-Message-State",
      "Value": ""
    },
    {
      "Name": "X-Gm-Gg",
      "Value": ""
    },
    {
      "Name": "X-Google-Smtp-Source",
      "Value": ""
    },
    {
      "Name": "X-Received",
      "Value": ""
    },
    {
      "Name": "MIME-Version",
      "Value": ""
    },
    {
      "Name": "X-Gm-Features",
      "Value": ""
    },
    {
      "Name": "Message-ID",
      "Value": ""
    }
  ],
  "Attachments": []
}
```
