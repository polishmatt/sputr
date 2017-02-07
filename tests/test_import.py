import os
from tests import SputrTest

class ImportTest(SputrTest):
    def test_import(self):
        expected = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'sputr'))
        expected = [
            os.path.join(expected, 'sputr.py'),
            os.path.join(expected, 'sputr.pyc'),
            os.path.join(expected, '__init__.py'),
            os.path.join(expected, '__init__.pyc')
        ]
        found = self.sputr.__file__
        if found not in expected:
            self.fail("""
                Version of sputr imported is not the version we want to test
                Found: '%s'
                Expected: '%s'
            """ % (found, expected))

