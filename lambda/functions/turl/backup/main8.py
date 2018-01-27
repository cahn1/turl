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
from boto3.dynamodb.conditions import Key, Attr
import base62
import json
import ast
import hashlib
import urllib
from urlparse import urlparse
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
base_num = 30000000
#mydomain = 'rango-dev.intuit.com'
mydomain = 'qpgds5ptla.execute-api.us-west-2.amazonaws.com'

#print(event)
print('Loading function')

# Check if the requested is valid url or not
def chk_valid_url(url):
  try:
    if url in mydomain:
      return True
    else:
      return urllib.urlopen(url)
  except IOError:
    log.error('Not a valid URL.')
    return False

# Retrieve short url based on the next sequence number
def get_short_url(t, q):
  print('qqq: {}'.format(q))

  try:
    response = t.get_item(
      Key = q
    )
    print('response: {}'.format(response))
    print('response[Item]: {}'.format(response[Item]))
    print('response[Item][short_url]: {}'.format(response['Item']['short_url']))
    print('response[ResponseMetadata][HTTPStatusCode]: {}'.format(response['ResponseMetadata']['HTTPStatusCode']))
    merge = { u'HTTPStatusCode': response['ResponseMetadata']['HTTPStatusCode'], u'short_url': response['Item']['short_url'] }
    #return response['Item']['short_url']
    return merge
  except NameError:
    print('before update q: {}'.format(q))
    print('before update q type: {}'.format(type(q)))
    seq = next_short(t)
    query = q.update({'short_url': seq})
    print('udpated q: {}'.format(q))
    print('udpated q type: {}'.format(type(q)))
    # Insert a new url w/ generated short_url into dynamodb table
    try:
      response = t.put_item(
        Item = q
      )
      print('2response: {}'.format(response))
      merge = { u'HTTPStatusCode': response['ResponseMetadata']['HTTPStatusCode'], u'short_url': seq }
      return merge
    except Exception:
      logger.info('Failed to insert a new item to the table.')
      return None

def next_short(t):
  try:
    response = t.scan(
      Select='COUNT'
    )
    count = response['Count']
    print('count: {}'.format(count))
    print(base62.encode(base_num+count+1))
    return base62.encode(base_num+count+1)
  except Exception:
    print('Table scan failed.')
    return None

# call get_orig_url from dynamodb table
def get_orig_url(t, q):
  try:
    response = t.query(
      IndexName='short_url-index',
      Select='ALL_PROJECTED_ATTRIBUTES',
      KeyConditionExpression=Key('short_url').eq(q['short_url'])
    )
    logger.info('response: {}'.format(response))
    item = response['Items']
    if len(item) != 0:
      orig_url = response['Items'][0].get('url')
    else:
      orig_url = u'Could not find the link..'
    jurl = { u'url': orig_url }
    return jurl
  except Exception:
    print('Couldn\'t run the query..')
    return None

# Generate HTTP Method Response
def gen_response(r):
  response = {
    'statusCode': r['HTTPStatusCode'],
    'headers': {},
    'body': json.dumps({ u'short_url': r['short_url'] })
  }
  print('1response: {}'.format(response))
  print('1response type: {}'.format(type(response)))
  return response

# Supports PutItem and GetItem on the dynamodb table
def handler(event, context):
  # set dynamodb table name
  table = ddb.Table('urls')

  # switch to either GetItem or PutItem
  if event['httpMethod'] == 'POST':
    b = event['body']
    logger.info(b)
    b_dict = ast.literal_eval(b)

    # check if the requested url is vaild
    response = chk_valid_url(b_dict['url'])
    if response != False:
      logger.info('Valid url.')
    else:
      logger.error('Not a valid url.')
      sys.exit(1)
    short_url = get_short_url(table, b_dict)
    print('returned short_url: {}'.format(short_url))
    return gen_response(short_url)
#    response = {
#      'statusCode': 200,
#      'headers': {},
#      'body': json.dumps({ u'url': orig_url })
#    }
    #print('response: {}'.format(response))
    #return response

  elif event['httpMethod'] == 'GET':
    q = event['queryStringParameters']
    logger.info(q)
    orig_url = get_orig_url(table, q)
    response = {
      'statusCode': 200,
      'headers': {},
      'body': json.dumps(orig_url)
    }
    print('response: {}'.format(response))
    return response
  else:
    raise Exception('No supprted method.')
    return '461'

if __name__ == "__main__":
  handler(event, 'context')
