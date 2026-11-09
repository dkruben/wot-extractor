# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/secondary_objectives/secondary_objectives.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.pve_base.base.pve_hud_widget import SeveralItemsPveHudWidget as SeveralItemsPveHudWidget
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.settings_model import SecondaryObjectiveServerModel as SecondaryObjectiveServerModel
from gui.Scaleform.daapi.view.battle.pve_base.secondary_objectives.state_machine.machine import SecondaryObjectiveStateMachine as SecondaryObjectiveStateMachine
from gui.Scaleform.daapi.view.meta.PveSecondaryObjectivesMeta import PveSecondaryObjectivesMeta as PveSecondaryObjectivesMeta
from pve_battle_hud import WidgetType as WidgetType, SecondaryObjectiveState as SecondaryObjectiveState

class PveSecondaryObjectives(SeveralItemsPveHudWidget, PveSecondaryObjectivesMeta):
    MAX_ITEMS_COUNT = 3
    def __init__(self):
        ...
    def addObjective(self, serverSettings, clientSettings):
        ...
    def removeObjective(self, objectiveId, hideType):
        ...
    def updateTimer(self, objectiveId, timerValue, isWarning=False):
        ...
    def updateProgress(self, objectiveId, progress):
        ...
    def updateTitle(self, objectiveId, title):
        ...
    def _onPrebattlePeriod(self):
        ...
    def _getStateToRestore(self, serverSettings):
        ...
