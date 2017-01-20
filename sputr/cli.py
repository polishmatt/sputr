import click
import unittest
import sputr
import config
import sys
import os

@click.command()
@click.version_option(version=config.version)
@click.argument('pattern', default='')
def cli(pattern):
    if sys.path[0] != os.getcwd():
        sys.path.insert(0, os.getcwd())

    suite = sputr.discover(pattern=pattern)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

