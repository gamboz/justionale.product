# -*- coding: utf-8 -*-
from justionale.product.content.riunione import IRiunione  # NOQA E501
from justionale.product.testing import JUSTIONALE_PRODUCT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class RiunioneIntegrationTest(unittest.TestCase):

    layer = JUSTIONALE_PRODUCT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_riunione_schema(self):
        fti = queryUtility(IDexterityFTI, name='Riunione')
        schema = fti.lookupSchema()
        self.assertEqual(IRiunione, schema)

    def test_ct_riunione_fti(self):
        fti = queryUtility(IDexterityFTI, name='Riunione')
        self.assertTrue(fti)

    def test_ct_riunione_factory(self):
        fti = queryUtility(IDexterityFTI, name='Riunione')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IRiunione.providedBy(obj),
            u'IRiunione not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_riunione_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Riunione',
            id='riunione',
        )

        self.assertTrue(
            IRiunione.providedBy(obj),
            u'IRiunione not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('riunione', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('riunione', parent.objectIds())

    def test_ct_riunione_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Riunione')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_riunione_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Riunione')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'riunione_id',
            title='Riunione container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
