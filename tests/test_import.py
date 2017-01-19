import unittest
import sputr
import os

class ImportTest(unittest.TestCase):
    def test_import(self):
        expected = os.path.join(os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')), 'sputr'), 'sputr.pyc')
        found = sputr.__file__
        self.assertEqual(found, expected, """
            Version of sputr imported is not the version we want to test
            Found: '%s'
            Expected: '%s'
        """ % (found, expected))

