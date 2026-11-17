# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/shared/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import unique as unique, IntEnum as IntEnum
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import HasCtxEvent as HasCtxEvent
from gui.shared.event_bus import SharedEvent as SharedEvent

class EventBridge(object):
    __slots__: tuple
    __event: Any
    __scope: Any
    def __init__(self, event, scope=...):
        ...
    def __call__(self, *_, **__):
        ...

class FunSelectionEvent(SharedEvent):
    selectedSubModeID: Any
    def __init__(self, selectedSubModeID):
        ...

class FunSubModesEvent(HasCtxEvent):
    subModes: Any
    def __init__(self, eventType, subModes, ctx=None):
        ...

# decorador original: @unique
class FunEventScope(IntEnum):
    DEFAULT = 1
    DESIRABLE = 2

# decorador original: @unique
class FunEventType(IntEnum):
    SUB_SETTINGS = 1
    SUB_SELECTION = 2
    SUB_STATUS_UPDATE = 3
    SUB_STATUS_TICK = 4
    PROGRESSION_UPDATE = 5
    PROGRESSION_TICK = 6
