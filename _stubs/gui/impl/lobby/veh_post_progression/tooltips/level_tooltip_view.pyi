# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/tooltips/level_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel as BonusValueModel
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.post_progression_level_tooltip_view_model import PostProgressionLevelTooltipViewModel as PostProgressionLevelTooltipViewModel, ModificationType as ModificationType
from gui.impl.pub import ViewImpl as ViewImpl
from frameworks.wulf import Array as Array
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.veh_post_progression.models.modifications import SimpleModItem as SimpleModItem
from gui.veh_post_progression.models.progression import PostProgressionItem as PostProgressionItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem

class BaseProgressionLevelTooltipView(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehicle, stepID, *args, **kwargs):
        ...
    def _getIsUnlocked(self, step):
        ...
    def _getModificationType(self, postProgression, step):
        ...
    def __fillModifiers(self, vehicle, modifiers, modification):
        ...

class CmpProgressionLevelTooltipView(BaseProgressionLevelTooltipView):
    __slots__: tuple
    def _getModificationType(self, postProgression, step):
        ...

class CfgProgressionLevelTooltipView(CmpProgressionLevelTooltipView):
    __slots__: tuple
    @property
    def viewModel(self):
        ...
    def _getIsUnlocked(self, step):
        ...
