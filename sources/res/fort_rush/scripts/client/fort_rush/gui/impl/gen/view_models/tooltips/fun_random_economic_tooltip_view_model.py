# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/tooltips/fun_random_economic_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/tooltips/fun_random_economic_tooltip_view_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.financial_details_model import FinancialDetailsModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTALS = 'crystal'
    XP = 'xp'
    FREE_XP = 'freeXP'
    TANKMEN_XP = 'tankmenXP'


class FunRandomEconomicTooltipViewModel(FinancialDetailsModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomEconomicTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyType(self):
        return CurrencyType(self._getString(4))

    def setCurrencyType(self, value):
        self._setString(4, value.value)

    def getPremiumAdvertising(self):
        return self._getString(5)

    def setPremiumAdvertising(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(FunRandomEconomicTooltipViewModel, self)._initialize()
        self._addStringProperty('currencyType')
        self._addStringProperty('premiumAdvertising', '')
