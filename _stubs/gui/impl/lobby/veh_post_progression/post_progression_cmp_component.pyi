# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_cmp_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import ProgressionState as ProgressionState
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_cmp_view_model import PostProgressionCmpViewModel as PostProgressionCmpViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import StepState as StepState
from gui.impl.lobby.veh_post_progression.post_progression_base_component import PostProgressionBaseComponentView as PostProgressionBaseComponentView
from gui.impl.lobby.veh_post_progression.tooltips.pair_modification_tooltip_view import CmpPairModificationTooltipView as CmpPairModificationTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.level_tooltip_view import CmpProgressionLevelTooltipView as CmpProgressionLevelTooltipView
from gui.veh_post_progression.models.progression import PostProgressionAvailability as PostProgressionAvailability, PostProgressionCompletion as PostProgressionCompletion
from gui.veh_post_progression.models.progression_step import PostProgressionStepState as PostProgressionStepState
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel as BonusesModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel as MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel as SingleStepModel
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
_SINGLE_STEP_STATE_MAP: dict
_MULTI_STEP_STATE_MAP: dict

class PostProgressionCmpComponentView(PostProgressionBaseComponentView):
    __slots__: tuple
    onExitAction: Any
    _vehicle: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def invalidateVehicle(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _updateVehicle(self, isReset=False, **kwargs):
        ...
    def _updateViewModel(self, viewModel, availabilityReason, completion):
        ...
    def _fillControlsModel(self, model, postProgression=None):
        ...
    def _fillMultiStepModel(self, stepModel, step, selectedModID):
        ...
    def _fillPersistentBonuses(self, bonuses, postProgression, completion):
        ...
    def _fillSingleStepModel(self, stepModel, step):
        ...
    def __onApplyAction(self):
        ...
    def __onExitAction(self, *_):
        ...
    def __onResetAction(self):
        ...
