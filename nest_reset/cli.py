# -*- coding: utf-8 -*-

"""Console script for nest_reset."""
# enable absolute imports of this module for Python2.x
from __future__ import absolute_import
from __future__ import unicode_literals  # unicode support for py2

import click

from .nest_reset import run
from nest_reset import __version__


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-v', '--version')
@click.argument('temperature')
def main(temperature=None):
    """
    Simple CLI tool to listen for changes in NEST thermostat and reset the temperature back

    Example usages:

    nest_reset 74

    """
    try:
        click.echo("Listening for changes in your NEST thermostat...")
        run(temperature)
    except Exception as e:
        # all other exceptions
        raise click.ClickException(e)


if __name__ == "__main__":
    main()  # pragma: no cover
