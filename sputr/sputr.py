
import unittest
import re
import os
import importlib

def discover(start_dir='.', pattern=''):
    if os.sep in pattern and pattern[-3:] == '.py':
        package = pattern[:-3].replace(os.path.sep, '.')
        module = importlib.import_module(package)
        return unittest.defaultTestLoader.loadTestsFromModule(module)

    kwargs = {
        'start_dir': start_dir,
    }
    search = False

    if os.sep in pattern:
        kwargs['start_dir'] = pattern
    elif pattern[-3:] == '.py':
        kwargs['pattern'] = pattern
    elif pattern != '':
        search = True

    suite = unittest.defaultTestLoader.discover(**kwargs)

    if search:
        tests = list_tests(suite)
        suite = unittest.TestSuite()

        for test in tests:
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

