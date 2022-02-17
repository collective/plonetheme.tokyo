# -*- coding: utf-8 -*-

from plone import api
from plonetheme.tokyo.testing import PLONETHEME_TOKYO_FUNCTIONAL_TESTING

import unittest


class TestListingsFunctional(unittest.TestCase):

    layer = PLONETHEME_TOKYO_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.view = api.content.get_view(
            name='listing_news',
            context=self.portal,
            request=self.request,
        )

    def test_listings(self):
        self.assertIn('template-listing_news', self.view(render=True))
