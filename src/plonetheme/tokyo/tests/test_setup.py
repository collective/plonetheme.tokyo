# -*- coding: utf-8 -*-

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
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
        # self.assertTrue(self.installer.isProductInstalled('plonetheme.tokyo'))

    def test_browserlayer(self):
        """Test that IPlonethemeTokyoLayer is registered."""
        # from plonetheme.tokyo.interfaces import IPlonethemeTokyoLayer
        # from plone.browserlayer import utils
        # self.assertIn(IPlonethemeTokyoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_TOKYO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        # self.installer.uninstallProducts(['plonetheme.tokyo'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.tokyo is cleanly uninstalled."""
        # self.assertFalse(self.installer.isProductInstalled('plonetheme.tokyo'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeTokyoLayer is removed."""
        # from plonetheme.tokyo.interfaces import IPlonethemeTokyoLayer
        # from plone.browserlayer import utils
        # self.assertNotIn(IPlonethemeTokyoLayer, utils.registered_layers())
