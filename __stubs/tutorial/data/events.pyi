# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/data/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from tutorial.data.has_id import HasTargetID as HasTargetID
from shared_utils import CONST_CONTAINER as CONST_CONTAINER

class GuiEventType(object):
    CLICK = 1
    CLICK_OUTSIDE = 2
    ESC = 3
    ENABLE = 4
    DISABLE = 5
    ENABLED_CHANGE = 6
    VISIBLE_CHANGE = 7

class _StateNames(CONST_CONTAINER):
    VISIBLE = 'visible'
    ENABLED = 'enabled'

class _Event(HasTargetID):
    __eventType: Any
    def __init__(self, eventType, targetID):
        ...
    def getEventType(self):
        ...
    def getActionCriteria(self):
        ...

class ClickEvent(_Event):
    def __init__(self, targetID):
        ...

class ClickOutsideEvent(_Event):
    def __init__(self, targetID):
        ...

class EscEvent(_Event):
    def __init__(self, targetID):
        ...

class EnableEvent(_Event):
    def __init__(self, targetID):
        ...

class DisableEvent(_Event):
    def __init__(self, targetID):
        ...

class EnabledChangeEvent(_Event):
    __state: Any
    def __init__(self, targetID, state=False):
        ...
    def getStateValue(self):
        ...
    def getStateName(self):
        ...

class VisibleChangeEvent(_Event):
    __state: Any
    def __init__(self, targetID, state=False):
        ...
    def getStateValue(self):
        ...
    def getStateName(self):
        ...
