from __future__ import print_function
from StringIO import StringIO
import boto3
import base64
import json
import logging
import time, datetime
import ast

"""
" Lambdb: ingestor
" query(curl) --> api gateway  --> Lambda#ingestor --> GET   --> dynamodb
"                                                  --> POST  --> dynamodb
"""

# set logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create resource for dynamodb
ddb = boto3.resource('dynamodb')
