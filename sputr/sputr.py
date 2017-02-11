import unittest
import re
import os
import importlib
import sys
import subprocess
import json

def discover(start_dir='.', pattern='', top_level_dir=None):

    if top_level_dir == None:
        top_level_dir = start_dir

    if os.sep in pattern and pattern[-3:] == '.py':
        # This approach was chosen over the more explicit use of paths with imp/importlib
        #   since they appear to be bugged and pick up parent modules with the same name as well.
        sys.path.insert(0, start_dir)
        name = pattern[:-3].replace(os.path.sep, '.')
        module = importlib.import_module(name)
        del sys.path[0]

        return unittest.defaultTestLoader.loadTestsFromModule(module)

    kwargs = {
        'start_dir': start_dir,
        'top_level_dir': top_level_dir,
    }
    search = False

    if os.sep in pattern:
        kwargs['start_dir'] += os.path.sep + pattern
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

def run(**kwargs):

    if kwargs.get('python', None) is not None:
        python = kwargs['python']
        del kwargs['python']
        child = subprocess.Popen([python, os.path.dirname(os.path.abspath(__file__)), '--json', '"' + json.dumps(kwargs) + '"'])
        data = child.communicate()
        sys.exit(child.returncode)

    if sys.path[0] != os.getcwd():
        sys.path.insert(0, os.getcwd())

    if kwargs['verbose']:
        verbosity = 2
    elif kwargs['quiet']:
        verbosity = 0
    else:
        verbosity = 1

    last = kwargs['runner'].rfind('.')
    package = kwargs['runner'][:last]
    runner = kwargs['runner'][last + 1:]
    try:
        module = importlib.import_module(package)
    except ImportError:
        if package[:6] == 'sputr.':
            package = package[6:]
            module = importlib.import_module(package)
    runner = getattr(module, runner)(
        verbosity=verbosity,
        failfast=kwargs['failfast'],
        buffer=kwargs['buffer']
    )
    runner.color = kwargs['color']

    suite = discover(
        start_dir=kwargs['start_dir'], 
        pattern=kwargs['pattern'], 
        top_level_dir=kwargs['top_level_dir']
    )

    if kwargs['catch']:
        unittest.installHandler()
    result = runner.run(suite)
    if kwargs['catch']:
        unittest.removeHandler()

    sys.exit(0 if result.wasSuccessful() else 1)

