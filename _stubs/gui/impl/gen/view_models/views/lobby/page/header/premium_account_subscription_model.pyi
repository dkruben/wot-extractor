# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/premium_account_subscription_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class PremiumTypeEnum(Enum):
    NONE = 'None'
    BASIC = 'Basic'
    PLUS = 'Plus'
    VIP = 'VIP'

class PremiumStateEnum(Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'

class PremiumAccountSubscriptionModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getExpiryTime(self):
        ...
    def setExpiryTime(self, value):
        ...
    def _initialize(self):
        ...
