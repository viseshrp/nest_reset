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
@click.argument('temperature', type=int)
@click.option(
    '-i',
    '--client-id',
    prompt="Please enter the Client ID to continue",
    hide_input=True,
    required=True,
    type=str,
    envvar="NEST_CLIENT_ID",
    help="Your NEST client ID"
)
@click.option(
    '-s',
    '--client-secret',
    prompt="Please enter the Client secret to continue",
    hide_input=True,
    required=True,
    type=str,
    envvar="NEST_CLIENT_SECRET",
    help="Your NEST client secret"
)
def main(temperature, client_id, client_secret):
    """
    Simple CLI tool to listen for changes in NEST thermostat and reset the temperature back

    Example usages:

    nest-reset 74

    """
    try:
        run(temperature, client_id, client_secret)
    except Exception as e:
        # all other exceptions
        raise click.ClickException(e)


if __name__ == "__main__":
    main()  # pragma: no cover
