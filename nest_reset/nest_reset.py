# -*- coding: utf-8 -*-

"""Module containing the core functionality."""

from __future__ import unicode_literals  # unicode support for py2

import click
import nest


def run(temp, client_id, client_secret):
    napi = nest.Nest(client_id=client_id, client_secret=client_secret)

    if napi.authorization_required:
        click.launch(napi.authorize_url)
        pin = click.prompt("Please enter your PIN to continue", hide_input=True, type=str)
        napi.request_token(pin=pin)

    thermostat = napi.structures[0].thermostats[0]

    if thermostat.is_locked:
        raise click.ClickException("Your thermostat is locked.")

    click.echo("Listening for changes in your NEST thermostat...")
    while napi.update_event.wait():
        napi.update_event.clear()
        thermostat.target = temp


