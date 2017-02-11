from __future__ import absolute_import
import sys
import os
import json

import sputr

def cli():
    if len(sys.argv) >= 3 and sys.argv[1] == '--json':
        sputr.run(**json.loads(sys.argv[2][1:-1]))

    if 'SPUTR_OPTIONS' in os.environ:
        sys.argv += os.environ['SPUTR_OPTIONS'].split()
    
    try:
        from .click_cli import click_cli
    except (ValueError, SystemError):
        from click_cli import click_cli
    click_cli()


if __name__ == '__main__':
    cli()

