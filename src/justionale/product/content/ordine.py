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

from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory

from plone import api


clienti_factory = getUtility(
    IVocabularyFactory, 'justionale.product.Clienti')
ClientiVocabulary = clienti_factory(None)

prodotti_factory = getUtility(
    IVocabularyFactory, 'justionale.product.Prodotti')
ProdottiVocabulary = prodotti_factory(None)


# https://docs.plone.org/external/plone.app.dexterity/docs/advanced/defaults.html
# https://training.plone.org/5/mastering-plone/dexterity_reference.html
@provider(IContextAwareDefaultFactory)
def getTot(context):
    tot = 0.0
    for row in context.table_rows:
        prodotto_UID = row['prodotto']
        # https://training.plone.org/5/mastering-plone/views_3.html
        brains = api.content.find(UID=prodotto_UID)
        brain = brains[0]
        prodotto = brain.getObject()
        qt = row['qt']
        tot += qt * prodotto.costo
    return tot


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
    # partial = schema.TextLine(
    #     title=_(u"Totale parziale"),
    #     readonly=True,
    # )


class IOrdine(model.Schema):
    """ Marker interface and Dexterity Python Schema for Ordine
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('ordine.xml')

    # TODO: switch to "reference"
    # https://docs.plone.org/external/plone.app.dexterity/docs/advanced/references.html
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

    tot = schema.Float(
        title='Totale',
        readonly=True,
        defaultFactory=getTot,
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

    # # Override title
    # # https://stackoverflow.com/a/33196501/1581629
    # # TODO: turn into una-tantum at __init__
    # def makeTitle(self):
    #     brains = api.content.find(UID=self.cliente)
    #     brain = brains[0]
    #     cliente = brain.Title
    #     title = f"{cliente}"
    #     return title

    # def Title(self):
    #     return self.makeTitle()

    # @property
    # def title(self):
    #     return self.makeTitle()
