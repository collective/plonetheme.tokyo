Theme Development
=================

Install dependencies
--------------------

Run `npm install` to add dependencies from package.json::

.. code-block:: shell

    $ cd ./src/plonetheme/tokyo/theme
    $ npm install

Compile resources
-----------------

Run `npm build` to add dependencies from package.json::

.. code-block:: shell

    $ npm build

This will compile your `scss/theme.scss` into `css/theme.css`. A minified
version will be created as well. Check out the scripts section from
`package.json` so see what happens exactly.

Watch for changes
-----------------

Run `npm watch` to automatically compile when a file has been changed::

.. code-block:: shell

    $ npm watch

With `npm watch` you start the build process automatically when you save a file.
