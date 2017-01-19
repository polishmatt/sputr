import click
import unittest
import os
import sputr

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as file:
    version = file.read().strip()

@click.command()
@click.version_option(version=version)
@click.argument('pattern', default='')
def cli(pattern):
    suite = sputr.discover(pattern=pattern)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

