# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.event_bus import SharedEvent as SharedEvent
from gui.shared.events import NavigationEvent as NavigationEvent

class _BackNavigationEvent(SharedEvent):
    EVENT_ID = 'backNavigationEvent'
    requestingState: Any
    def __init__(self, requestingState=None):
        ...

class _BackNavigationGeneratedNavigationEvent(NavigationEvent):
    shouldKillView: Any
    def __init__(self, targetStateID, params, shouldKillView):
        ...

class _NonViewClosingBackNavigationEvent(_BackNavigationEvent):
    EVENT_ID = 'nonViewClosingBackNavigationEvent'

class _StopEvent(NavigationEvent):
    ...
