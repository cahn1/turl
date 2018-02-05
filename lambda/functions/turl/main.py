# URL shortener
from __future__ import print_function

__author__ = "Kay Ahn"
__license__ = "GPL"
__version__ = "0.5.0"
__maintainer__ = "chulho_ahn@intuit.com"
__email__ = "chulho_ahn@intuit.com"
__status__ = "dev"

import sys
sys.path.append('turl/lib')
sys.path.append('lib')
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
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create resource for dynamodb
ddb = boto3.resource('dynamodb')
base_num = 30000000
#mydomain = 'rango-dev.intuit.com'
# API Gateway url. This can be shorted.
mydomain = 'qpgds5ptla.execute-api.us-west-2.amazonaws.com'

print('Loading function')

# Check if the requested is valid url or not
def chk_valid_url(url):
  try:
    if url in mydomain:
      return True
    else:
      return urllib.urlopen(url)
  except IOError:
    logger.error('Not a valid URL.')
    return False

# Retrieve short url based on the next sequence number
def get_short_url(t, q):
  print('q: {}'.format(q))
  try:
    response = t.get_item(
      Key = q
    )
    print('response[Item]: {}'.format(response['Item']))
    merge = { u'HTTPStatusCode': response['ResponseMetadata']['HTTPStatusCode'], u'short_url': response['Item']['short_url'] }
    return merge
  # if the requested url doesn't exist in the table then geenerate new short_url
  except Exception as e:
    print('URL is not in the table. {}'.format(e))
    seq = next_short(t)
    query = q.update({'short_url': seq})
    # Insert a new url w/ generated short_url into dynamodb table
    try:
      response = t.put_item(
        Item = q
      )
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
    # Current total number of items
    count = response['Count']
    print('count: {}'.format(count))
    logger.info('Total Item Count: {}'.format(count))
    # return next number encoded by base62. This will be the next short_url
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
    merge = { u'HTTPStatusCode': response['ResponseMetadata']['HTTPStatusCode'], u'url': orig_url }
    return merge
  except Exception:
    print('Couldn\'t run the query..')
    return None

# Generate HTTP Method Response
def gen_response(r, t):
  # Generate separate response depdending on the request type
  if t == 'POST':
    body = json.dumps({u'short_url': r['short_url']})
  else:
    body = json.dumps({u'url': r['url']})

  response = {
    'statusCode': r['HTTPStatusCode'],
    'headers': {},
    'body': body
  }
  return response

# Supports PutItem and GetItem to the dynamodb table
def handler(event, context):
  # set dynamodb table name
  table = ddb.Table('urls')

  # switch to either GetItem or PutItem
  # when the reuqest is POST
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

    # Call get_short_url either for new one or existing one
    short_url = get_short_url(table, b_dict)
    print('Returned short_url: {}'.format(short_url))
    return gen_response(short_url, 'POST')
  # when the reuqest is GET
  elif event['httpMethod'] == 'GET':
    q = event['queryStringParameters']
    logger.info(q)
    # Call get_orig_url to get original long url.
    orig_url = get_orig_url(table, q)
    return gen_response(orig_url, 'GET')
  else:
    raise Exception('No supprted method.')
    return '460'

if __name__ == "__main__":
  handler(event, 'context')
