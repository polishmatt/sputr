
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
        discover_suite = unittest.defaultTestLoader.discover(start_dir=start_dir)
        suite = unittest.TestSuite()

        for test in list_tests(discover_suite):
            if re.search(pattern, test.id()) is not None:
                suite.addTest(test)

    return suite

def list_tests(suite):
    tests = []
    items = [item for item in suite]

    while len(items):
        next_items = []
        for item in items:
            if hasattr(item, '__iter__'):
                next_items += [ next_item for next_item in item ]
            else:
                tests.append(item)
        items = next_items

    return tests

