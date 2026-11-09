# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/subsystems.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.gift_system.constants import GiftMessageType as GiftMessageType
from helpers.server_settings import GiftEventConfig as GiftEventConfig

class BaseHubSubsystem(object):
    __slots__: tuple
    _settings: Any
    def __init__(self, eventSettings):
        ...
    def destroy(self):
        ...
    def reset(self):
        ...
    def updateSettings(self, eventSettings):
        ...

class BaseMessegesDelayer(BaseHubSubsystem):
    __slots__: tuple
    _msgHandlers: Any
    _msgQueue: Any
    def __init__(self, eventSettings):
        ...
    def destroy(self):
        ...
    def isMessagesEnabled(self):
        ...
    def isMessagesSuspended(self, *args, **kwargs):
        ...
    def addToQueue(self, msgType, msgData):
        ...
    def _clearMessagesQueue(self):
        ...
    def _processMessagesQueue(self):
        ...
