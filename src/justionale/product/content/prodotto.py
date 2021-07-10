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
from Products.Five import BrowserView
# from Acquisition import aq_inner
from plone import api


from justionale.product import _
# import pdb; pdb.set_trace()
# from justionale.product import IOrdine


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


class ProdottoView(BrowserView):

    def ordini(self):
        """Return a catalog search result of sessions to show."""

        # context = aq_inner(self.context)
        catalog = api.portal.get_tool(name='portal_catalog')

        # this returns a catalog search (or a list of brains?)
        return catalog(
            # object_provides=IOrdine.__identifier__,
            # path='/'.join(context.getPhysicalPath()),
            sort_on='sortable_title')
