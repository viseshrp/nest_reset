# -*- coding: utf-8 -*-

"""Module containing the core functionality."""

from __future__ import unicode_literals  # unicode support for py2

import os
from time import sleep

import click
import nest

API_CALL_DELAY_SECONDS = 3
TOKEN_PATH = os.path.expanduser('~') + '/' + '.nrtk'


def write_access_token(token):
    # save to file
    with open(TOKEN_PATH, 'w') as file:
        file.write(token)


def read_access_token():
    # read access token if file is present
    token = ''
    if os.path.isfile(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as file:
            token = file.read()

    return token


def run(temp, client_id, client_secret):
    """
    Main runner function

    :param temp: user defined temp
    :param client_id: for nest auth
    :param client_secret: for nest auth
    :return: None
    """
    # init
    nest_data = nest.Nest(client_id=client_id, client_secret=client_secret,
                          access_token=read_access_token())

    # check auth
    if nest_data.authorization_required:
        # launch url in browser for auth
        click.launch(nest_data.authorize_url)
        # prompt and read pin
        pin = click.prompt("Please enter your PIN to continue", hide_input=True, type=str)
        nest_data.request_token(pin=pin)
        # save it to a file
        write_access_token(nest_data.access_token)

    thermostats = nest_data.structures.pop(0).thermostats

    if not thermostats:
        click.ClickException("No thermostat found in your account.")

    # get thermostat
    thermostat = thermostats.pop(0)

    if thermostat.is_locked:
        raise click.ClickException("Your thermostat is locked.")

    click.echo("Listening for changes in your NEST thermostat...")
    # wait for event
    while nest_data.update_event.wait():
        # clear event
        nest_data.update_event.clear()

        if thermostat.target != temp:  # only if changed temp != desired temp
            # do stuff
            click.echo("Someone tried to change the temperature to {}. Thermostat reset to {}".format(
                thermostat.target, temp))
            # reset the temp back
            thermostat.target = temp
            # delay to allow API to update
            sleep(API_CALL_DELAY_SECONDS)
