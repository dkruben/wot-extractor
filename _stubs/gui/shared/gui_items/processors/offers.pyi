# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/offers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
from AccountCommands import RES_SUCCESS as RES_SUCCESS, RES_FAILURE as RES_FAILURE
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared.gui_items.processors import Processor as Processor, makeI18nError as makeI18nError, makeSuccess as makeSuccess
from gui.shared.gui_items.processors.plugins import MessageConfirmator as MessageConfirmator
from helpers import dependency as dependency
from messenger.formatters.service_channel import QuestAchievesFormatter as QuestAchievesFormatter
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any

class ReceiveOfferGiftProcessor(Processor):
    __offerID: Any
    __giftID: Any
    def __init__(self, offerID, giftID, cdnTitle='', skipConfirm=False):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class ReceiveGiftConfirmator(MessageConfirmator):
    _offerID: Any
    _giftID: Any
    _cdnTitle: Any
    def __init__(self, offerID, giftID, cdnTitle='', isEnabled=True):
        ...
    def _gfMakeMeta(self):
        ...

class ReceiveMultipleOfferGiftsProcessor(Processor):
    ERROR_DEFAULT_KEY = 'offers/server_error'
    ERROR_CODE_MULTI_ERROR = 'MULTI_ERROR'
    __chosenGifts: Any
    def __init__(self, chosenGifts):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class BattleMattersOfferProcessor(ReceiveOfferGiftProcessor):
    __systemMessages: Any
    def _successHandler(self, code, ctx=None):
        ...

class WinbackMultipleOfferProcessor(ReceiveMultipleOfferGiftsProcessor):
    __systemMessages: Any
    def _successHandler(self, code, ctx=None):
        ...
