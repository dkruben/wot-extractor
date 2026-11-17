# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_blacklist/maps_blacklist_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import ArenaType as ArenaType
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREMIUM_TYPE as PREMIUM_TYPE, PremiumConfigs as PremiumConfigs
from frameworks.wulf import View as View, ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui import SystemMessages as SystemMessages
from gui.Scaleform import MENU as MENU
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl as getWotPlusShopUrl, getBuyPremiumUrl as getBuyPremiumUrl
from gui.game_control.wot_plus.utils import getExcludedMapsPromoData as getExcludedMapsPromoData
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_dashboard.map_model import SlotTypeEnum as SlotTypeEnum
from gui.impl.gen.view_models.views.lobby.excluded_maps.excluded_maps_tooltip_model import ExcludedMapsTooltipModel as ExcludedMapsTooltipModel
from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_map_filter_model import MapsBlacklistMapFilterModel as MapsBlacklistMapFilterModel
from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_slot_model import MapsBlacklistSlotModel as MapsBlacklistSlotModel, MapStateEnum as MapStateEnum
from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_view_model import MapsBlacklistViewModel as MapsBlacklistViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.maps_blacklist.maps_blacklist_confirm_view import MapsBlacklistDialog as MapsBlacklistDialog
from gui.impl.lobby.common.sound_constants import HANGAR_FILTERED_SOUND_SPACE as HANGAR_FILTERED_SOUND_SPACE
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.formatters import time_formatters as time_formatters
from gui.shared.gui_items.processors.common import MapsBlackListSetter as MapsBlackListSetter, MapsBlackListChanger as MapsBlackListChanger, MapsBlackListRemover as MapsBlackListRemover
from gui.shared.utils import decorators as decorators
from gui.shared.utils.scheduled_notifications import AcyclicNotifier as AcyclicNotifier, Notifiable as Notifiable
from helpers import dependency as dependency
from helpers import i18n as i18n
from helpers import time_utils as time_utils
from items.vehicles import CAMOUFLAGE_KINDS as CAMOUFLAGE_KINDS
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from wg_async import wg_await as wg_await, wg_async as wg_async
from typing import List as List, Type as Type, Any as Any, Dict as Dict, Optional as Optional
from frameworks.wulf import ViewEvent as ViewEvent
_logger: _Any

class MapsBlacklistView(ViewImpl):
    __lobbyContext: _Any
    __gameSession: _Any
    __wotPlusCtrl: _Any
    _COMMON_SOUND_SPACE = HANGAR_FILTERED_SOUND_SPACE
    __availableMaps: _Any
    minTimeToWait: _Any
    __notifier: _Any
    def __init__(self, layoutID, wsFlags=..., viewModelClazz=..., exitEvent=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, exitEvent):
        ...
    def _finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onWindowClose(self):
        ...
    # decorador original: @args2params(...)
    def __onFilterSelected(self, seasonID):
        ...
    def __onFilterReset(self, _=None):
        ...
    def __applyFilter(self, viewModel):
        ...
    # decorador original: @args2params(...)
    def __onMapAddToBlacklist(self, mapId):
        ...
    # decorador original: @args2params(...)
    def __onMapRemoveFromBlacklist(self, mapId):
        ...
    def __onDestroy(self, _=None):
        ...
    def __initFilterData(self):
        ...
    def __updateAvailableMaps(self):
        ...
    def __updateMainData(self, viewModel):
        ...
    def __updateDisabledMaps(self, viewModel):
        ...
    def __update(self, *args, **kwargs):
        ...
    def __onWotPlusChanged(self, data):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __hasFreeOrExpiredSlots(self):
        ...
    def __getDisabledMap(self, mapName):
        ...
    # decorador original: @wg_async
    def __showMapConfirmDialog(self, mapId):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __sendMapChangingRequest(self, mapToSet, mapToChange):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __sendMapRemovingRequest(self, removeMapName):
        ...
    @staticmethod
    def __mapNameToID(mapName):
        ...
    def __onShopOpenWotPlus(self):
        ...
    def __onShopOpenPremium(self):
        ...

class ExcludedMapsTooltip(ViewImpl):
    __slots__: tuple
    _lobbyContext: _Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def buildSlotsMap(lobbyContext=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def buildSlotsModels(lobbyContext=None, itemsCache=None):
    ...
