# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/param_value_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class MechanicState(Enum):
    DEFAULT = ''
    ON = 'on'
    OFF = 'off'

class ParamValueModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getMechanic(self):
        ...
    def setMechanic(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
