import unittest
import sputr
import os

class ImportTest(unittest.TestCase):
    def test_import(self):
        expected = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'sputr', 'sputr.py'))
        found = sputr.__file__
        if found not in [expected, expected + 'c']:
            self.fail("""
                Version of sputr imported is not the version we want to test
                Found: '%s'
                Expected: '%s'
            """ % (found, expected))

