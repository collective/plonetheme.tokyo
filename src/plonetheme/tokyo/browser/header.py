# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from Products.CMFPlone import utils
from Products.CMFPlone.interfaces import ISiteSchema
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility


class PortalHeader(ViewletBase):
    index = ViewPageTemplateFile('header.py')

    def update(self):
        super(PortalHeader, self).update()
        registry = getUtility(IRegistry)
        settings = registry.forInterface(
            ISiteSchema, prefix='plone', check=False)
        self.logo = None
        if getattr(settings, 'site_logo', False):
            self.logo = utils.getSiteLogo()
        self.logo_title = settings.site_title
