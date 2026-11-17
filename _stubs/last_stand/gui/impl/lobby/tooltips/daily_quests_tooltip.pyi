# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/daily_quests_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, time_utils as time_utils
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.daily_tooltip_view_model import DailyTooltipViewModel as DailyTooltipViewModel
from last_stand.gui.impl.lobby.ls_helpers import fillRewardsForTooltips as fillRewardsForTooltips, getQuestFinishTimeLeft as getQuestFinishTimeLeft
from last_stand.skeletons.ls_controller import ILSController as ILSController

class DailyQuestsTooltip(ViewImpl):
    lsCtrl: Any
    _MAX_BONUSES_IN_VIEW = 10
    __quest: Any
    __allDailyCompleted: Any
    def __init__(self, quest, completedAllDaily):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
