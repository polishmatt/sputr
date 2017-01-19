import unittest
import re
import click
import os

@click.command()
@click.argument('pattern', default='')
def cli(pattern):
    if pattern == '':
        suite = unittest.defaultTestLoader.discover(start_dir='.')
    elif os.sep in pattern:
        # run exact file or directory
        pass
    elif pattern[-3:] == '.py':
        suite = unittest.defaultTestLoader.discover(start_dir='.', pattern=pattern)
    else:
        suite = unittest.defaultTestLoader.discover(start_dir='.')
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

    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

