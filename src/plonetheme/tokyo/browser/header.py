# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.CMFPlone import utils


class PortalHeader(ViewletBase):
    def update(self):
        super(PortalHeader, self).update()
        self.logo = None
        if api.portal.get_registry_record('plone.site_logo'):
            self.logo = utils.getSiteLogo()
        self.logo_title = api.portal.get_registry_record('plone.site_title')
