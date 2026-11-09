# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/battle_result_stat_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional, Tuple as Tuple
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from story_mode.gui.impl.gen.view_models.views.lobby.battle_result_stat_tooltip_model import BattleResultStatTooltipModel as BattleResultStatTooltipModel, StatEnum as StatEnum, DetailedStatModel as DetailedStatModel
from gui.impl.pub import ViewImpl as ViewImpl

class BattleResultStatTooltip(ViewImpl):
    __slots__: tuple
    __stat: Any
    __detailedStats: Any
    __infoList: Any
    def __init__(self, stat, detailedStats, infoList):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillViewModel(self, vm):
        ...
