from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

# implement a basic test under turl.tests
import unittest

#class TestSomething(unittest.TestCase):
#  def test_something_else(self):
#    self.assertEqual(True, True)
#
#class TestMain(unittest.TestCase):
#  def test_main(self):
#    self.assertEqual(True, True)

def get_suite():
  "Return a unittest.TestSuite."
  import turl.tests

  loader = unittest.TestLoader()
  #suite = loader.loadTestsFromModule(turl.tests)
  suite = loader.discover('turl.tests', pattern='test_*.py')
  return suite
