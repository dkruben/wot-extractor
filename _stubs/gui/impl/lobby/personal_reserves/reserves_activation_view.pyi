# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/reserves_activation_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, Array as Array, ViewEvent as ViewEvent, ViewModel as ViewModel
from goodies.goodie_constants import BoosterCategory as BoosterCategory
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPersonalReservesUrl as getBuyPersonalReservesUrl
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control import BoostersController as BoostersController
from gui.goodies.goodie_items import ClanReservePresenter as ClanReservePresenter
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import PERSONAL_RESOURCE_ORDER as PERSONAL_RESOURCE_ORDER, GOODIES_TYPE_TO_CLAN_BOOSTERS as GOODIES_TYPE_TO_CLAN_BOOSTERS
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import getPersonalBoosterModelDataByResourceType as getPersonalBoosterModelDataByResourceType, addPersonalBoostersGroup as addPersonalBoostersGroup, addBoosterModel as addBoosterModel, addEventGroup as addEventGroup
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_activation_view_model import ReservesActivationViewModel as ReservesActivationViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel as ReservesGroupModel, GroupCategory as GroupCategory
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.personal_reserves import boosterActivationFlow as boosterActivationFlow
from gui.impl.lobby.personal_reserves.booster_tooltip import BoosterTooltip as BoosterTooltip
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getNearestExpirationTimeAndCountForToday as getNearestExpirationTimeAndCountForToday
from gui.impl.lobby.personal_reserves.reserves_constants import PERSONAL_RESERVES_SOUND_SPACE as PERSONAL_RESERVES_SOUND_SPACE
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.settings import getPersonalReservesSettings as getPersonalReservesSettings
from gui.shared.event_dispatcher import showStorage as showStorage, showPersonalReservesIntro as showPersonalReservesIntro
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.money import Currency as Currency
from gui.shared.tooltips import contexts as contexts
from helpers import dependency as dependency
from skeletons.gui.game_control import IBoostersController as IBoostersController, IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Dict as Dict, List as List, Optional as Optional
from gui.game_control.epic_meta_game_ctrl import EpicBattleMetaGameController as EpicBattleMetaGameController
from gui.goodies.goodies_cache import GoodiesCache as GoodiesCache
from gui.shared.items_cache import ItemsCache as ItemsCache
from gui.wgcg.web_controller import WebController as WebController
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import BoosterModelData as BoosterModelData
_logger: Any

class ReservesActivationView(ViewImpl, EventSystemEntity):
    _COMMON_SOUND_SPACE = PERSONAL_RESERVES_SOUND_SPACE
    _goodiesCache: Any
    _boosters: Any
    _itemsCache: Any
    _webController: Any
    _epicController: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self):
        ...
    def getClanBoostersByType(self):
        ...
    def fillViewModel(self):
        ...
    def addClanGroup(self, groupsArray):
        ...
    def onBoostersDataUpdate(self):
        ...
    def onPersonalReserveTick(self):
        ...
    def onClose(self, *args, **kwargs):
        ...
    # decorador original: @args2params(...)
    def onBoosterActivate(self, boosterId):
        ...
    # decorador original: @args2params(...)
    def onCardHover(self, boosterId):
        ...
    def onNavigateToStore(self):
        ...
    def onNavigateToDepot(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onCurrencyBalanceChanged(self, _):
        ...
    def __onEpicUpdate(self, diff, *_):
        ...
