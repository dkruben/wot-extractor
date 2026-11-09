# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/tooltips/fun_random_economic_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.battle_results.financial_details_model import FinancialDetailsModel as FinancialDetailsModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTALS = 'crystal'
    XP = 'xp'
    FREE_XP = 'freeXP'
    TANKMEN_XP = 'tankmenXP'

class FunRandomEconomicTooltipViewModel(FinancialDetailsModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    def getCurrencyType(self):
        ...
    def setCurrencyType(self, value):
        ...
    def getPremiumAdvertising(self):
        ...
    def setPremiumAdvertising(self, value):
        ...
    def _initialize(self):
        ...
