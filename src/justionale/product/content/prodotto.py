# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from justionale.product import _


class IProdotto(model.Schema):
    """ Marker interface and Dexterity Python Schema for Prodotto
    """
    costo = schema.Float(
        title=_(u"Costo"),
        required=True,
        min=0.0,
        max=100.0,
    )
    note = RichText(
        title=_(u'Note'),
        required=False
    )


@implementer(IProdotto)
class Prodotto(Item):
    """
    """
