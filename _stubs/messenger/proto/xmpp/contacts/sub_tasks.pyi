# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/contacts/sub_tasks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.m_constants import USER_TAG as USER_TAG, USER_ACTION_ID as USER_ACTION_ID, CLIENT_ACTION_ID as CLIENT_ACTION_ID
from messenger.proto.xmpp import errors as errors
from messenger.proto.xmpp.contacts.roster_tasks import SyncSubscriptionTask as SyncSubscriptionTask
from messenger.proto.xmpp.contacts.tasks import TaskResult as TaskResult
from messenger.proto.xmpp.gloox_constants import SUBSCRIPTION as _SUB

class AskSubscriptionTask(SyncSubscriptionTask):
    _result: Any
    def sync(self, name, groups, sub=None, clanInfo=None):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class _ChangeSubscriptionTask(SyncSubscriptionTask):
    __slots__: tuple
    _auto: Any
    def __init__(self, jid, name='', auto=False):
        ...

class ApproveSubscriptionTask(_ChangeSubscriptionTask):
    __slots__: tuple
    _tasks: Any
    _result: Any
    def __init__(self, jid, name='', auto=False):
        ...
    def clone(self):
        ...
    def sync(self, name, groups, sub=None, clanInfo=None):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class CancelSubscriptionTask(_ChangeSubscriptionTask):
    def isInstantaneous(self):
        ...
    def _doRun(self, client):
        ...
