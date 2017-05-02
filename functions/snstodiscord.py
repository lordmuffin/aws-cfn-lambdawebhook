#!/usr/bin/python
# Written by: Andrew Jackson
# This is used to pull repo from github and drop to S3
import json
import logging
import os
import time
import uuid
import boto3

def handler(event, context):
    print "event.dump = " + json.dumps(event)
    url = 'https://discordapp.com/api/webhooks/308790391031726082/zGRwUsO66V6UXl4Vb8eg8lDZ2pE7eljfPMQLVF9lSJlytAoYOCDSSsi8wUe9F1shC2IJ/github'
    payload = {json.dumps(event)}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
