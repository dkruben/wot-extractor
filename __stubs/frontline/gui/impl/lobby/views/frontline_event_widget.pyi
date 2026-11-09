# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/frontline_event_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import LoadoutParams as LoadoutParams
from frontline.frontline_account_settings import isRentBannerClicked as isRentBannerClicked, setRentBannerClicked as setRentBannerClicked
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineConst as FrontlineConst
from frontline.gui.impl.gen.view_models.views.lobby.views.event_widget_model import EventWidgetModel as EventWidgetModel
from frontline.gui.impl.lobby.states import ProgressionScreenState as ProgressionScreenState, FrontlineBattleAbilitiesLoadoutState as FrontlineBattleAbilitiesLoadoutState
from frontline.gui.impl.lobby.tooltips.banner_tooltip import BannerTooltipView as BannerTooltipView
from frontline.gui.impl.lobby.user_missions.hangar_widget.overlap_ctrl import FLOverlapCtrlMixin as FLOverlapCtrlMixin
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getRentVehicleUrl as getRentVehicleUrl
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.lobby.user_missions.hangar_widget.presenters.constants import UserMissionGroups as UserMissionGroups
from gui.impl.lobby.user_missions.hangar_widget.presenters.base_child_presenter import UserMissionChildPresenter as UserMissionChildPresenter
from gui.impl.lobby.user_missions.hangar_widget.tooltip_positioner import TooltipPositionerMixin as TooltipPositionerMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showShop as showShop, showEpicRewardsSelectionWindow as showEpicRewardsSelectionWindow
from gui.shared.formatters.ranges import toRangeString as toRangeString, toRomanRangeString as toRomanRangeString
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils import isRomanNumberForbidden as isRomanNumberForbidden
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from frontline.gui.frontline_helpers import isFinishedCycleState as isFinishedCycleState, isAnnouncedCycleState as isAnnouncedCycleState, getFrontlineState as getFrontlineState
from PlayerEvents import g_playerEvents as g_playerEvents
from wg_async import wg_async as wg_async, wg_await as wg_await, delay as delay
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
_g_entryLastState: Any

class _LastEntryState(object):
    rewards: Any
    rewardsHash: Any
    def __init__(self):
        ...
    def update(self, rewards=None, rewardsHash=0):
        ...

class BattleAbilitiesLoadoutParams(object):
    loadoutGroupId = AmmunitionPanelConstants.NO_GROUP
    loadoutSectionName = FrontlineConst.BATTLE_ABILITIES
    loadoutSlotIndex = 0
    parameters: dict

# base nao representavel no stub: ViewComponent[...]
class FrontlineEventWidget(UserMissionChildPresenter, TooltipPositionerMixin, FLOverlapCtrlMixin):
    GROUP = UserMissionGroups.EVENTS
    __epicController: Any
    __itemsCache: Any
    __hangarSpace: Any
    __abilitiesPanelCriteria: tuple
    __gameModeStatus: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _prepareRewardsData(self):
        ...
    def _rawUpdate(self, *_, **__):
        ...
    # decorador original: @wg_async
    def __onTokensUpdate(self, diff, _):
        ...
    def __onProgressionClick(self):
        ...
    def __onCombatReservesClick(self):
        ...
    def __onSpaceCreate(self):
        ...
    def __onEpicUpdated(self, *_):
        ...
    def __onGameModeStatusChange(self):
        ...
    def __onVehicleRentClick(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __setRentHightlighted(self):
        ...
    def __fillWidgetModel(self, vm):
        ...
    def __updateBattleAbilitiesPanel(self):
        ...
    def __onChangedVehicle(self):
        ...
