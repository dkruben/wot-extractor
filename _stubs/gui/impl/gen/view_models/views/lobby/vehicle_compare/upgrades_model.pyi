# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/upgrades_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class UpgradesState(Enum):
    ZERO_UPGRADES = 'zeroUpgrades'
    PARTIAL_UPGRADES = 'partialUpgrades'
    FULL_UPGRADES = 'fullUpgrades'

class UpgradesModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsSelected(self):
        ...
    def setIsSelected(self, value):
        ...
    def _initialize(self):
        ...
