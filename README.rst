==========
nest_reset
==========


Simple CLI tool to listen for changes in NEST thermostat and reset the temperature back.

Works only for one thermostat.

* GitHub: https://github.com/viseshrp/nest_reset
* Free software: MIT license


Installation
------------
.. code-block:: bash

    $ pip install -U nest-reset


Requirements
------------

#. Python 2.7+
#. Nest client ID and secret. See here_ for instructions.


Features
--------

I found that the NEST thermostat can be super annoying and sets the temp automatically at times.
Sometimes its super cold outside, I set heating to 77-ish and then it just resets itself back to
70 and it gets really cold inside. I've tried changing multiple settings but it just sucks. And
thus, this tool was born. Also helpful if you've got annoying guests or kids changing the stat :)

All this does is use the NEST API, authenticates you with your ID and secret, pulls all your thermostat
info. **Note that I have only one thermostat registered so I have programmed this to work with only one/the first**
**thermostat associated with your account.**

All this really does is listen for temperature change events and if the temp is not what you need,
resets the thermostat to what you need.

.. code-block:: bash

    $ nest-reset 74
    # starts monitoring your thermostat and resets the temp to 74F whenever it detects
    # someone changing it

Client ID and secret can be set as env vars: ``NEST_CLIENT_ID`` and ``NEST_CLIENT_SECRET``.
They will be auto-read if present.
If they are not set, they will be prompted for. Its a one time prompt only.
Once you've been authenticated, an access token is obtained using the id and secret, and stored
at ``~/.nrtk``. Further runs will use this file, and if it does not exist or has expired, you'll
be prompted again.

Credits
-------

* Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template for getting me started.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _here: https://github.com/jkoelker/python-nest
