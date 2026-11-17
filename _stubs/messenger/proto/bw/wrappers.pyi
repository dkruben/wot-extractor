# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as _time
from collections import namedtuple as namedtuple
from past.builtins import unicode as unicode
from chat_shared import SYS_MESSAGE_IMPORTANCE as SYS_MESSAGE_IMPORTANCE
_ChannelData: Any
_ChatActionData: Any
_ServiceChannelData: Any

class ChannelDataWrapper(_ChannelData):
    def __new__(cls, id=0, channelName='Unknown', owner=-1, ownerName='', isReadOnly=False, isSystem=False, isSecured=False, greeting='', flags=0, notifyFlags=0, **kwargs):
        ...

class ChatActionWrapper(_ChatActionData):
    def __new__(cls, action=-1, channel=0, actionResponse=-1, group=0, originator=-1, originatorNickName='Unknown', requestID=-1, data=None, time=..., sentTime=..., flags=0, **kwargs):
        ...

class ServiceChannelMessage(_ServiceChannelData):
    @staticmethod
    def __new__(cls, messageID=-1, user_id=-1, type=-1, importance=..., active=True, personal=False, sentTime=..., started_at=None, finished_at=None, created_at=None, data=None, **kwargs):
        ...
    @property
    def isHighImportance(self):
        ...
    @classmethod
    def fromChatAction(cls, chatAction, personal=False):
        ...
