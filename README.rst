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

    $ pip install nest-reset


Requirements
------------

#. Python 2.7+
#. Nest client ID and secret. See here_ for instructions.


Features
--------

.. code-block:: bash

    $ nest-reset 74
    # starts monitoring your thermostat and resets the temp to 74F whenever it detects
    # someone changing it


Credits
-------

* Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template for getting me started.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _here: https://github.com/jkoelker/python-nest
