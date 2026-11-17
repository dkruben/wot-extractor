# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/primary_objective/primary_objective.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.pve_base.base.pve_hud_widget import SingleItemPveHudWidget as SingleItemPveHudWidget
from gui.Scaleform.daapi.view.battle.pve_base.primary_objective.settings_model import PrimaryObjectiveServerModel as PrimaryObjectiveServerModel
from gui.Scaleform.daapi.view.battle.pve_base.primary_objective.state_machine.states import TimerState as TimerState
from gui.Scaleform.daapi.view.battle.pve_base.primary_objective.state_machine.machine import PrimaryObjectiveStateMachine as PrimaryObjectiveStateMachine
from gui.Scaleform.daapi.view.meta.PvePrimaryObjectiveMeta import PvePrimaryObjectiveMeta as PvePrimaryObjectiveMeta
from pve_battle_hud import WidgetType as WidgetType, PrimaryObjectiveState as PrimaryObjectiveState, getPveHudLogger as getPveHudLogger
_logger: Any

class PvePrimaryObjective(SingleItemPveHudWidget, PvePrimaryObjectiveMeta):
    def __init__(self):
        ...
    def setTimerState(self, timer, state):
        ...
    def updateTimer(self, timerValue):
        ...
    def updateHeaderWithSubheader(self, header, subheader):
        ...
    def updateSubheader(self, subheader):
        ...
    def updateProgress(self, progresses=None, isVisible=True):
        ...
    def showMessage(self, isBackgroundVisible, icon, text):
        ...
    def hideMessage(self):
        ...
    def hideObjective(self):
        ...
    def _onPrebattlePeriod(self):
        ...
    def _getStateToRestore(self, serverSettings):
        ...
    @staticmethod
    def _createVo(header='', objective='', title=''):
        ...
