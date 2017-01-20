import click
import unittest
import sputr
import config
import sys
import os

@click.command()
@click.version_option(version=config.version)
@click.argument('pattern', default='')
@click.option('--start_dir', default='.', show_default=True)
def cli(pattern, start_dir):
    if sys.path[0] != os.getcwd():
        sys.path.insert(0, os.getcwd())

    suite = sputr.discover(pattern=pattern, start_dir=start_dir)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

