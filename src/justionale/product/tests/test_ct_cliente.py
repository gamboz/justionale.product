# -*- coding: utf-8 -*-
from justionale.product.content.cliente import ICliente  # NOQA E501
from justionale.product.testing import JUSTIONALE_PRODUCT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ClienteIntegrationTest(unittest.TestCase):

    layer = JUSTIONALE_PRODUCT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_cliente_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cliente')
        schema = fti.lookupSchema()
        self.assertEqual(ICliente, schema)

    def test_ct_cliente_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cliente')
        self.assertTrue(fti)

    def test_ct_cliente_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cliente')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICliente.providedBy(obj),
            u'ICliente not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_cliente_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Cliente',
            id='cliente',
        )

        self.assertTrue(
            ICliente.providedBy(obj),
            u'ICliente not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('cliente', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cliente', parent.objectIds())

    def test_ct_cliente_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cliente')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
