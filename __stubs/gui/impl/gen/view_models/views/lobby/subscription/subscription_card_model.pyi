# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/subscription/subscription_card_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class SubscriptionCardState(Enum):
    AVAILABLE = 'available'
    ACTIVE = 'active'
    DISABLE = 'disable'

class SubscriptionCardModel(ViewModel):
    __slots__: tuple
    onCardClick: Any
    onInfoButtonClik: Any
    def __init__(self, properties=2, commands=2):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getNextCharge(self):
        ...
    def setNextCharge(self, value):
        ...
    def _initialize(self):
        ...
