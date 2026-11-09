# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/tooltip/seniority_awards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_tooltip_model import SeniorityAwardsTooltipModel as SeniorityAwardsTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController

class SeniorityAwardsTooltip(ViewImpl):
    __slots__: tuple
    __seniorityAwardsCtrl: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, category, maxCategory, years):
        ...
