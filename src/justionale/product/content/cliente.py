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


class ICliente(model.Schema):
    """ Marker interface and Dexterity Python Schema for Cliente
    """
    telefono = schema.TextLine(
        title=_(u"Telefono"),
        required=False,
    )
    indirizzo = schema.TextLine(
        title=_(u"Indirizzo"),
        required=False,
    )
    note = RichText(
        title=_(u'Note'),
        required=False
    )


@implementer(ICliente)
class Cliente(Item):
    """
    """
