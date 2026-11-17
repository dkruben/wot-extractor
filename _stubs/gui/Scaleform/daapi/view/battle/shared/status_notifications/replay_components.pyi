# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/status_notifications/replay_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
from ReplayEvents import g_replayEvents as g_replayEvents
from gui.Scaleform.daapi.view.battle.shared.status_notifications.components import StatusNotificationContainer as StatusNotificationContainer, StatusNotificationsGroup as StatusNotificationsGroup
from gui.Scaleform.daapi.view.battle.shared.status_notifications.sn_items import TimerSN as TimerSN, TimeSnapshotHandler as TimeSnapshotHandler
from gui.Scaleform.daapi.view.battle.shared.timers_common import PrecisePythonTimer as PrecisePythonTimer
_logger: Any

class CallbackPrecisePythonTimer(object):
    tickCallback: Any
    endCallback: Any
    def __init__(self, tickCallback, endCallback):
        ...
    def destroy(self):
        ...

class CallbackTruePythonTimer(PrecisePythonTimer):
    __slots__: tuple
    __timeLeft: Any
    def __init__(self, viewObject, typeID, viewID, totalTime, finishTime, startTime=None, interval=1.0, secondInRow=False, **kwargs):
        ...
    def clear(self):
        ...
    def _hideView(self):
        ...
    def getTimeLeft(self):
        ...
    def _setViewSnapshot(self, timeLeft):
        ...
    def _showView(self, isBubble):
        ...

class _ReplaySnapshotHandler(TimeSnapshotHandler):
    __ticker: Any
    __finishTime: Any
    __totalTime: Any
    def __init__(self, updateHandler):
        ...
    def destroy(self):
        ...
    def setTimeParams(self, totalTime, finishTime):
        ...
    def __onReplayPaused(self, _):
        ...
    def __restartTicker(self):
        ...
    def __onTickerTick(self, timeLeft):
        ...
    def __onTickerFinished(self):
        ...
    def __destroyTicker(self):
        ...

class ReplayStatusNotificationContainer(StatusNotificationContainer):
    def __init__(self, items, updateCallback):
        ...
