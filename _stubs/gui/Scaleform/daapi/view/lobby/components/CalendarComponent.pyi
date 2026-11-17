# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/components/CalendarComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event, EventManager as EventManager
from gui.Scaleform.daapi.view.meta.CalendarMeta import CalendarMeta as CalendarMeta
from gui.impl import backport as backport

class CalendarComponent(CalendarMeta):
    __em: Any
    onMonthChangedEvent: Any
    onDateSelectedEvent: Any
    def __init__(self):
        ...
    def onMonthChanged(self, rawDate):
        ...
    def onDateSelected(self, rawDate):
        ...
    def formatYMHeader(self, rawDate):
        ...
    def _dispose(self):
        ...
