try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='turl',
    version='0.1.0',
    packages=['turl', 'turl.tests'],
    description='Tiny url test_suite',
    test_suite='turl.tests.get_suite'
)
