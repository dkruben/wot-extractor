# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/modifications_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import ActionType as ActionType
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_modifications_panel_view_model import CompareModificationsPanelViewModel as CompareModificationsPanelViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_modification_model import CompareModificationModel as CompareModificationModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_step_model import CompareStepModel as CompareStepModel
from gui.impl.lobby.veh_post_progression.tooltips.level_tooltip_view import BaseProgressionLevelTooltipView as BaseProgressionLevelTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.pair_modification_tooltip_view import CmpPanelPairModificationTooltipView as CmpPanelPairModificationTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared import event_dispatcher as shared_events
from gui.veh_post_progression.models.modifications import PostProgressionActionTooltip as PostProgressionActionTooltip
from gui.veh_post_progression.models.progression import PostProgressionCompletion as PostProgressionCompletion
from frameworks.wulf import Array as Array, ViewEvent as ViewEvent
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
_ACTION_TOOLTIP_MAP: dict

class CompareModificationsPanelView(ViewImpl):
    __slots__: tuple
    __vehItem: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def update(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onClose(self):
        ...
    def __onClearModifications(self):
        ...
    def __onConfigureModifications(self):
        ...
    def __parseTooltipEvent(self, event):
        ...
    def __updateSteps(self, stepsArray, suitableSteps, postProgression):
        ...
    def __fillModificationModel(self, modificationModel, step, postProgression):
        ...
