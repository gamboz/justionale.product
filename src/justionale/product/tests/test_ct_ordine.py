# -*- coding: utf-8 -*-
from justionale.product.content.ordine import IOrdine  # NOQA E501
from justionale.product.testing import JUSTIONALE_PRODUCT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class OrdineIntegrationTest(unittest.TestCase):

    layer = JUSTIONALE_PRODUCT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Riunione',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_ordine_schema(self):
        fti = queryUtility(IDexterityFTI, name='Ordine')
        schema = fti.lookupSchema()
        self.assertEqual(IOrdine, schema)

    def test_ct_ordine_fti(self):
        fti = queryUtility(IDexterityFTI, name='Ordine')
        self.assertTrue(fti)

    def test_ct_ordine_factory(self):
        fti = queryUtility(IDexterityFTI, name='Ordine')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOrdine.providedBy(obj),
            u'IOrdine not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_ordine_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Ordine',
            id='ordine',
        )

        self.assertTrue(
            IOrdine.providedBy(obj),
            u'IOrdine not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('ordine', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('ordine', parent.objectIds())

    def test_ct_ordine_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Ordine')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
