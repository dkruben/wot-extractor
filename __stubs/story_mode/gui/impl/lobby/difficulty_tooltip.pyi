# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from story_mode.gui.impl.gen.view_models.views.lobby.mission_difficulty_tooltip_model import MissionDifficultyTooltipModel as MissionDifficultyTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class DifficultyTooltip(ViewImpl):
    _difficulty: Any
    _isAutoCompleteCondition: Any
    _isSelected: Any
    _isLocked: Any
    def __init__(self, difficulty, isSelected, isLocked=False, isAutoCompleteCondition=False):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
