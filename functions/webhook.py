#!/usr/bin/python
# Written by: Andrew Jackson
# This is used to send a JSON payload to a webhook.
import json
import logging
import os
import time
import uuid
import boto3
import requests
import decimal

#def default(obj):
#    if isinstance(obj, decimal.Decimal):
#        return int(obj)
#    return o.__dict__

def handler(event, context):
    print "event.dump = " + json.dumps(event)
    data = json.loads(event['body'])
    url = 'https://discordapp.com/api/webhooks/308790391031726082/zGRwUsO66V6UXl4Vb8eg8lDZ2pE7eljfPMQLVF9lSJlytAoYOCDSSsi8wUe9F1shC2IJ/github'
    #payload = {json.dumps(event)}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data['payload']))
    print(r.text)
