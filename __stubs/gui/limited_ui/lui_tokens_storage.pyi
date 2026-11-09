# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/limited_ui/lui_tokens_storage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from itertools import chain as chain
import typing as typing
from future.utils import itervalues as itervalues
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.system_factory import collectLimitedUITokens as collectLimitedUITokens, registerLimitedUITokens as registerLimitedUITokens
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items import getTypeOfCompactDescr as getTypeOfCompactDescr
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IAchievementsController as IAchievementsController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, Union as Union, Tuple as Tuple, Callable as Callable
LimitedUITokenInfo: Any
_VEHICLE_LEVEL_TOKENS: Any
_REGISTER_TOKENS: Any

class LimitedUICondition(object):
    __slots__: tuple
    __tokenID: Any
    __value: Any
    __isActive: Any
    onConditionValueUpdated: Any
    def __init__(self, tokenID):
        ...
    def initialize(self, *args):
        ...
    @property
    def tokenID(self):
        ...
    def value(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def finalize(self):
        ...
    def _getValue(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def _clear(self):
        ...
    def _update(self, *_, **__):
        ...

class _PermanentTrue(LimitedUICondition):
    __slots__: tuple
    def _getValue(self):
        ...

class _PermanentFalse(LimitedUICondition):
    __slots__: tuple
    def _getValue(self):
        ...

class _BattleCountCondition(LimitedUICondition):
    __slots__: tuple
    __itemsCache: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...
    def __onSyncCompleted(self, reason, diff):
        ...

class _BattleMattersCompletedQuests(LimitedUICondition):
    __slots__: tuple
    __battleMattersController: Any
    __eventsCache: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _VehicleInventoryUpdater(object):
    __itemsCache: Any
    _instance = None
    __subscribers: Any
    __isActive: Any
    __inventoryVehicles: Any
    __criteria: Any
    onValueUpdated: Any
    @classmethod
    def getInstance(cls):
        ...
    def __init__(self):
        ...
    def clear(self):
        ...
    def subscribe(self, ruleID):
        ...
    def unsubscribe(self, ruleID):
        ...
    def getValue(self, criteria):
        ...
    def __updateActivity(self):
        ...
    def __activate(self):
        ...
    def __deactivate(self):
        ...
    def __update(self, *_):
        ...
    def __updateCache(self):
        ...
    def __clearCache(self):
        ...

class _VehicleCondition(LimitedUICondition):
    __slots__: tuple
    __itemsCache: Any
    __criteria: Any
    def __init__(self, tokenID):
        ...
    def initialize(self, level, *args):
        ...
    @property
    def criteria(self):
        ...
    def _makeCriteria(self, level):
        ...
    def _getValue(self):
        ...

class _VehicleInventoryCondition(_VehicleCondition):
    __slots__: tuple
    __vehicleUpdater: Any
    def __init__(self, tokenID):
        ...
    def initialize(self, level, *args):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def finalize(self):
        ...
    def _clear(self):
        ...
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _MinVehicleLevel(_VehicleInventoryCondition):
    __slots__: tuple
    def _makeCriteria(self, level):
        ...

class _MinNonPremiumVehicleLevel(_MinVehicleLevel):
    __slots__: tuple
    def _makeCriteria(self, level):
        ...

class _MinUnlockedVehicleLevel(_VehicleCondition):
    __slots__: tuple
    def _makeCriteria(self, level):
        ...
    def _getCallbacks(self):
        ...
    def __onUnlocksUpdate(self, unlocks):
        ...

class _DailyMissionsCompletedCount(LimitedUICondition):
    __slots__: tuple
    __eventsCache: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _BattlePassPoints(LimitedUICondition):
    __slots__: tuple
    __battlePass: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _PersonalMissionsActive(LimitedUICondition):
    __slots__: tuple
    __eventsCache: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _BluePrintsAvailability(LimitedUICondition):
    __slots__: tuple
    __itemsCache: Any
    def _getValue(self):
        ...
    def _getCallbacks(self):
        ...

class _PersonalReservesAvailability(LimitedUICondition):
    __slots__: tuple
    __goodiesCache: Any
    __itemsCache: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

class _WereRealMoneyExpenses(LimitedUICondition):
    __slots__: tuple
    __itemsCache: Any
    __REAL_MONEY_EXPENSES_ENTITLEMENT = 'real_money_expenses'
    def _getValue(self):
        ...
    def _getCallbacks(self):
        ...
    def __updateEntitlements(self, entitlements):
        ...

class _AdvancedAchievementsCount(LimitedUICondition):
    __slots__: tuple
    __advAchmntCtrl: Any
    def _getValue(self):
        ...
    def _getEvents(self):
        ...

def getTokensInfo():
    ...
