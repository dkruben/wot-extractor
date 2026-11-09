# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/contacts/block_tasks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from shared_utils import findFirst as findFirst
from messenger.m_constants import USER_ACTION_ID as USER_ACTION_ID, USER_TAG as USER_TAG, PROTO_TYPE as PROTO_TYPE, CLIENT_ACTION_ID as CLIENT_ACTION_ID
from messenger.proto.xmpp import entities as entities, errors as errors
from messenger.proto.xmpp.contacts.tasks import TaskResult as TaskResult, ContactTask as ContactTask, SeqTask as SeqTask, IQTask as IQTask
from messenger.proto.xmpp.extensions import blocking_cmd as blocking_cmd
from messenger.proto.xmpp.find_criteria import ItemsFindCriteria as ItemsFindCriteria
from messenger.proto.xmpp.jid import ContactJID as ContactJID
from messenger.proto.xmpp.log_output import g_logOutput as g_logOutput, CLIENT_LOG_AREA as CLIENT_LOG_AREA
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE as XMPP_ITEM_TYPE
from messenger.proto.xmpp.xmpp_items import BlockItem as BlockItem
from soft_exception import SoftException as SoftException

class _BlockItemTask(ContactTask):
    def sync(self, name, groups, sub=None, clanInfo=None):
        ...
    def _doSync(self, name, groups=None, sub=None, clanInfo=None):
        ...

class BlockListResultTask(SeqTask):
    _result: Any
    _iqID: Any
    def result(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...

class AddBlockItemTask(_BlockItemTask):
    _iqID: Any
    _result: Any
    def set(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class RemoveBlockItemTask(_BlockItemTask):
    _iqID: Any
    _result: Any
    def set(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...
    def _getError(self, pyGlooxTag):
        ...

class SyncBlockItemTask(IQTask):
    __slots__: tuple
    _handlers: Any
    def __init__(self):
        ...
    def set(self, pyGlooxTag):
        ...
    def _doRun(self, client):
        ...

def _syncBlockItem(storage, jid, name='', dbID=0, clanInfo=None):
    ...
