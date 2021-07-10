# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow
from plone import api


from justionale.product import _


@provider(IContextAwareDefaultFactory)
def getTot(context):
    tot = 0.0
    for (dummy, ordine) in context.items():
        tot += ordine.tot
    return tot


class DGRow(model.Schema):
    "this zope.schema describes the columns of the data grid/table"

    prodotto = schema.Choice(
        title=_(u"Prodotto"),
        source="justionale.product.Prodotti",
    )


class IRiunione(model.Schema):
    """ Marker interface and Dexterity Python Schema for Riunione
    """

    padrona = schema.Choice(
        title=_(u"Padrona di casa"),
        source="justionale.product.Clienti",
    )

    data = schema.Datetime(
        title=_(u'Data'),
        required=True,
    )

    note = RichText(
        title=_(u'Note'),
        required=False
    )

    tot = schema.Float(
        title=_(u'Totale'),
        readonly=True,
        defaultFactory=getTot,
    )

    directives.widget(regalo=DataGridFieldFactory)
    regalo = schema.List(
        title=_(u"Regalo padrona di casa"),
        value_type=DictRow(
            title=u"One row",  # where is this used?
            schema=DGRow,),
    )


@implementer(IRiunione)
class Riunione(Container):
    """
    """

    # # Override title
    # # https://stackoverflow.com/a/33196501/1581629
    # # TODO: turn into una-tantum at __init__
    # def makeTitle(self):
    #     brains = api.content.find(UID=self.padrona)
    #     brain = brains[0]
    #     padrona = brain.Title
    #     title = f"{padrona} - {self.data.strftime('%B %Y')}"
    #     return title

    # def Title(self):
    #     return self.makeTitle()

    # @property
    # def title(self):
    #     return self.makeTitle()
