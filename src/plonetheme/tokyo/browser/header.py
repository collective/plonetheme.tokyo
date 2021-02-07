# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase
from Products.CMFPlone import utils


class PortalHeader(ViewletBase):
    def update(self):
        super(PortalHeader, self).update()
        if api.portal.get_registry_record('plone.site_logo'):
            self.logo_url = utils.getSiteLogo()
        else:
            self.logo_url = '{0}/++plone++plonetheme.tokyo/{1}'.format(
                api.portal.get().absolute_url(),
                'plone_logow.svg')
        self.logo_title = api.portal.get_registry_record('plone.site_title')
