# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/empty_skill_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.empty_skill_tooltip_view_model import EmptySkillTooltipViewModel as EmptySkillTooltipViewModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setSkillProgressionModel as setSkillProgressionModel
from gui.impl.pub import ViewImpl as ViewImpl

class EmptySkillTooltip(ViewImpl):
    __slots__: tuple
    _tankman: Any
    _skillIndex: Any
    def __init__(self, tankman, skillIndex):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self):
        ...
