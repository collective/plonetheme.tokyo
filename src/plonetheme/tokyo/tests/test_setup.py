# -*- coding: utf-8 -*-

from plone import api
from plonetheme.tokyo.testing import PLONETHEME_TOKYO_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.tokyo is properly installed."""

    layer = PLONETHEME_TOKYO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.tokyo is installed."""
        self.assertTrue(self.installer.isProductInstalled('plonetheme.tokyo'))

    def test_browserlayer(self):
        """Test that IPlonethemeTokyoLayer is registered."""
        from plone.browserlayer import utils
        from plonetheme.tokyo.interfaces import IPlonethemeTokyoLayer
        self.assertIn(IPlonethemeTokyoLayer, utils.registered_layers())

    def testCurrentTheme(self):
        from plone.app.theming.interfaces import IThemeSettings
        self.assertEqual(
            api.portal.get_registry_record('currentTheme', IThemeSettings),
            'plonetheme.tokyo',
        )


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_TOKYO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        with api.env.adopt_roles(['Manager']):
            self.installer.uninstallProducts(['plonetheme.tokyo'])

    def test_product_uninstalled(self):
        """Test if plonetheme.tokyo is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plonetheme.tokyo'))

    def test_browserlayer_removed(self):
        """ Test that IPlonethemeTokyoLayer is removed."""
        from plone.browserlayer import utils
        from plonetheme.tokyo.interfaces import IPlonethemeTokyoLayer
        self.assertNotIn(IPlonethemeTokyoLayer, utils.registered_layers())

    def testCurrentTheme(self):
        from plone.app.theming.interfaces import IThemeSettings
        self.assertEqual(
            api.portal.get_registry_record('currentTheme', IThemeSettings),
            'barceloneta',
        )
