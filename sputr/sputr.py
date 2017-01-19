
import unittest
import re
import os
import importlib

def discover(start_dir='.', pattern=''):
    if pattern == '':
        suite = unittest.defaultTestLoader.discover(start_dir=start_dir)
    elif os.sep in pattern and pattern[-3:] == '.py':
        package = pattern[:-3].replace(os.path.sep, '.')
        module = importlib.import_module(package)
        suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    elif os.sep in pattern:
        suite = unittest.defaultTestLoader.discover(start_dir=pattern)
    elif pattern[-3:] == '.py':
        suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern=pattern)
    else:
        suite = unittest.defaultTestLoader.discover(start_dir=start_dir)
        items = [item for item in suite]
        suite = unittest.TestSuite()

        while len(items):
            nextItems = []
            for item in items:
                if hasattr(item, '__iter__'):
                    nextItems += [ nextItem for nextItem in item ]
                else:
                    if re.search(pattern, item.id()) is not None:
                        suite.addTest(item)
            items = nextItems

    return suite

