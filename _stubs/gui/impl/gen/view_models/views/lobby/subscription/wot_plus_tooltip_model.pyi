# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/subscription/wot_plus_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel

class SubscriptionState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELED = 2

class WotPlusTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getNextCharge(self):
        ...
    def setNextCharge(self, value):
        ...
    def getExpirationDate(self):
        ...
    def setExpirationDate(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getBonuses(self):
        ...
    def setBonuses(self, value):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def _initialize(self):
        ...
