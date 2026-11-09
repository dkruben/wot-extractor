# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/pet_system/promotion_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class PromoBonus(Enum):
    BONDS = 'bonds'
    COMBAT = 'combat'
    CREDITS = 'credits'
    CREW = 'crew'
    EVENTS = 'events'
    SHOWOFF = 'showoff'

class PromotionModel(ViewModel):
    __slots__: tuple
    onChallengeSelect: Any
    onPurchaseSelect: Any
    def __init__(self, properties=4, commands=2):
        ...
    def getIsPromotionEnabled(self):
        ...
    def setIsPromotionEnabled(self, value):
        ...
    def getPromotionBonuses(self):
        ...
    def setPromotionBonuses(self, value):
        ...
    @staticmethod
    def getPromotionBonusesType():
        ...
    def getIsChallengeButtonEnabled(self):
        ...
    def setIsChallengeButtonEnabled(self, value):
        ...
    def getIsPurchaseButtonEnabled(self):
        ...
    def setIsPurchaseButtonEnabled(self, value):
        ...
    def _initialize(self):
        ...
