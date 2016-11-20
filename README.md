lightcones
==========

Next version of the [jangler.lightcones.net](http://jangler.lightcones.net/)
website code, implemented in Python 3 and Flask.

Dependencies
------------

- python3
    - flask
    - pyyaml
    - markdown

Starting Server
---------------

    $ export FLASK_APP=lightcones.py
    $ flask run

or

    $ gunicorn lightcones:app
