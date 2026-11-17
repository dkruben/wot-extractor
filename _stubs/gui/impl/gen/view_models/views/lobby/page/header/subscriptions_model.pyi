# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/subscriptions_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.premium_account_subscription_model import PremiumAccountSubscriptionModel as PremiumAccountSubscriptionModel
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusSubscriptionModel as WotPlusSubscriptionModel

class SubscriptionsModel(ViewModel):
    __slots__: tuple
    onOpenPremium: Any
    onOpenWotPlus: Any
    def __init__(self, properties=3, commands=2):
        ...
    @property
    def wotPlus(self):
        ...
    @staticmethod
    def getWotPlusType():
        ...
    @property
    def premiumAccount(self):
        ...
    @staticmethod
    def getPremiumAccountType():
        ...
    def getIsCnRealm(self):
        ...
    def setIsCnRealm(self, value):
        ...
    def _initialize(self):
        ...
