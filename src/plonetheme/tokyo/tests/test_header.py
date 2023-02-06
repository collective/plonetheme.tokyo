# -*- coding: utf-8 -*-

from plone import api
from plonetheme.tokyo.browser.header import PortalHeader
from plonetheme.tokyo.testing import PLONETHEME_TOKYO_FUNCTIONAL_TESTING

import unittest


SITE_LOGO_BASE64 = (
    b'filenameb64:cGl4ZWwucG5n;datab64:iVBORw0KGgoAAAANSUhEUgA'
    b'AAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4z8AAAAMBAQAY3Y2wAAA'
    b'AAElFTkSuQmCC'
)


class TestHeaderFunctional(unittest.TestCase):

    layer = PLONETHEME_TOKYO_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.viewlet = PortalHeader(self.portal, self.request, None)

    def test_site_title(self):

        # default plne site title
        self.viewlet.update()
        self.assertEqual(self.viewlet.logo_title, 'Plone site')

        # custom plone site title
        api.portal.set_registry_record(
            name='plone.site_title',
            value='Foobar',
        )
        self.viewlet.update()
        self.assertEqual(
            self.viewlet.logo_title,
            u'Foobar',
        )

    def test_logo_url(self):

        # default logo
        logo_url = '{0}/++plone++plonetheme.tokyo/{1}'.format(
            self.portal.absolute_url(),
            'plone_logow.svg',
        )
        self.viewlet.update()
        self.assertEqual(self.viewlet.logo_url, logo_url)

        # custom logo
        api.portal.set_registry_record(
            name='plone.site_logo',
            value=SITE_LOGO_BASE64,
        )
        self.viewlet.update()
        logo_url = '{0}/@@site-logo/pixel.png'.format(
            self.portal.absolute_url(),
        )
        self.assertEqual(self.viewlet.logo_url, logo_url)
