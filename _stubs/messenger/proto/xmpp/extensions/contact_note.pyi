# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/contact_note.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring, long as long
from helpers import html as html
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, PyQuery as PyQuery
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.rsm import RqResultSet as RqResultSet, ResultSet as ResultSet
from messenger.proto.xmpp.extensions.shared_handlers import IQHandler as IQHandler
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE

class NoteID(PyExtension):
    __slots__: tuple
    _dbID: Any
    def __init__(self, dbID=0):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
    def _makeChildrenString(self):
        ...

class NoteText(PyExtension):
    __slots__: tuple
    _text: Any
    def __init__(self, text=''):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getTag(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...
    def _makeChildrenString(self):
        ...

class NoteItem(PyExtension):
    def __init__(self, dbID=0, text=''):
        ...
    def getDefaultData(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class NoteList(PyExtension):
    def __init__(self, items=None, rsm=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
    def _getXPathAttr(self):
        ...

class NoteQuery(PyExtension):
    def __init__(self, items=None, rsm=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class NotesListQuery(PyQuery):
    def __init__(self, max=0, after=None):
        ...

class NotesListHandler(IQHandler):
    def __init__(self):
        ...

class SetNoteQuery(PyQuery):
    def __init__(self, dbID, text):
        ...

class SetNotesQuery(PyQuery):
    def __init__(self, items):
        ...

class RemoveNoteQuery(PyQuery):
    def __init__(self, dbID):
        ...

class RemoveNotesQuery(PyQuery):
    def __init__(self, dbIDs):
        ...
