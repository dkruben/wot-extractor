# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_reward_award_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel

class ShopOnOpenState(Enum):
    AVAILABLE = 'available'
    NOT_AVAILABLE = 'notAvailable'
    DISABLED = 'disabled'

class SeniorityRewardAwardViewModel(ViewModel):
    __slots__: tuple
    onOpenBtnClick: Any
    onShopBtnClick: Any
    def __init__(self, properties=5, commands=2):
        ...
    def getCategory(self):
        ...
    def setCategory(self, value):
        ...
    def getMaxCategory(self):
        ...
    def setMaxCategory(self, value):
        ...
    def getBonuses(self):
        ...
    def setBonuses(self, value):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def getSpecialCurrencyCount(self):
        ...
    def setSpecialCurrencyCount(self, value):
        ...
    def getShopOnOpenState(self):
        ...
    def setShopOnOpenState(self, value):
        ...
    def _initialize(self):
        ...
