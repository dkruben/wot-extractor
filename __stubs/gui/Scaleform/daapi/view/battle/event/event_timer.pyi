# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/event_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.meta.EventTimerMeta import EventTimerMeta as EventTimerMeta

class EventTimer(EventTimerMeta):
    _COLOR = '#ffffff'
    _MESSAGE = 'timerEventMessage'
    _HTML_TEMPLATE_PATH = 'html_templates:battleTimer'
    _WAIT_TIME = 300
    _ALARM_TIME = 60
    _ALART_STATE_ENABLED = 1
    _ALART_STATE_DISABLED = 0
    _MAX_PROGRESS = 100
    _TITLE_TMPL = '<font color="{color}">{text}</font>'
    _TIMER_TMPL = '<font color="{color}">{min:02d}:{sec:02d}</font>'
    _waitTime: Any
    _alarmTime: Any
    _visible: Any
    _progress: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onUpdateScenarioTimer(self, waitTime, alarmTime, visible):
        ...
    def _updateTimer(self):
        ...
    def _playFxS(self):
        ...
    def _hideTimer(self):
        ...
    def setProgress(self, progress):
        ...
