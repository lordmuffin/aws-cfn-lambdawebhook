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

def handler(event, context):
    print "event.dump = " + json.dumps(event)
    url = event['webhookurl']
    payload = {json.dumps(event['payload'])}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
