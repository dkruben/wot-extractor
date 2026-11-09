# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/team_health_bar_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from builtins import range as range
from past.utils import old_div as old_div
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class ITeamHealthBarListener(object):
    def updateTeamHealthPercent(self, allyPercentage, enemyPercentage):
        ...

class TeamHealthBarController(ViewComponentsController):
    __arenaVisitor: Any
    __arenaDP: Any
    __latestHealthBarData: Any
    __loadingFinished: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, *components):
        ...
    def __handleBattleLoading(self, event):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def __onTeamHealthPercentUpdate(self, percentages):
        ...
