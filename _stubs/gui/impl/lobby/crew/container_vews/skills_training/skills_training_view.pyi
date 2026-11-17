# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/skills_training_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.game_control.wot_plus.wot_plus_crew_assist import CrewAssistantCtrl as CrewAssistantCtrl
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.skills_training_view_model import SkillsTrainingViewModel as SkillsTrainingViewModel
from gui.impl.gen.view_models.views.lobby.crew.sort_dropdown_item_model import SortingTypeEnum as SortingTypeEnum, SortDropdownItemModel as SortDropdownItemModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.container_views.base.components import ContainerBase as ContainerBase
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.crew.container_vews.skills_training import loadSortingOrderType as loadSortingOrderType, saveSortingOrderType as saveSortingOrderType
from gui.impl.lobby.crew.container_vews.skills_training.components.skills_list_component import SkillsListComponent as SkillsListComponent
from gui.impl.lobby.crew.container_vews.skills_training.context import SkillsTrainingViewContext as SkillsTrainingViewContext
from gui.impl.lobby.crew.container_vews.skills_training.controller import SkillsTrainingInteractionController as SkillsTrainingInteractionController
from gui.impl.lobby.crew.crew_helpers import tankmanHasCrewAssistOrderSets as tankmanHasCrewAssistOrderSets
from gui.impl.lobby.crew.tooltips.sorting_dropdown_tooltip import SortingDropdownTooltip as SortingDropdownTooltip
from gui.impl.lobby.crew.widget.crew_widget import CrewWidget as CrewWidget, SkillsTrainingCrewWidget as SkillsTrainingCrewWidget
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import VehicleSkillPreviewParamsPresenter as VehicleSkillPreviewParamsPresenter
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_bus import SharedEvent as SharedEvent
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Type as Type
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase

class SkillsTrainingView(ContainerBase, ViewImpl):
    __slots__: tuple
    itemsCache: Any
    wotPlus: Any
    _SKILLS_COMPONENT_NAME = 'skills_list'
    _crewWidget: Any
    _paramsView: Any
    def __init__(self, **kwargs):
        ...
    @property
    def crewWidget(self):
        ...
    @property
    def paramsView(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getComponents(self):
        ...
    def _getContext(self, *args, **kwargs):
        ...
    def _getInteractionControllerCls(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _finalize(self):
        ...
    def _onWidgetSlotClick(self, tankmanInvID, slotIdx):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onSortSelectionChanged(self, sortingType):
        ...
    def __refreshSorting(self, sortingType):
        ...
    def __onDisconnected(self):
        ...
    def __onEnabledStatusChanged(self, _):
        ...
    def __refreshSkillsComponent(self, vm=None):
        ...
    def __createDropDownViewModel(self, mType, isSelected, isEnabled):
        ...
    def __fillSortingDropDown(self, vm, storedPresetVal):
        ...
    def __onCrewAssistDataChanged(self, _):
        ...

class SkillsTrainingWindow(WindowImpl):
    __slots__: tuple
    _blur: Any
    _callback: Any
    def __init__(self, **kwargs):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
