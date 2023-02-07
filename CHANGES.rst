Changelog
=========


1.0.0 (2023-02-07)
------------------

Changed:

- Update buildout to Plone 5.2.11
  [santonelli]

- Drop jQuery dependency
  [santonelli]

- Update Bootstrap to 5.2.3
  [olda-a]

- Added Czech translation
  [olda-a]

Fixed:

- Fix postion of plone.header in @@manage-viewlets
  [santonelli]


0.7.0 (2021-05-06)
------------------

Changed:

- Added jQuery 3.5 required by Bootstrap
  [santonelli]

- Added scripts viewlet and moved Bootstrap JS to footer
  [santonelli]

Fixed:

- Removed non existent custom.css from theme manifest.
  [santonelli]

- Added missing map files.
  [santonelli]


0.6.0 (2021-04-15)
------------------

Added:

- Re-added version pins for development packages.
  [santonelli]

- Add required marker via CSS.
  [santonelli]

- Add translations to fix file upload translations.
  [santonelli]

Changed:

- Cleanup search result page.
  [santonelli]

- Move logo viewlet logic to viewlet code.
  [santonelli]

- Update buildout to Plone 5.2.4
  [santonelli]

Fixed:

- Update markup from p.a.z3cform. Fix checkbox/radio field widget.
  [santonelli]

- Fix navbar padding on mobile devices.
  [santonelli]

- Added styling fixes for folder_contents structure pattern.
  [santonelli]


0.5.0 (2020-10-06)
------------------

Added:

- Added Bootstrap icons and make them available via bi-icon classes.
  [santonelli]

- Added templates for Plone's default content types.
  [santonelli]

Changed:

- Changed container structure in main template.
  [santonelli]

- Changed pagination to use arrows instead of text.
  [santonelli]

- Update Bootstrap icons to 1.0.0.
  [santonelli]

- Bump version of collective.sidebar to 1.4.0.
  [santonelli]


0.4.0 (2020-04-20)
------------------

Added:

- Nothing added yet
  [santonelli]

Changed:

- Cleanup, remove paddings, add wrapper in main template
  [santonelli]

- Rename resources
  [santonelli]

- Removed CSS overrides for Bootstrap styling
  [santonelli]

- Update config for npm / yarn
  [santonelli]

- Convert Less to Sass
  [santonelli]

Fixed:

- Remove custom error message to fix redirection tool
  [santonelli]


0.3.0 (2019-12-06)
------------------

Added:

- Added Event View and Listing
  [santonelli]

Changed:

- Update package for Plone 5.2 and Python 3.7
  [ale-rt, santonelli]

Fixed:

- Restore barceloneta after the theme has been uninstalled (Refs. #32)
  [ale-rt]

- Improve reference widget styling
  [santonelli]


0.2.1 (2019-08-20)
------------------

Fixed:

- Fixed KeyError in @@prefs_install_products_form.
  [sarn0ld]


0.1.0 (2019-08-14)
------------------

Added:

- Add Event Listing and View. #19
  [santonelli]

- Updated password reset & recovery views with Bootstrap 4 markup.
  [Netroxen]

- Updated @@prefs_install_products_form view with Bootstrap 4 markup.
  [Netroxen]

- Updated @@edit view and form fields with Bootstrap 4 markup.
  [Netroxen]

- Update @@login views for Plone 5.1 and 5.2.
  [Netroxen]
