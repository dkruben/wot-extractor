# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/unit_chat_cmd.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto.entities import OutChatCommand as OutChatCommand, ReceivedUnitChatCommand as ReceivedUnitChatCommand
from messenger.proto.interfaces import IUnitCommandFactory as IUnitCommandFactory
from messenger_common_chat2 import messageArgs as messageArgs
from messenger_common_chat2 import UNIT_CHAT_COMMANDS as UNIT_CHAT_COMMANDS, UNIT_CHAT_COMMANDS_BY_NAMES as UNIT_CHAT_COMMANDS_BY_NAMES
_MINIMAP_CMD_ID = 0

class _OutCmdDecorator(OutChatCommand):
    __slots__: tuple
    _name: Any
    def __init__(self, name, args=None):
        ...
    def getID(self):
        ...
    def getProtoType(self):
        ...
    def getCommand(self):
        ...

class _ReceivedCmdDecorator(ReceivedUnitChatCommand):
    __slots__: tuple
    _commandID: Any
    def __init__(self, commandID, args):
        ...
    def getID(self):
        ...
    def getProtoType(self):
        ...
    def getCommandText(self):
        ...
    def getMapPosX(self):
        ...
    def getMapPosY(self):
        ...
    def isOnMinimap(self):
        ...

class UnitCommandFactory(IUnitCommandFactory):
    @staticmethod
    def createByAction(actionID, args):
        ...
    def createByMapPos(self, x, y):
        ...
