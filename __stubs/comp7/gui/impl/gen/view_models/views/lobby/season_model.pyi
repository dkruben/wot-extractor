# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/season_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from frameworks.wulf import ViewModel as ViewModel

class SeasonState(IntEnum):
    NOTSTARTED = 0
    JUSTSTARTED = 1
    ACTIVE = 2
    ENDSOON = 3
    END = 4
    DISABLED = 5

class SeasonModel(ViewModel):
    __slots__: tuple
    pollServerTime: Any
    def __init__(self, properties=6, commands=1):
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getStartTimestamp(self):
        ...
    def setStartTimestamp(self, value):
        ...
    def getEndTimestamp(self):
        ...
    def setEndTimestamp(self, value):
        ...
    def getServerTimestamp(self):
        ...
    def setServerTimestamp(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getHasTentativeDates(self):
        ...
    def setHasTentativeDates(self, value):
        ...
    def _initialize(self):
        ...
