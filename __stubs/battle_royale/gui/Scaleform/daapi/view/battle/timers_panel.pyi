# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/timers_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import math as math
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.meta.BattleRoyaleTimersPanelMeta import BattleRoyaleTimersPanelMeta as BattleRoyaleTimersPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.shared.timers_common import TimerComponent as TimerComponent, PythonTimer as PythonTimer
from battle_royale.gui.shared.events import AirDropEvent as AirDropEvent

class _AsTimer(TimerComponent):
    _viewFunc: Any
    def __init__(self, panel, totalTime, viewFunc):
        ...
    def _startTick(self):
        ...
    def _stopTick(self):
        ...
    def _hideView(self):
        ...
    def _showView(self, isBubble):
        ...

class _ReplayTimer(PythonTimer):
    _viewFunc: Any
    def __init__(self, panel, totalTime, viewFunc):
        ...
    def _hideView(self):
        ...
    def _showView(self, isBubble):
        ...
    def _setViewSnapshot(self, timeLeft):
        ...

class TimersPanelPanel(BattleRoyaleTimersPanelMeta, IAbstractPeriodView):
    __sessionProvider: Any
    __timerCreator: Any
    _respawnPeriod: Any
    _airDroptimer: Any
    _respawnTimer: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def setPeriod(self, period):
        ...
    def __onAirDropLootSpawned(self, event):
        ...

def _setRespawnTime(panel, timeLeft):
    ...
def _setAirDropTime(panel, timeLeft):
    ...
