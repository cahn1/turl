# Implement test_main turl.tests
import unittest
import pytest
import turl.main as m
import turl.lib.base62 as b62
import boto3
from boto3.dynamodb.conditions import Key, Attr

class TestMain(unittest.TestCase):
  def test_main_chk_valid_url_valid(self):
    self.assertNotEqual(m.chk_valid_url('https://www.google.com'), False)

  def test_main_chk_valid_url_invalid(self):
    self.assertEqual(m.chk_valid_url('https://www.google1.com'), False)

  def test_get_short_url_existing_url(self):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('urls')
    test_qstr = {'url':'https://shop.scholastic.com/parent-ecommerce/books/zac-and-the-dream-stealers-9780545401067.html'}
    test_response = m.get_short_url(table, test_qstr)['short_url']
    self.assertEqual(test_response, u'21sMz')

#  def test_get_short_url_new_url(self):
#    ddb = boto3.resource('dynamodb')
#    table = ddb.Table('urls')
#    qstr = {'url':'https://newurl'}
#    response = m.get_short_url(table, qstr)['short_url']
#    self.assertEqual(m.get_short_url('https://www.google.com'), False)

  def test_next_short(self):
    ddb = boto3.resource('dynamodb')
    base_num = 30000000
    table = ddb.Table('urls')
    test_response = table.scan(Select='COUNT')
    item_count = test_response['Count']
    self.assertEqual(m.next_short(table), b62.encode(base_num+item_count+1))

  def test_get_orig_url(self):
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('urls')
    test_response = table.query(IndexName='short_url-index',Select='ALL_PROJECTED_ATTRIBUTES',KeyConditionExpression=Key('short_url').eq(u'21sMz'))
    self.assertEqual(m.get_orig_url(table, {u'short_url': u'21sMz'}).get('url'), test_response['Items'][0].get('url'))

def get_suite():
  "Return a unittest.TestSuite."
  import turl.tests

  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(turl.tests)
  return suite
