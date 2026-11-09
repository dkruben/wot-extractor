# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/premacc/squad_bonus_tooltip_content_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/squad_bonus_tooltip_content_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class SquadBonusTooltipType(Enum):
    COMMON = 'common'
    SIMPLE = 'simple'
    SIMPLEWITHBONUS = 'simpleWithBonus'


class SquadBonusTooltipContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SquadBonusTooltipContentModel, self).__init__(properties=properties, commands=commands)

    def getCreditsBonusWithPremium(self):
        return self._getNumber(0)

    def setCreditsBonusWithPremium(self, value):
        self._setNumber(0, value)

    def getCreditsBonusWithoutPremium(self):
        return self._getNumber(1)

    def setCreditsBonusWithoutPremium(self, value):
        self._setNumber(1, value)

    def getExperienceBonus(self):
        return self._getNumber(2)

    def setExperienceBonus(self, value):
        self._setNumber(2, value)

    def getBattleType(self):
        return self._getString(3)

    def setBattleType(self, value):
        self._setString(3, value)

    def getType(self):
        return SquadBonusTooltipType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(SquadBonusTooltipContentModel, self)._initialize()
        self._addNumberProperty('creditsBonusWithPremium', 0)
        self._addNumberProperty('creditsBonusWithoutPremium', 0)
        self._addNumberProperty('experienceBonus', 0)
        self._addStringProperty('battleType', '')
        self._addStringProperty('type')
