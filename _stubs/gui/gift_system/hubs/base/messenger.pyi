# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/base/messenger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.gift_system.constants import GiftMessageType as GiftMessageType
from gui.gift_system.hubs.subsystems import BaseMessegesDelayer as BaseMessegesDelayer
from gui.gift_system.wrappers import ifMessagesEnabled as ifMessagesEnabled, ifMessagesAllowed as ifMessagesAllowed
from helpers.server_settings import GiftEventConfig as GiftEventConfig
from gui.gift_system.wrappers import GiftsHistoryData as GiftsHistoryData, IncomeSysMessage as IncomeSysMessage, SendGiftResponse as SendGiftResponse

class IGiftEventMessenger(BaseMessegesDelayer):
    def isMessagesEnabled(self):
        ...
    def isMessagesSuspended(self, *args, **kwargs):
        ...
    def setMessagesAllowed(self, isMessagesAllowed):
        ...
    def pushHistoryMessage(self, history):
        ...
    def pushIncomeMessage(self, incomeData):
        ...
    def pushOutcomeMessage(self, outcomeData):
        ...

class GiftEventBaseMessenger(IGiftEventMessenger):
    __slots__: tuple
    __isMessagesAllowed: Any
    def __init__(self, eventSettings, isMessagesAllowed):
        ...
    def isMessagesEnabled(self):
        ...
    def isMessagesSuspended(self, *args, **kwargs):
        ...
    def setMessagesAllowed(self, isMessagesAllowed):
        ...
    # decorador original: @ifMessagesEnabled
    # decorador original: @ifMessagesAllowed(...)
    def pushHistoryMessage(self, history):
        ...
    # decorador original: @ifMessagesEnabled
    # decorador original: @ifMessagesAllowed(...)
    def pushIncomeMessage(self, incomeData):
        ...
    # decorador original: @ifMessagesEnabled
    # decorador original: @ifMessagesAllowed(...)
    def pushOutcomeMessage(self, outcomeData):
        ...
    def updateSettings(self, eventSettings):
        ...
    def _pushHistoryMessage(self, history):
        ...
    def _pushIncomeMessage(self, incomeData):
        ...
    def _pushOutcomeMessage(self, outcomeData):
        ...
