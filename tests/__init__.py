import unittest
import imp

class SputrTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(SputrTest, self).__init__(*args, **kwargs)
        module = imp.find_module('sputr')
        self.sputr = imp.load_module(*('sputr',) + module)

