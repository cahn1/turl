# URL shortener
from __future__ import print_function

__author__ = "Kay Ahn"
__license__ = "GPL"
__version__ = "0.5.0"
__maintainer__ = "chulho_ahn@intuit.com"
__email__ = "chulho_ahn@intuit.com"
__status__ = "dev"

import sys
sys.path.append('base62')
from StringIO import StringIO
import boto3
import base62
import json
import ast
import hashlib
import logging
import time, datetime

"""
" Lambdb: turl
" query(curl)  ---->   api gateway     ---->   Lambda#turl    --> GET   --> dynamodb   --> Lambda#turl     ----> dynamodb
"                     + IAM role               + IAM role                                                        + IAM role
"                     (lambda/cloudwatch)       (dynamodb/cloudwatch)                                           (dynamodb/cloudwatch)
"                                                             --> POST  --> dynamodb   --> Lambda#turl
"""

# set logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create resource for dynamodb
ddb = boto3.resource('dynamodb')

#url = 'https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html'
raw =  '{"body":{"url":"https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html"},"httpMethod":"POST","resource":"/api/q","queryStringParameters":null,"requestContext":{"httpMethod":"POST","requestId":"ace5627b-b775-11e7-a802-9f805fb72059","path":"/dev/api/q","resourceId":"62va99","apiId":"qqlfrb4ca6","stage":"dev","resourcePath":"/api/q","identity":{"apiKey":"","userArn":null,"user":null,"cognitoIdentityPoolId":null,"userAgent":"curl/7.54.0","accountId":null,"cognitoAuthenticationType":null,"accessKey":null,"caller":null,"cognitoIdentityId":null,"sourceIp":"66.74.181.240","cognitoAuthenticationProvider":null},"accountId":"413035961530"}}'
raw1 = '{"body":null,"httpMethod":"GET","resource":"/api/q","queryStringParameters":{"url":"https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html"}}'

event = json.loads(raw)
event1 = json.loads(raw1)

#print(event)
print('Loading function')

## call put_item to dynamodb table
def put_item(t, b):
  response = t.put_item(
    Item = b
  )
  return response

# call get_item from dynamodb table
def get_item(t, q):
  print(q)
  print(type(q))
  try:
	  response = t.get_item(
	    Key = {
        'url': '64ff6f9c0327ec9c59db5c31107ed507c36536c9',
        'id': '909090'
      }
	  )
	  item = response['Item']
	  return item
  except KeyError:
    print('Cannot find station_id')
    return None

def url_sha1(s):
  sha1o = hashlib.sha1()
  sha1o.update(s)
  return sha1o.hexdigest()

# Supports PutItem and GetItem on the dynamodb table
#def handler(event, context):
def main():
  # set dynamodb table name
  table = ddb.Table('urls')

  print(type(event['body']['url']))
  #a_conv = ast.literal_eval(event['body']['url'])

  hash_object = hashlib.sha1(b'https://www.worksheetworks.com/math/multi-digit-operations/division/two-with-three-digit-remainders.html')
  hex_dig = hash_object.hexdigest()
  print(hex_dig)

  sha_1 = hashlib.sha1()
  sha_1.update(event['body']['url'])
  print(sha_1.hexdigest())

  url_sha1_hex = url_sha1(event['body']['url'])
  print(url_sha1_hex)

  # switch to either GetItem or PutItem
  if event['httpMethod'] == 'POST':
    b = event['body']
    print(b)
    print(type(b))
    # convert unicoded dict to normal dict
    #b_conv = ast.literal_eval(b)
    b_conv = b
    id = {'id' : '19999'}
    short_url = {'short_url' : 'oPol'}
    merge = b_conv.update(id)
    merge = b_conv.update(short_url)
    print(b_conv)

    resmeta = put_item(table, b_conv)
    logger.info(resmeta)
    response = {'statusCode': resmeta['ResponseMetadata']['HTTPStatusCode'],
                'headers': {},
                'body': ''
    }
    return response
  elif event['httpMethod'] == 'GET':
    resmeta = get_item(table, event['queryStringParameters'])
    logger.info(resmeta)
    response = {'statusCode': 200,
                'headers': {},
                'body': json.dumps(resmeta)
    }
    return response
  else:
  	raise Exception('No supprted method.')

  e = base62.decode('2ck')
  print(e)

if __name__ == "__main__":
  main()
#  handler(event, 'context')
