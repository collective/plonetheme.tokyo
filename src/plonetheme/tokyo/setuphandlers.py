# -*- coding: utf-8 -*-

from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        profiles = [
            'plonetheme.tokyo:uninstall',
            ]
        return profiles


def install(context):
    """
    Post install script:
    Do something at the end of the installation of this package.
    """
    _set_mark_special_links()


def uninstall(context):
    """
    Uninstall script:
    Do something at the end of the uninstallation of this package.
    """


def _set_mark_special_links():
    """Removes external link icon."""
    api.portal.set_registry_record('plone.mark_special_links', False)
