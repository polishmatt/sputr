import click
import unittest
import sputr
import config

@click.command()
@click.version_option(version=config.version)
@click.argument('pattern', default='')
def cli(pattern):
    suite = sputr.discover(pattern=pattern)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

