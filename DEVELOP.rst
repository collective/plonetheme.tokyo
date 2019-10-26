Development Buildout Usage
==========================


Create a virtualenv in the package::

    $ python3.7 -m venv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg
