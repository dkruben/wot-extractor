# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/tooltips/all_quests_done_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.tooltips.all_quests_done_tooltip_model import AllQuestsDoneTooltipModel as AllQuestsDoneTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel

class AllQuestsDoneTooltip(ViewImpl):
    __questTimerLeft: Any
    def __init__(self, layoutID=..., questTimerLeft=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
