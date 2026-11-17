# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/event_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from gui.Scaleform.daapi.view.meta.EventTimerMeta import EventTimerMeta as EventTimerMeta
from helpers import dependency as dependency
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

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
    _currentHint: Any
    def __init__(self):
        ...
    @property
    def lsBattleGuiCtrl(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onTimerUpdated(self, seconds, prev, lastPhase, isTimerAlarmEnabled):
        ...
    def _hideTimer(self):
        ...
