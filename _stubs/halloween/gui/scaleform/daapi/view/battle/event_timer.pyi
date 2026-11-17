# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/event_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
import typing as typing
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from gui.Scaleform.daapi.view.meta.EventTimerMeta import EventTimerMeta as EventTimerMeta
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional

class _AlarmTime(IntEnum):
    FIRST = 60
    SECOND = 30
    LAST = 10

class _AlertState(IntEnum):
    DISABLED = 0
    ENABLED = 1

class EventTimer(EventTimerMeta):
    sessionProvider: Any
    _COLOR = '#ffffff'
    _HTML_TEMPLATE_PATH = 'html_templates:battleTimer'
    _ALERT_STATE_ENABLED = 1
    _ALERT_STATE_DISABLED = 0
    _ONE_MINUTE_SECONDS = 60
    _visible: Any
    _timerState: Any
    def __init__(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onChangeAnomaliesViewVisibility(self, _):
        ...
    def _onTimerUpdated(self, seconds, prev, lastPhase):
        ...
    def _refreshTimerState(self):
        ...
    def _hideTimer(self):
        ...
