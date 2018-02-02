# RUNME as 'python -m turl.tests.__main__'
import unittest
import turl.tests

def main():
  "Run all of the tests when run as a module with -m."
  suite = turl.tests.get_suite()
  runner = unittest.TextTestRunner()
  runner.run(suite)

if __name__ == '__main__':
  main()
