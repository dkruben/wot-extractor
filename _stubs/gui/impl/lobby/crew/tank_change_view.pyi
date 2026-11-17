# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tank_change_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from .base_crew_view import BaseCrewView as BaseCrewView
from .crew_sounds import SOUNDS as SOUNDS
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.filter_panel_widget_model import FilterPanelType as FilterPanelType
from gui.impl.gen.view_models.views.lobby.crew.tank_change_vehicle_model import TankChangeVehicleModel as TankChangeVehicleModel
from gui.impl.gen.view_models.views.lobby.crew.tank_change_view_model import TankChangeViewModel as TankChangeViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.crew.filter import getVehicleLocationSettings as getVehicleLocationSettings, getVehicleTypeSettings as getVehicleTypeSettings, getVehicleTierSettings as getVehicleTierSettings, getVehicleGradeSettings as getVehicleGradeSettings, GRADE_PREMIUM as GRADE_PREMIUM, SEARCH_MAX_LENGTH as SEARCH_MAX_LENGTH
from gui.impl.lobby.crew.filter.data_providers import VehiclesDataProvider as VehiclesDataProvider
from gui.impl.lobby.crew.filter.filter_panel_widget import FilterPanelWidget as FilterPanelWidget
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.impl.lobby.crew.utils import VEHICLE_TAGS_FILTER as VEHICLE_TAGS_FILTER
from gui.shared.event_dispatcher import showChangeCrewMember as showChangeCrewMember
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN, MAX_ROLE_LEVEL as MAX_ROLE_LEVEL, NO_SLOT as NO_SLOT
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache

class TankChangeView(BaseCrewView):
    __slots__: tuple
    itemsCache: Any
    restore: Any
    platoonCtrl: Any
    __selectedTmanInvID: Any
    __tankman: Any
    __vehicle: Any
    _filterPanelWidget: Any
    __filterState: Any
    __dataProvider: Any
    def __init__(self, layoutID, **kwargs):
        ...
    @property
    def tankman(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def selectedTmanInvID(self):
        ...
    @property
    def viewModel(self):
        ...
    def getFilterTypeVehicle(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    @staticmethod
    def getTooltipData(event):
        ...
    def _setWidgets(self, **kwargs):
        ...
    def _fillViewModel(self, vm):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _clear(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _onMembersUpdate(self):
        ...
    def _onInventoryUpdate(self, invDiff):
        ...
    def _onTankmanSlotAutoSelect(self, tankmanID, slotIdx):
        ...
    def _onTankmanSlotClick(self, tankmanInvID, slotIdx):
        ...
    def _findWidgetSlotNextIdx(self, tankmanID, slotIDX):
        ...
    def _onEmptySlotClick(self, tankmanID, slotIdx):
        ...
    def _onFilterStateUpdated(self):
        ...
    def _onResetFilters(self):
        ...
    # decorador original: @args2params(...)
    def _onVehicleSelected(self, vehicleID):
        ...
    def _onVehicleUpdated(self, _):
        ...
    def __updateModelsData(self):
        ...
    def __isValidForTraining(self, vehicle):
        ...
    def __fillVehicleList(self, tx):
        ...
