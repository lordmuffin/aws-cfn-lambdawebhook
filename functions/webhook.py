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
    data = json.loads(event)
    url = data['webhookurl']
    payload = data['payload']
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload))
    print(r.text)
