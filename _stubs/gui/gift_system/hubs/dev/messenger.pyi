# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/gift_system/hubs/dev/messenger.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.gift_system.hubs.base.messenger import GiftEventBaseMessenger as GiftEventBaseMessenger
from gui.gift_system.hubs.dev import IDevMessagesPusher as IDevMessagesPusher
from gui.shared.formatters import text_styles as text_styles
from gui.gift_system.wrappers import GiftsHistoryData as GiftsHistoryData, IncomeSysMessage as IncomeSysMessage, SendGiftResponse as SendGiftResponse
_logger: Any

class GiftEventDevMessenger(GiftEventBaseMessenger, IDevMessagesPusher):
    __slots__: tuple
    def __repr__(self):
        ...
    @classmethod
    def _formatMessage(cls, message):
        ...
    def _pushHistoryMessage(self, history):
        ...
    def _pushIncomeMessage(self, incomeData):
        ...
    def _pushOutcomeMessage(self, outcomeData):
        ...
