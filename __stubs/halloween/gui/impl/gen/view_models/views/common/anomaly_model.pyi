# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/common/anomaly_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class AnomalyType(Enum):
    REGULAR = 'regular'
    EPIC = 'epic'
    INDIVIDUAL = 'individual'
    SECRET = 'secret'

class AnomalyState(Enum):
    UNKNOWN = 'unknown'
    KNOWN = 'known'
    AVAILABLE = 'available'
    ACQUIRED = 'acquired'
    NEW = 'new'

class AnomalyModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
