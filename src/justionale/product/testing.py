# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import justionale.product


class JustionaleProductLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=justionale.product)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'justionale.product:default')


JUSTIONALE_PRODUCT_FIXTURE = JustionaleProductLayer()


JUSTIONALE_PRODUCT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JUSTIONALE_PRODUCT_FIXTURE,),
    name='JustionaleProductLayer:IntegrationTesting',
)


JUSTIONALE_PRODUCT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JUSTIONALE_PRODUCT_FIXTURE,),
    name='JustionaleProductLayer:FunctionalTesting',
)


JUSTIONALE_PRODUCT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JUSTIONALE_PRODUCT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='JustionaleProductLayer:AcceptanceTesting',
)
