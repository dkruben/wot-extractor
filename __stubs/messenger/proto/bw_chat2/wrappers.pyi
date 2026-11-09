# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.moves import pickle as pickle
from past.builtins import unicode as unicode, long as long
from gui.shared.utils import transport as transport
from helpers.time_utils import makeLocalServerTime as makeLocalServerTime
from messenger.proto.entities import SharedUserEntity as SharedUserEntity, ClanInfo as ClanInfo
from messenger_common_chat2 import messageArgs as messageArgs
ChannelProtoData: Any

class _MessageVO(object):
    __slots__: tuple
    accountDBID: Any
    avatarSessionID: Any
    vehicleID: Any
    text: Any
    sentAt: Any
    accountName: Any
    def __init__(self, floatArg1=0, strArg1='', **kwargs):
        ...

class ArenaMessageVO(_MessageVO):
    __slots__: tuple
    vehicleID: Any
    isCommonChannel: Any
    def __init__(self, floatArg1=0, int32Arg1=False, int64Arg1=0, strArg1='', **kwargs):
        ...

class UnitMessageVO(_MessageVO):
    accountDBID: Any
    accountName: Any
    def __init__(self, floatArg1=0, int64Arg1=0, strArg1='', strArg2='', **kwargs):
        ...

class IDataFactory(object):
    def broadcastArgs(self, text, *args):
        ...
    def historyIter(self, args):
        ...
    def messageVO(self, args):
        ...

class ArenaDataFactory(IDataFactory):
    def broadcastArgs(self, text, *args):
        ...
    def historyIter(self, args):
        ...
    def messageVO(self, args):
        ...

class UnitDataFactory(IDataFactory):
    def broadcastArgs(self, text, *args):
        ...
    def historyIter(self, args):
        ...
    def messageVO(self, args):
        ...

class CHAT_TYPE(object):
    UNIT = 1
    ARENA = 2

def UnitHistoryIterator(value):
    ...
def ArenaHistoryIterator(value):
    ...
def SearchResultIterator(value):
    ...
