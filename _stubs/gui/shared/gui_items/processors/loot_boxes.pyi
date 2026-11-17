# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/loot_boxes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from BWUtil import AsyncReturn as AsyncReturn
from debug_utils import deprecated as deprecated
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.shared.formatters.currency import applyAll as applyAll
from helpers.time_utils import getServerUTCTime as getServerUTCTime, makeLocalServerTime as makeLocalServerTime
from lootboxes_common import makeStopRerollTokenID as makeStopRerollTokenID
from messenger.formatters import TimeFormatter as TimeFormatter
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.dialogs import dialogs as dialogs
from gui.lootbox_system.base.awards import addCompensation as addCompensation, preformatRewardsInfo as preformatRewardsInfo
from gui.lootbox_system.base.common import REROLLABLE_BOX_OPEN_COUNT as REROLLABLE_BOX_OPEN_COUNT, getTextResource as getTextResource
from gui.server_events.bonuses import getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.shared.gui_items.processors import Processor as Processor, makeI18nError as makeI18nError, makeSuccess as makeSuccess, makeError as makeError, plugins as plugins
from gui.shared.gui_items.processors.plugins import SyncValidator as SyncValidator
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.money import Currency as Currency, ZERO_MONEY as ZERO_MONEY, Money as Money
from helpers import dependency as dependency
from messenger.formatters.service_channel import LootBoxAchievesFormatter as LootBoxAchievesFormatter, LootBoxSystemAchievesFormatter as LootBoxSystemAchievesFormatter
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from gui.impl.lobby.lootbox_system.base.reset_stats_dialog import ResetStatsDialog as ResetStatsDialog
_logger: Any
_SERVER_ERROR_TEXT_PATH: list
_TRANSACTION_TEXT_PATH: list
_TRANSACTION_SM_TYPE_TEMPLATE = 'LootBox{}Transaction'

class _LootBoxAvailableValidator(SyncValidator):
    _lootBoxes: Any
    _eventName: Any
    _category: Any
    def __init__(self, eventName, category, isEnabled=True):
        ...
    def _validate(self):
        ...

class LootBoxOpenProcessor(Processor):
    __lootBox: Any
    __count: Any
    def __init__(self, lootBoxItem, count=1):
        ...
    def _getCount(self):
        ...
    def _getLootBox(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def _preformatCompensationValue(self, rewardsList):
        ...
    def __getCompensationValue(self, vehicles):
        ...

class LootBoxSystemOpenProcessor(LootBoxOpenProcessor):
    __lootBoxes: Any
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class LootBoxGetInfoProcessor(Processor):
    __lootBoxes: Any
    def __init__(self, lootBoxes):
        ...
    # decorador original: @deprecated
    def _request(self, callback):
        ...

class ResetLootBoxSystemStatisticsProcessor(Processor):
    __boxIDs: Any
    def __init__(self, boxIDs):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...
    # decorador original: @wg_async
    def __showResetStatsDialog(self):
        ...
    def __dialogConfirmator(self):
        ...

class RerollLootBoxProcessor(Processor):
    __lootBoxes: Any
    __eventName: Any
    __category: Any
    def __init__(self, eventName, category):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class AcceptLootBoxRerollProcessor(Processor):
    __lootBoxes: Any
    __eventName: Any
    __category: Any
    def __init__(self, eventName, category):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

def _makeEventError(errStr, eventName):
    ...
def _makeBoxOpenSuccess(eventName, boxName, count, rewardsList, auxData=None):
    ...
