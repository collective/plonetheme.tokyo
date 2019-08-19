==================
User Documentation
==================


The "fluid" Container
---------------------

In Plonetheme Tokyo, we've implemented an additional slot into the core template called "fluid". This allows users to insert content into a full-width container without being bound by the column system. This is incredibly useful for landing pages, login screens and error pages and negates the need to use negative margins.

To use the "fluid" container in your Page Template, do the following::

```xml
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      metal:use-macro="context/main_template/macros/master">

  <body>

    <metal:main fill-slot="fluid">

      <!-- Custom Content -->

    </metal:main>

  </body>

</html>
```
