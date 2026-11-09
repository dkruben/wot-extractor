# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/header_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ModeStatus(Enum):
    ALERT = 'alert'
    BATTLESELECTOR = 'battleSelector'

class HeaderModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=1, commands=0):
        ...
    def getModeStatus(self):
        ...
    def setModeStatus(self, value):
        ...
    def _initialize(self):
        ...
