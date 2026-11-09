# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/curtain/curtain_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R

class CurtainStateEnum(IntEnum):
    CLOSED = 0
    OPENING = 1
    OPENED = 2
    CLOSING = 3
    HIDING = 4
    HIDDEN = 5
    REVEALING = 6

class CurtainViewModel(ViewModel):
    __slots__: tuple
    onMoveSpace: Any
    onStateTransitionComplete: Any
    def __init__(self, properties=4, commands=2):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsWaiting(self):
        ...
    def setIsWaiting(self, value):
        ...
    def getWaitingText(self):
        ...
    def setWaitingText(self, value):
        ...
    def getCurrentSubViewID(self):
        ...
    def setCurrentSubViewID(self, value):
        ...
    def _initialize(self):
        ...
