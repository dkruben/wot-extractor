# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/premium_plus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/premium_plus_model.py
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel

class PremiumPlusModel(AdditionalBonusModel):
    __slots__ = ('onNextBonusTimeUpdate', )

    def __init__(self, properties=18, commands=4):
        super(PremiumPlusModel, self).__init__(properties=properties, commands=commands)

    def getIsUndefinedLeftBonusCount(self):
        return self._getBool(16)

    def setIsUndefinedLeftBonusCount(self, value):
        self._setBool(16, value)

    def getNextBonusTime(self):
        return self._getReal(17)

    def setNextBonusTime(self, value):
        self._setReal(17, value)

    def _initialize(self):
        super(PremiumPlusModel, self)._initialize()
        self._addBoolProperty('isUndefinedLeftBonusCount', False)
        self._addRealProperty('nextBonusTime', -1)
        self.onNextBonusTimeUpdate = self._addCommand('onNextBonusTimeUpdate')
