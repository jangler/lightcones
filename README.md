lightcones
==========

Next version of the [jangler.lightcones.net](http://jangler.lightcones.net/)
website code, implemented in Python 3 and Flask.

Starting Server
---------------

    $ export FLASK_APP=lightcones.py
    $ flask run

or

    $ gunicorn lightcones:app
