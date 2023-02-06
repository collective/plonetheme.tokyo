# -*- coding: utf-8 -*-

from plone.testing.z2 import Browser
from plonetheme.tokyo.browser.main_template import MainTemplate
from plonetheme.tokyo.testing import PLONETHEME_TOKYO_FUNCTIONAL_TESTING

import unittest


class TestListingsFunctional(unittest.TestCase):

    layer = PLONETHEME_TOKYO_FUNCTIONAL_TESTING

    def setUp(self):
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.browser = Browser(app)

    def test_main_template(self):
        self.main_template = MainTemplate(self.portal, self.request)
        template = self.main_template()
        self.assertTrue(template)

    def test_ajax_laod(self):
        self.browser.open(self.portal.absolute_url() + '?ajax_load=1')
        self.assertIn('ajax_load', self.browser.contents)
