# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.tokyo


class PlonethemeTokyoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.tokyo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.tokyo:default')


PLONETHEME_TOKYO_FIXTURE = PlonethemeTokyoLayer()


PLONETHEME_TOKYO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_TOKYO_FIXTURE,),
    name='PlonethemeTokyoLayer:IntegrationTesting',
)


PLONETHEME_TOKYO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_TOKYO_FIXTURE,),
    name='PlonethemeTokyoLayer:FunctionalTesting',
)


PLONETHEME_TOKYO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_TOKYO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeTokyoLayer:AcceptanceTesting',
)
