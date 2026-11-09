# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/contacts/note_tasks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.m_constants import USER_ACTION_ID as USER_ACTION_ID, CLIENT_ACTION_ID as CLIENT_ACTION_ID, USER_TAG as USER_TAG
from messenger.proto.entities import SharedUserEntity as SharedUserEntity
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.xmpp import errors as errors
from messenger.proto.xmpp.contacts.tasks import TaskResult as TaskResult, ContactTask as ContactTask, SeqTask as SeqTask
from messenger.proto.xmpp.extensions import contact_note as contact_note
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT as CONTACT_LIMIT
from soft_exception import SoftException as SoftException

class NotesListTask(SeqTask):
    __slots__: tuple
    _offset: Any
    _iqID: Any
    _result: Any
    def __init__(self):
        ...
    def isRequired(self):
        ...
    def result(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...

class _NoteTask(ContactTask):
    def sync(self, name, groups, sub=None, clanInfo=None):
        ...
    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        ...
    def _update(self, note):
        ...

class SetNoteTask(_NoteTask):
    __slots__: tuple
    _text: Any
    _result: Any
    _iqID: Any
    def __init__(self, jid, text):
        ...
    def result(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class RemoveNoteTask(_NoteTask):
    _result: Any
    _iqID: Any
    def result(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class RemoveNotesTask(SeqTask):
    _ids: Any
    _result: Any
    _iqID: Any
    def __init__(self, seq):
        ...
    def result(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...

def canNoteAutoDelete(contact):
    ...
