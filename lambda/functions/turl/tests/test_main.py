# Implement test_main turl.tests
import unittest
import turl.main
import turl.lib.base62

class TestMain(unittest.TestCase):
  def test_main(self):
    self.assertEqual(True, False)

def get_suite():
  "Return a unittest.TestSuite."
  import turl.tests

  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(turl.tests)
  return suite
