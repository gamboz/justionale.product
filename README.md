# justionale.product

Gestionale di ordini Just per Anna

## Development

### New add-on

Install Plone 5.2 with python 3.7 and work from `zinstance` dir.

I need a Plone add-on. So I need `mr.bob` and `bobtemplates.plone`.
I install them with buildout. In `buildout.cfg` add:
```
parts =
    ...
    mrbob

[mrbob]
recipe = zc.recipe.egg
eggs =
    mr.bob
    bobtemplates.plone
```
then run `./bin/buidout`.\
Now you should have the runnable script `./bin/mrbob` and a folder like\
`../buildout-cache/eggs/bobtemplates.plone-XXX.egg/bobtemplates/plone/addon`\
(that's where the template is).

Now prepare a Plone add-on using a template:\
`./bin/mrbob -O src/a.b bobtemplates:plone/addon`\
where `a.b` is any name (not sure if it _must_ have the ".", but it
usually have at least one ".")

If all goes well you have a folder `src/a.b` (with a git repo inside).
You can already use it in Plone:
```
[buildout]
...
eggs =
    Plone
    ...
    a.b

develop =
    src/a.b

```
Do not forget the `develop` part.
Then `./bin/buildout && ./bin/plonectl fg` as usual.
You should see your addon in
http://localhost:8080/Justionale/prefs_install_products_form

This addon does nothing. If you want to develop a content type, run:\
`./bin/mrbob -O src/a.b/ bobtemplates:plone/content_type`\
follow the instructions (say 'n' to the 'XML Model') and create a content type called "vaso".

Now restart your Plone instance, go to the
 (addon page)[http://localhost:8080/Justionale/prefs_install_products_form]
 and click "install" for your addon.

Some reference:
* https://training.plone.org/5/mastering-plone/dexterity.html
* https://docs.plone.org/external/plone.app.dexterity/docs/index.html

### Interesting stuff

You can configure your content type in three ways. I will look at the
python schema only (i.e. define the fields & co. using python only, no
XML models).

You should have a folder such as: `src/a.b/src/a/b/content/` and there
the python file for the content type: `vaso.py`.

There uncomment the stuff related to the filed `level`.
Now you have a broken toy, because `LevelVocabulary` is not defined anywhere...

So commit all your changes (git) and create one vocabulary with\
`./bin/mrbob -O src/a.b/ bobtemplates:plone/vocabulary`

You have now registered your vocabulary (`a.b.LevelVocabulary`) as a reusable component.\
See https://docs.plone.org/develop/plone/forms/vocabularies.html \
To access it add the following to `vaso.py`:
```python
...
from a.b import _

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


factory = getUtility(IVocabularyFactory, 'a.b.LevelVocabulary')
LevelVocabulary = factory(None)


class IVaso(model.Schema):
    ...

    directives.widget(level=RadioFieldWidget)
    level = schema.Choice(
        title=_(u'Sponsoring Level'),
        vocabulary=LevelVocabulary,
        required=True
    )

    ...
```

Apparently the factory function-object wants a "context" on which to
operate (see `def __call__(self, context)` in `level_vocabulary.py` at
l.24), but I do not know how to provide one from here (from
`vaso.py`), so I just put `None`...


And finally the data grid.

To install it proceed as usual: add
`collective.z3cform.datagridfield` to your eggs and re-run buildout
(similar to what you did for your package, but no need for the
`develop` part):
```
[buildout]
...
eggs =
    ...
    collective.z3cform.datagridfield

```
Then `./bin/buildout && ./bin/plonectl fg` as usual.

Now you can use it in your content type.
First you need to define what a row in your data-grid will look like.
Define a `zope.schema`:
```python
class DGRow(model.Schema):
    "this zope.schema describes the columns of the data grid/table"

    something = schema.TextLine(
        title=_(u"Just an example"),
    )
    levels = schema.Choice(
        title=_(u"Levels"),
        source="a.b.LevelVocabulary",
    )
```
(in other examples, you can find the name `ITableRowSchema`, but I find it confusing)

And then use it in your conten type:
```python
class IVaso(model.Schema):
    ...
    directives.widget(table_rows=DataGridFieldFactory)
    table_rows = schema.List(
        title=_(u"Many rows"),  # this will be the title of the grid/table
        value_type=DictRow(
            title=u"One row",  # where is this used?
            schema=DGRow,),
    )
```

## This justionale.product

Create new Plone add-on and add 4 content types:
Prodotto e Cliente (simple Items), Riunione (container) and Ordine
(addable only inside Riunione) and one vocabulary.
