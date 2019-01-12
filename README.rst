==========
nest_reset
==========


Simple CLI tool to listen for changes in NEST thermostat and reset the temperature back
Works only if you have one thermostat

* GitHub: https://github.com/viseshrp/nest_reset
* Free software: MIT license


Installation
------------
.. code-block:: bash

    $ git clone <url>

    $ cd nest_reset

    $ pip install -e .


Requirements
------------

#. Python 2.7+


Features
--------

.. code-block:: bash

    $ nest_reset 74
    # starts monitoring your thermostat and resets the temp to 74F whenever it detects
    # someone changing it


Credits
-------

* Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template for getting me started.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

