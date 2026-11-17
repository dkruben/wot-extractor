# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_setup_selector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class SetupStates(IntEnum):
    NORMAL = 0
    WARNING = 1

class AmmunitionSetupSelector(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getIsSwitchEnabled(self):
        ...
    def setIsSwitchEnabled(self, value):
        ...
    def getIsPrebattleSwitchDisabled(self):
        ...
    def setIsPrebattleSwitchDisabled(self, value):
        ...
    def getStates(self):
        ...
    def setStates(self, value):
        ...
    @staticmethod
    def getStatesType():
        ...
    def _initialize(self):
        ...
