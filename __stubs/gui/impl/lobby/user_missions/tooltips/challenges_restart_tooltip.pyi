# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_restart_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.challenges_restart_tooltip_model import ChallengesRestartTooltipModel as ChallengesRestartTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from shared_utils import first as first

class ChallengesRestartTooltip(ViewImpl):
    __challenge: Any
    def __init__(self, challenge):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
