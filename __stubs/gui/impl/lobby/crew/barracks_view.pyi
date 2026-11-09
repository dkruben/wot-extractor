# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/barracks_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.genConsts.BARRACKS_CONSTANTS import BARRACKS_CONSTANTS as BARRACKS_CONSTANTS
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.game_control import restore_contoller as restore_contoller
from gui.impl import backport as backport
from gui.impl.backport import createContextMenuData as createContextMenuData, BackportContextMenuWindow as BackportContextMenuWindow
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.barracks_view_model import BarracksViewModel as BarracksViewModel
from gui.impl.gen.view_models.views.lobby.crew.filter_panel_widget_model import FilterPanelType as FilterPanelType
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel as TankmanModel, TankmanKind as TankmanKind
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.base_tankman_list_view import BaseTankmanListView as BaseTankmanListView
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel, setRecruitTankmanModel as setRecruitTankmanModel
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getBethsSlotsCount as getBethsSlotsCount
from gui.impl.lobby.crew.filter import getTankmanKindSettings as getTankmanKindSettings, getNationSettings as getNationSettings, getTankmanRoleSettings as getTankmanRoleSettings, getVehicleTypeSettings as getVehicleTypeSettings, getVehicleTierSettings as getVehicleTierSettings, getVehicleGradeSettings as getVehicleGradeSettings, SEARCH_MAX_LENGTH as SEARCH_MAX_LENGTH
from gui.impl.lobby.crew.filter.data_providers import CompoundDataProvider as CompoundDataProvider, TankmenDataProvider as TankmenDataProvider, RecruitsDataProvider as RecruitsDataProvider
from gui.impl.lobby.crew.filter.filter_panel_widget import FilterPanelWidget as FilterPanelWidget
from gui.impl.lobby.crew.tooltips.retire_undertrained_tooltip import RetireUndertrainedTooltip as RetireUndertrainedTooltip
from gui.impl.lobby.crew.widget.crew_banner_widget import CrewBannerWidget as CrewBannerWidget
from gui.impl.lobby.crew.filter.state import FilterState as FilterState, Persistor as Persistor
from gui.impl.lobby.crew.tooltips.bunks_confirm_discount_tooltip import BunksConfirmDiscountTooltip as BunksConfirmDiscountTooltip
from gui.server_events import recruit_helper as recruit_helper
from gui.server_events.events_dispatcher import showRecruitWindow as showRecruitWindow
from gui.shared.event_dispatcher import showPersonalCase as showPersonalCase, showHangar as showHangar, showJunkTankmenConversion as showJunkTankmenConversion
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IRestoreController as IRestoreController, ICrewController as ICrewController
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_await as wg_await, wg_async as wg_async

class BarracksView(BaseTankmanListView):
    itemsCache: Any
    restore: Any
    specialSounds: Any
    eventsCache: Any
    crewController: Any
    __slots__: tuple
    __berthPrice: Any
    __berthsInPack: Any
    __defaultBerthPrice: Any
    __hasFilters: Any
    __filterState: Any
    __filterPanelWidget: Any
    __bannerWidget: Any
    __dataProviders: Any
    __tankmenStatsCache: Any
    __recruitsForVisit: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def createContextMenu(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _updateJunkTankmenBtn(self, tx):
        ...
    def _onVehicleLockChanged(self, _, __):
        ...
    def _getEvents(self):
        ...
    @property
    def _tankmenProvider(self):
        ...
    @property
    def _recruitsProvider(self):
        ...
    @property
    def _filterState(self):
        ...
    def _getCallbacks(self):
        ...
    def _fillTankmanCard(self, cardsList, tankman):
        ...
    def _fillVisibleCards(self, cardsList):
        ...
    def _fillRecruitCard(self, cardsList, recruitInfo):
        ...
    def __onInventoryUpdate(self, invDiff):
        ...
    def __onNewRecruits(self, *_):
        ...
    def __onJunkTankmanChanged(self):
        ...
    def __onTankmenBufferUpdated(self):
        ...
    def __onTankmenBerthsCountUpdate(self, *_):
        ...
    def __onBerthsPricesChanged(self, *_):
        ...
    def __onFilterStateUpdated(self):
        ...
    def __onResetFilters(self):
        ...
    def __onRetireUndertrained(self):
        ...
    # decorador original: @wg_async
    def __onClickBuyBerth(self):
        ...
    # decorador original: @args2params(...)
    def __onNewTankmanHovered(self, index, recruitID):
        ...
    # decorador original: @args2params(...)
    def __onTankmanSelected(self, tankmanID):
        ...
    # decorador original: @args2params(...)
    def __onTankmanRecruit(self, recruitID):
        ...
    # decorador original: @args2params(...)
    def __onTankmanDismiss(self, tankmanID):
        ...
    # decorador original: @args2params(...)
    def __onPlayTankmanVoiceover(self, recruitID):
        ...
    def __initFilterPanelWidget(self):
        ...
    def __fillCardList(self):
        ...
    def __showHangar(self):
        ...
    def __refreshRecruitsForVisit(self):
        ...
