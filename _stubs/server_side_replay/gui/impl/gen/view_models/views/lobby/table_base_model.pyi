# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/table_base_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.replay_model import ReplayModel as ReplayModel

class StatParams(Enum):
    EARNEDXP = 'earnedXp'
    DAMAGEDEALT = 'damageDealt'
    DAMAGEASSISTED = 'damageAssisted'
    DAMAGEBLOCKEDBYARMOR = 'damageBlockedByArmor'
    KILLS = 'kills'
    MARKSOFMASTERY = 'marksOfMastery'
    DATE = 'date'

class State(IntEnum):
    INITIAL = 0
    SUCCESS = 1
    ERROR = 2

class TableBaseModel(ViewModel):
    __slots__: tuple
    DEFAULT_REPLAY_INDEX = -1
    onResetFilter: Any
    onSort: Any
    onRefresh: Any
    onWatch: Any
    def __init__(self, properties=7, commands=4):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsLoading(self):
        ...
    def setIsLoading(self, value):
        ...
    def getIsPopoverEnabled(self):
        ...
    def setIsPopoverEnabled(self, value):
        ...
    def getIsPopoverHighlighted(self):
        ...
    def setIsPopoverHighlighted(self, value):
        ...
    def getSelectedSorting(self):
        ...
    def setSelectedSorting(self, value):
        ...
    def getItems(self):
        ...
    def setItems(self, value):
        ...
    @staticmethod
    def getItemsType():
        ...
    def getInitialReplayIndex(self):
        ...
    def setInitialReplayIndex(self, value):
        ...
    def _initialize(self):
        ...
