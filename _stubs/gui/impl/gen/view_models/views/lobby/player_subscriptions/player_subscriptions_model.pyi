# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/player_subscriptions/player_subscriptions_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription import Subscription as Subscription

class PlayerSubscriptionsModel(ViewModel):
    __slots__: tuple
    onBack: Any
    onCardClick: Any
    onButtonClick: Any
    def __init__(self, properties=2, commands=3):
        ...
    def getSubscriptions(self):
        ...
    def setSubscriptions(self, value):
        ...
    @staticmethod
    def getSubscriptionsType():
        ...
    def getWarningTitle(self):
        ...
    def setWarningTitle(self, value):
        ...
    def _initialize(self):
        ...
