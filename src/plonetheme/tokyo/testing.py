# -*- coding: utf-8 -*-
from Acquisition import aq_get
from plone import api
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.testing import z2
from plonetheme.tokyo.interfaces import IPlonethemeTokyoLayer
from zope.interface import alsoProvides

import collective.sidebar
import plonetheme.tokyo


def set_browserlayer(request):
    """
    Set the BrowserLayer for the request.
    We have to set the browserlayer manually, since importing the profile alone
    doesn't do it in tests.
    """
    alsoProvides(request, IPlonethemeTokyoLayer)


def setup_sdm(portal):
    """
    Setup session data manager.
    """
    tf_name = 'temp_folder'
    idmgr_name = 'browser_id_manager'
    toc_name = 'temp_transient_container'
    sdm_name = 'session_data_manager'

    from Products.Sessions.BrowserIdManager import BrowserIdManager
    from Products.Sessions.SessionDataManager import SessionDataManager
    from Products.TemporaryFolder.TemporaryFolder import MountedTemporaryFolder
    from Products.Transience.Transience import TransientObjectContainer

    import transaction

    bidmgr = BrowserIdManager(idmgr_name)
    tf = MountedTemporaryFolder(tf_name, title='Temporary Folder')
    toc = TransientObjectContainer(
        toc_name,
        title='Temporary Transient Object Container',
        timeout_mins=20,
    )
    session_data_manager = SessionDataManager(
        id=sdm_name,
        path=tf_name + '/' + toc_name,
        title='Session Data Manager',
        requestName='TESTOFSESSION',
    )
    portal._setObject(idmgr_name, bidmgr)
    portal._setObject(sdm_name, session_data_manager)
    portal._setObject(tf_name, tf)
    portal.temp_folder._setObject(toc_name, toc)
    transaction.commit()


class PlonethemeTokyoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        request = aq_get(app, 'REQUEST')
        request.environ['HTTP_ACCEPT_LANGUAGE'] = 'de'
        self.loadZCML(package=plonetheme.tokyo)
        self.loadZCML(package=collective.sidebar)

    def setUpPloneSite(self, portal):
        qi = api.portal.get_tool('portal_quickinstaller')
        qi.installProduct('plonetheme.tokyo')
        portal.acl_users.userFolderAddUser(
            SITE_OWNER_NAME,
            SITE_OWNER_PASSWORD,
            ['Manager'],
            [],
        )


class PlonethemeTokyoAcceptanceLayer(PlonethemeTokyoLayer):
    def setUpPloneSite(self, portal):
        super(PlonethemeTokyoAcceptanceLayer, self).setUpPloneSite(portal)
        setup_sdm(portal)


PLONETHEME_TOKYO_FIXTURE = PlonethemeTokyoLayer()
PLONETHEME_TOKYO_ACCEPTANCE_FIXTURE = PlonethemeTokyoAcceptanceLayer()


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
        PLONETHEME_TOKYO_ACCEPTANCE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PlonethemeTokyoLayer:AcceptanceTesting',
)
