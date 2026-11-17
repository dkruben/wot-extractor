# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/player_subscriptions/wot_subscription_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, IntEnum as IntEnum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel as SubscriptionModel

class WotSubscriptionStateEnum(Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'

class WotTierEnum(Enum):
    NONE = 'None'
    CORE = 'Core'
    PRO = 'Pro'

class WotPlusPeriodicityEnum(IntEnum):
    P6MONTHS = 6
    P12MONTHS = 12

class WotSubscriptionModel(SubscriptionModel):
    __slots__: tuple
    def __init__(self, properties=12, commands=0):
        ...
    def getWotSubscriptionState(self):
        ...
    def setWotSubscriptionState(self, value):
        ...
    def getWotTier(self):
        ...
    def setWotTier(self, value):
        ...
    def getSubscriptionPeriodicity(self):
        ...
    def setSubscriptionPeriodicity(self, value):
        ...
    def getIsButtonHighlighted(self):
        ...
    def setIsButtonHighlighted(self, value):
        ...
    def _initialize(self):
        ...
