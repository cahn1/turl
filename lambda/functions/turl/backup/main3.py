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
mydomain = 'rango-dev.intuit.com'

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
    print('Not a valid URL.')
    return False

# Retrieve short url based on the next sequence number
def get_short_url(t, q):
  try:
    response = t.get_item(
      Key = q
    )
    print('response: {}'.format(response))
    print('response[Item][short_url]: {}'.format(response['Item']['short_url']))
    return response['Item']['short_url']
  except KeyError:
    print('before update q: {}'.format(q))
    print('before update q type: {}'.format(type(q)))

    # s = next_short(t)
    merge = q.update({'short_url': next_short(t)})
    print('udpated q: {}'.format(q))
    print('udpated q type: {}'.format(type(q)))
    try:
      response = t.put_item(
        Item = q
      )
    except KeyError:
      print('Cannot find station_id')
      return None
  #try:
  #  response = t.scan(
  #    Select='COUNT'
  #  )
  #  count = response['Count']
  #  print('count: {}'.format(count))
  #  print(base62.encode(base_num+count))
  #  return base62.encode(base_num+count)
  #except Exception:
  #  print('Table scan failed.')
  #  return None
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

#def get_fqdn(url):
#  return urlparse(url).netloc.split(':')[0]

# Supports PutItem and GetItem on the dynamodb table
def handler(event, context):
  # set dynamodb table name
  table = ddb.Table('urls')
  print(event)

  print('event[httpMethod]: {}'.format(event['httpMethod']))
  #a_conv = ast.literal_eval(event['body']['url'])
  http_method = event['httpMethod']
  if http_method != 'GET' or http_method != 'POST'
    logger.info('Not implemented method.')
    return '451'

  if event['body'] != None: # This means it's POST
    b = event['body']
    logger.info(b)
    print('event[body]: {}'.format(b))
    print('type of event[body]: {}'.format(type(b)))
    b_conv = ast.literal_eval(b)
    print('b_conv: {}'.format(b_conv))
    print('type of b_conv: {}'.format(type(b_conv)))
    r = chk_valid_url(b_conv['url'])
    if r != False:
      print('valid url')
    else:
      print('Not a valid url')
  else:
    q = event['path']
    logger.info(q)
    print('event[path]: {}'.format(q))
    print('type of event[path]: {}'.format(type(q)))
    q_conv = ast.literal_eval(q)
    print('q_conv: {}'.format(q_conv))
    print('type of q_conv: {}'.format(type(q_conv)))
    r = chk_valid_url(q_conv['short_url'])
    if r != False:
      print('valid url')
    else:
      print('Not a valid url')


#  fqdn = get_fqdn(b_conv['url'])
#  print('b_conv[url]: {}'.format(type(b_conv['url'])))

  # switch to either GetItem or PutItem
  if mydomain not in b_conv['url']:
    print('url dont contains rango-dev.intuit.com')
    if http_method != 'POST':
      print('not valid request since its not POST')
    else:
      short_url = get_short_url(table, b_conv)
      print('returned short_url: {}'.format(short_url))
  else:
    print('url contains rango-dev.intuit.com')
    if event['httpMethod'] != 'GET':
      print('not valid request since its not GET')
    else:
      print('event: {}'.format(event))
      #resmeta = get_item(table, event['queryStringParameters'])
      #logger.info(resmeta)


  #e = base62.encode(30000000)
  #print(e) -> 21sMy

if __name__ == "__main__":
  handler(event, 'context')
