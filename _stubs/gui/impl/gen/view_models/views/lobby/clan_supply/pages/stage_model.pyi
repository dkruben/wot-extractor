# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/pages/stage_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class StageStatus(IntEnum):
    AVAILABLE = 0
    DISABLED = 1
    OPENED = 2

class StageModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def getIsPremium(self):
        ...
    def setIsPremium(self, value):
        ...
    def _initialize(self):
        ...
