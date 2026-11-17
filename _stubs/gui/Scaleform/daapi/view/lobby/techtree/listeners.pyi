# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from logging import getLogger as getLogger
from future.utils import viewitems as viewitems
from collector_vehicle import CollectorVehicleConsts as CollectorVehicleConsts
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController, IVehicleComparisonBasket as IVehicleComparisonBasket, IRentalsController as IRentalsController, IRestoreController as IRestoreController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_INV_ITEM_VCDESC_KEY = 'compDescr'
_CACHE_VEHS_LOCK_KEY = 'vehsLock'
_STAT_DIFF_KEY = 'stats'
_INVENTORY_DIFF_KEY = 'inventory'
_CACHE_DIFF_KEY = 'cache'
_GOODIES_DIFF_KEY = 'goodies'
_STAT_DIFF_FORMAT: Any
_CREDITS_DIFF_KEY: Any
_GOLD_DIFF_KEY: Any
_FREE_XP_DIFF_KEY: Any
_UNLOCKS_DIFF_KEY: Any
_VEH_XP_DIFF_KEY: Any
_ELITE_DIFF_KEY: Any
_BLUEPRINT_DIFF_KEY = 'blueprints'
_BLUEPRINT_SETTINGS_KEY = 'serverSettings.blueprints_config'

class _Listener(object):
    _page: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def startListen(self, page):
        ...
    def stopListen(self):
        ...

class _BlueprintsListener(_Listener):
    __lobbyContext: Any
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def _onBlueprintsUpdate(self, blueprints):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...

class _StatsListener(_Listener):
    __lobbyContext: Any
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def _onCreditsUpdate(self, _):
        ...
    def _onGoldUpdate(self, _):
        ...
    def _onFreeXPUpdate(self, _):
        ...
    def _onEliteVehiclesUpdate(self, elites):
        ...
    def _onVehiclesXPUpdate(self, xps):
        ...
    def _onUnlocksUpdate(self, unlocks):
        ...
    def __onServerSettingsChanged(self, diff):
        ...

class _ItemsCacheListener(_Listener):
    __itemsCache: Any
    __comparisonBasket: Any
    __invalidated: Any
    def __init__(self):
        ...
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def __onInventoryUpdate(self, _):
        ...
    def __onGoodiesUpdate(self, goodies):
        ...
    def __onCacheUpdate(self, cache):
        ...
    def __items_onSyncCompleted(self, reason, invalidated):
        ...
    def __center_onIsLongDisconnected(self, _):
        ...
    def __onVehCompareBasketChanged(self, changedData):
        ...
    def __onVehCompareBasketSwitchChange(self):
        ...

class _WalletStatusListener(_Listener):
    __wallet: Any
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def __onWalletStatusChanged(self, status):
        ...

class _RentChangeListener(_Listener):
    __rentals: Any
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def __onRentChange(self, vehicles):
        ...

class _RestoreListener(_Listener):
    __restores: Any
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def __onRestoreChanged(self, vehicles):
        ...

class _PrbGlobalListener(_Listener, IGlobalListener):
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onPreQueueSettingsChanged(self, diff):
        ...
    def onPlayerStateChanged(self, entity, roster, accountInfo):
        ...
    def onUnitPlayerStateChanged(self, pInfo):
        ...
    def __onDisconnected(self):
        ...

class TTListenerDecorator(_Listener):
    __slots__: tuple
    _stats: Any
    _items: Any
    _wallet: Any
    _prbListener: Any
    _rent: Any
    _restore: Any
    _blueprints: Any
    def __init__(self):
        ...
    def startListen(self, page):
        ...
    def stopListen(self):
        ...
