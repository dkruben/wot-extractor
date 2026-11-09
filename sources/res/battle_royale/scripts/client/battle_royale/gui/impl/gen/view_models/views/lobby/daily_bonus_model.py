# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/daily_bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/daily_bonus_model.py
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType
from frameworks.wulf import ViewModel

class DailyBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DailyBonusModel, self).__init__(properties=properties, commands=commands)

    def getHasDailyBonus(self):
        return self._getBool(0)

    def setHasDailyBonus(self, value):
        self._setBool(0, value)

    def getDailyBonusFactor(self):
        return self._getNumber(1)

    def setDailyBonusFactor(self, value):
        self._setNumber(1, value)

    def getSoloTopPlaces(self):
        return self._getNumber(2)

    def setSoloTopPlaces(self, value):
        self._setNumber(2, value)

    def getSquadTopPlaces(self):
        return self._getNumber(3)

    def setSquadTopPlaces(self, value):
        self._setNumber(3, value)

    def getCoinType(self):
        return CoinType(self._getString(4))

    def setCoinType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(DailyBonusModel, self)._initialize()
        self._addBoolProperty('hasDailyBonus', False)
        self._addNumberProperty('dailyBonusFactor', 0)
        self._addNumberProperty('soloTopPlaces', 0)
        self._addNumberProperty('squadTopPlaces', 0)
        self._addStringProperty('coinType')
