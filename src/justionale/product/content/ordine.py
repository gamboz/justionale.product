# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow

from justionale.product import _

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

clienti_factory = getUtility(
    IVocabularyFactory, 'justionale.product.Clienti')
ClientiVocabulary = clienti_factory(None)

prodotti_factory = getUtility(
    IVocabularyFactory, 'justionale.product.Prodotti')
ProdottiVocabulary = prodotti_factory(None)


class DGRow(model.Schema):
    "this zope.schema describes the columns of the data grid/table"

    prodotto = schema.Choice(
        title=_(u"Prodotto"),
        source="justionale.product.Prodotti",
    )
    qt = schema.Int(
        title=_(u"Quantità"),
        default=1,
    )
    note = schema.TextLine(
        title=_(u"Note?"),
        required=False,
    )


class IOrdine(model.Schema):
    """ Marker interface and Dexterity Python Schema for Ordine
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('ordine.xml')

    cliente = schema.Choice(
        title=_(u"Cliente"),
        source="justionale.product.Clienti",
    )

    directives.widget(table_rows=DataGridFieldFactory)
    table_rows = schema.List(
        title=_(u"Ordini"),  # this will be the title of the grid/table
        value_type=DictRow(
            title=u"One row",  # where is this used?
            schema=DGRow,),
    )

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IOrdine)
class Ordine(Item):
    """
    """
