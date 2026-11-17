# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_base_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel as BonusesModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_grid_model import PostProgressionGridModel as PostProgressionGridModel

class ProgressionAvailability(Enum):
    AVAILABLE = 'available'
    UNAVAILABLEELITE = 'unavailableElite'
    UNAVAILABLEPURCHASE = 'unavailablePurchase'
    UNAVAILABLERENT = 'unavailableRent'
    UNAVAILABLERENTOVER = 'unavailableRentOver'
    UNAVAILABLEBATTLE = 'unavailableBattle'
    UNAVAILABLEFORMATION = 'unavailableFormation'
    UNAVAILABLEBREAKER = 'unavailableBreaker'
    UNAVAILABLEBROKEN = 'unavailableBroken'

class ProgressionState(Enum):
    INITIAL = 'initial'
    TRANSITIONAL = 'transitional'
    FINAL = 'final'

class PostProgressionBaseViewModel(ViewModel):
    __slots__: tuple
    onViewRendered: Any
    def __init__(self, properties=5, commands=1):
        ...
    @property
    def grid(self):
        ...
    @staticmethod
    def getGridType():
        ...
    @property
    def persistentBonuses(self):
        ...
    @staticmethod
    def getPersistentBonusesType():
        ...
    def getProgressionAvailability(self):
        ...
    def setProgressionAvailability(self, value):
        ...
    def getProgressionState(self):
        ...
    def setProgressionState(self, value):
        ...
    def getVehicleRole(self):
        ...
    def setVehicleRole(self, value):
        ...
    def _initialize(self):
        ...
