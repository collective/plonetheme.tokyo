TinyMCE templates
=================

To enable the TinyMCE templates feature you have to enable the plugin and
configure the templates within the TinyMCE controlpanel of your Plone site.

Activate TinyMCE Templates Plugin
---------------------------------

.. code-block::

    template|++plone++static/components/tinymce-builded/js/tinymce/plugins/template


Configure TinyMCE Templates
---------------------------

.. code-block:: json

    [
        {
          "title": "List",
          "url": "++theme++tokyo-theme/tinymce-templates/list.html"
        },
        {
          "title": "Card Group",
          "url": "++theme++tokyo-theme/tinymce-templates/card-group.html"
        },
    ]
