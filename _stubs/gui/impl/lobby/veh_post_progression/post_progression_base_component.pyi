# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_base_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import range as range
from future.utils import iteritems as iteritems
from Event import Event as Event, EventManager as EventManager
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel as BonusValueModel
from gui.impl.gen.view_models.views.lobby.post_progression.modification_model import RoleCategory as RoleCategory, ModificationModel as ModificationModel
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import ActionType as ActionType
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import ActionState as ActionState
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel as MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel as SingleStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_grid_model import PostProgressionGridModel as PostProgressionGridModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.items_parameters.functions import aggregateKpi as aggregateKpi
from gui.veh_post_progression.models.modifications import PostProgressionActionState as PostProgressionActionState, PostProgressionActionTooltip as PostProgressionActionTooltip
from gui.veh_post_progression.models.progression import PostProgressionAvailability as PostProgressionAvailability, PostProgressionCompletion as PostProgressionCompletion
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from post_progression_common import ACTION_TYPES as ACTION_TYPES, VehicleState as VehicleState
from frameworks.wulf import Array as Array, ViewEvent as ViewEvent
from gui.veh_post_progression.models.modifications import SimpleModItem as SimpleModItem
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel as BonusesModel
from gui.impl.gen.view_models.views.lobby.post_progression.restrictions_model import RestrictionsModel as RestrictionsModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel as PostProgressionBaseViewModel
from gui.shared.gui_items import KPI as KPI
from items.artefacts_helpers import VehicleFilter as VehicleFilter
_NOT_SELECTED_IDX = -1
_ACTION_TYPE_MAP: dict
_ACTION_STATE_MAP: dict
_ACTION_TOOLTIP_MAP: dict
_CATEGORY_MAP: dict

class _SelectionProvider(object):
    __slots__: tuple
    __mainStepsBorder: Any
    __mainStepsSelection: Any
    __multiStepsSelection: Any
    __postProgression: Any
    def __init__(self):
        ...
    def getCustomProgressionState(self):
        ...
    def getSelectedMainSteps(self):
        ...
    def getSelectedMultiSteps(self):
        ...
    def setPostProgression(self, progression):
        ...
    def mergePostProgression(self, progression):
        ...
    def selectMainStep(self, stepID, isInternal=False):
        ...
    def selectMultiStep(self, stepID, modID):
        ...
    def __invalidateRelations(self):
        ...

class PostProgressionBaseComponentView(ViewImpl):
    __slots__: tuple
    _vehicle: Any
    _selectionProvider: Any
    _eventManager: Any
    onCustomProgressionState: Any
    onViewRendered: Any
    def __init__(self, layoutID, model, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onMainStepActionClick(self, args):
        ...
    def _onMultiStepActionClick(self, args):
        ...
    def _updateAll(self, **kwargs):
        ...
    def _updateVehicle(self, **kwargs):
        ...
    def _updateViewModel(self, viewModel, availabilityReason, completion):
        ...
    def _fillBonusesArray(self, bonusesArray, kpiList):
        ...
    def _fillControlsModel(self, model, postProgression):
        ...
    def _fillModification(self, modModel, modification):
        ...
    def _fillMultiStepModel(self, stepModel, step, selectedModID):
        ...
    def _fillPersistentBonuses(self, bonuses, postProgression, completion):
        ...
    def _fillSingleStepModel(self, stepModel, step):
        ...
    def _notifyCustomState(self, needDiff=True):
        ...
    def _parseTooltipEvent(self, event):
        ...
    def __onViewRendered(self):
        ...
    def __onMainStepSelectClick(self, args):
        ...
    def __onMultiStepSelectClick(self, args):
        ...
    def __fillChildrenArray(self, childrenArray, childrenIds):
        ...
    def __fillGridModel(self, grid, postProgression):
        ...
    def __fillModificationsArray(self, modsArray, modifications):
        ...
    def __fillRestrictionsModel(self, restrictionsModel, restrictions):
        ...
    def __updateSelection(self, needDiff=False):
        ...
