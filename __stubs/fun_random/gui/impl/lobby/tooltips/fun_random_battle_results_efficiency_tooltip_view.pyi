# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_battle_results_efficiency_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel as EfficiencyTooltipModel
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService

class PersonalEfficiencyParamTooltip(ViewImpl):
    __battleResults: Any
    __efficiencyParam: Any
    __arenaUniqueID: Any
    __packer: Any
    def __init__(self, arenaUniqueID, paramType, packer):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __invalidateAll(self):
        ...
