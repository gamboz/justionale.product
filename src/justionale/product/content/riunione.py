# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory


from justionale.product import _


@provider(IContextAwareDefaultFactory)
def getTot(context):
    tot = 0.0
    for (dummy, ordine) in context.items():
        tot += ordine.tot
    return tot


class IRiunione(model.Schema):
    """ Marker interface and Dexterity Python Schema for Riunione
    """

    padrona = schema.Choice(
        title=_(u"Padrona di casa"),
        source="justionale.product.Clienti",
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


@implementer(IRiunione)
class Riunione(Container):
    """
    """
