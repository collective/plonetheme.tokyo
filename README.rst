.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.com/collective/plonetheme.tokyo.svg?branch=master
    :target: https://travis-ci.com/collective/plonetheme.tokyo


========================================
Tokyo Theme for Plone (plonetheme.tokyo)
========================================

Tokyo Theme for Plone implements Bootstrap 4 into Plone, with an emphasis on keeping things as close to "default" as possible.


Frontpage
---------

.. image:: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/frontpage.png
    :target: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/frontpage.png


Sidebar
-------

.. image:: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/sidebar.png
    :target: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/sidebar.png


Mobile
------

.. image:: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/mobile.png
    :target: https://raw.githubusercontent.com/collective/plonetheme.tokyo/master/docs/mobile.png


Demo
----

- https://plonetheme.tokyo/


Features
--------

- Responsive mobile first theme for Plone
- No Dependencies to Barceloneta
- No Diazo Rules
- No Toolbar
- No Portlets
- Plone patterns still persistent
- Default Bootstrap 4 for form fields and views
- Bootstrap 4 components and JavaScript
- Bootstrap icons available 
- Uses https://github.com/collective/collective.sidebar


Documentation
-------------

Full documentation for end users can be found in the "docs" folder.


Credits
-------

This theme is developed and maintained by `operun Digital Solutions <https://www.operun.de>`_. Check out other `projects <https://www.operun.de/projekte>`_ we developed based on the `Enterprise Content Management System <https://www.operun.de/produkte/enterprise-content-management-system>`_ Plone.


Translations
------------

This product has been translated into:

- English (thanks, Netroxen)
- German (thanks, santonelli)


Known Issues
------------

- Some missing view overrides
- Some unstyled form widgets and fields

Some views implement custom forms that do not use `z3c.form`. In these cases it's possible the form fields may be styled incorrectly. We encourage users to report missing, broken or incomplete views (see below).


Installation
------------

Install plonetheme.tokyo by adding it to your buildout::

    [buildout]

    ...

    eggs =
        plonetheme.tokyo


and then running ``bin/buildout``...


Versions
--------

- Version 0.x and 1.x works with Plone 5.2
- Version 2.x works with Plone 6


Contribute
----------

- Issue Tracker: https://github.com/collective/plonetheme.tokyo/issues
- Source Code: https://github.com/collective/plonetheme.tokyo


Support
-------

If you are having issues, please let us know. We have a issue tracker located at: https://github.com/collective/plonetheme.tokyo/issues


License
-------

The project is licensed under the GPLv2.
