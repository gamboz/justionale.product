# -*- coding: utf-8 -*-

# from plone import api
from justionale.product import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class Prodotti(object):
    """
    """

    def __call__(self, context):

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # https://docs.plone.org/develop/plone/forms/vocabularies.html
        # Get site root
        root = context.portal_url.getPortalObject()

        # Acquire portal catalog
        portal_catalog = root.portal_catalog

        # Query all Prodotti
        brains = portal_catalog.searchResults(
            portal_type=["Prodotto", ])

        # create a list of SimpleTerm items:
        terms = []
        for brain in brains:
            terms.append(
                SimpleTerm(
                    value=brain["UID"],
                    token=str(brain["UID"]),
                    title=_(brain["Title"]),
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


ProdottiFactory = Prodotti()
