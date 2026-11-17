# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/daily_reroll_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.daily_reroll_tooltip_model import DailyRerollTooltipModel as DailyRerollTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class DailyRerollTooltip(ViewImpl):
    __slots__: tuple
    _timeLeft: Any
    _rerollInterval: Any
    def __init__(self, timeLeft, rerollInterval):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
