# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/comparison_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel

class ComparisonModel(ViewModel):
    __slots__: tuple
    ENABLED = 'enabled'
    DISABLED_FULL_BASKET = 'disabledFullBasket'
    DISABLED_ON_SERVER = 'disabledOnServer'
    CAN_NOT_COMPARE = 'canNotCompare'
    onAddToComparison: Any
    def __init__(self, properties=1, commands=1):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def _initialize(self):
        ...
