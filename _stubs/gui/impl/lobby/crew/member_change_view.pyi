# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/member_change_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.game_control import restore_contoller as restore_contoller
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.filter_panel_widget_model import FilterPanelType as FilterPanelType
from gui.impl.gen.view_models.views.lobby.crew.member_change_tankman_model import MemberChangeTankmanModel as MemberChangeTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.member_change_view_model import MemberChangeViewModel as MemberChangeViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanCardState as TankmanCardState, TankmanKind as TankmanKind
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.base_crew_view import BaseCrewView as BaseCrewView
from gui.impl.lobby.crew.base_tankman_list_view import BaseTankmanListView as BaseTankmanListView
from gui.impl.lobby.crew.crew_helpers.model_setters import setRecruitTankmanModel as setRecruitTankmanModel, setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.lobby.crew.filter import getTankmanKindSettings as getTankmanKindSettings, getTankmanLocationSettings as getTankmanLocationSettings, getTankmanRoleSettings as getTankmanRoleSettings, getVehicleTierSettings as getVehicleTierSettings, getVehicleTypeSettings as getVehicleTypeSettings
from gui.impl.lobby.crew.filter.data_providers import CompoundDataProvider as CompoundDataProvider, RecruitsChangeDataProvider as RecruitsChangeDataProvider, TankmenChangeDataProvider as TankmenChangeDataProvider
from gui.impl.lobby.crew.filter.filter_panel_widget import FilterPanelWidget as FilterPanelWidget
from gui.impl.lobby.crew.filter.state import FilterState as FilterState, Persistor as Persistor
from gui.impl.lobby.crew.utils import discountPercent as discountPercent
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import VehicleSkillPreviewParamsPresenter as VehicleSkillPreviewParamsPresenter
from gui.server_events.events_dispatcher import showRecruitWindow as showRecruitWindow
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.game_control import IRestoreController as IRestoreController, ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils.requesters import IShopRequester as IShopRequester
from PlayerEvents import g_playerEvents as g_playerEvents
from AccountCommands import LOCK_REASON as LOCK_REASON

class MemberChangeView(BaseCrewView, BaseTankmanListView):
    itemsCache: Any
    restore: Any
    specialSounds: Any
    __currentVehicle: Any
    __tankmanId: Any
    __slotIdx: Any
    __requiredRole: Any
    __tankman: Any
    __filterPanelWidget: Any
    __filterState: Any
    __dataProviders: Any
    __requiredNation: Any
    __paramsView: Any
    __hasFilters: Any
    def __init__(self, layoutID, **kwargs):
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
    @property
    def viewModel(self):
        ...
    def selectSlot(self, slotIdx):
        ...
    def _createDataProvider(self):
        ...
    def _getDefaultFilters(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _setWidgets(self, **kwargs):
        ...
    def _fillTankmen(self, cardsList, limit, offset):
        ...
    def _fillViewModel(self, vm):
        ...
    def _fillTankmenList(self, tx):
        ...
    def _fillVisibleCards(self, cardsList):
        ...
    def _fillTankmanCard(self, cardsList, tankman):
        ...
    def _fillRecruitCard(self, cardsList, recruitInfo):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def widgetAutoSelectSlot(self, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onItemsCacheSyncCompleted(self, reason, _):
        ...
    def _onVehicleLockChanged(self, _, lockReason):
        ...
    def _onEmptySlotClick(self, tankmanID, slotIdx):
        ...
    def _onFilterStateUpdated(self):
        ...
    def _onClose(self, params=None):
        ...
    def _onDataChanged(self):
        ...
    def _onWidgetChangeCrewClick(self, _, slotIdx, __):
        ...
    def _onResetFilters(self):
        ...
    def _onCrewChanged(self, *_, **__):
        ...
    def _onChangeSlotIdx(self, slotIdx):
        ...
    # decorador original: @args2params(...)
    def _onTankmanSelected(self, tankmanID):
        ...
    # decorador original: @args2params(...)
    def _onPlayRecruitVoiceover(self, recruitID):
        ...
    # decorador original: @args2params(...)
    def _onRecruitSelected(self, recruitID):
        ...
    # decorador original: @args2params(...)
    def _onTankmanRestore(self, tankmanID):
        ...
    def _onRecruitNewTankman(self):
        ...
    @property
    def __roleChangeDiscountPercent(self):
        ...
    @property
    def __isChangeRoleDiscountAvailable(self):
        ...
    def __getPopoverGroupSettings(self):
        ...
    def __updatedRoleChangeCost(self):
        ...
    def __equipTankman(self, newTankman):
        ...
    def __changeRoleAndEquipConfirm(self, newTankman):
        ...
    def __createTankmanModelByTankman(self, tankman):
        ...
    def __updateTankmanData(self, slotIdx):
        ...
