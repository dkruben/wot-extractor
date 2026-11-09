# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/subcategory_advanced_achievement_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/subcategory_advanced_achievement_model.py
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel

class SubcategoryAdvancedAchievementModel(AdvancedAchievementModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(SubcategoryAdvancedAchievementModel, self).__init__(properties=properties, commands=commands)

    def getPrevValue(self):
        return self._getNumber(15)

    def setPrevValue(self, value):
        self._setNumber(15, value)

    def getPrevAchievementScore(self):
        return self._getNumber(16)

    def setPrevAchievementScore(self, value):
        self._setNumber(16, value)

    def getBubbles(self):
        return self._getNumber(17)

    def setBubbles(self, value):
        self._setNumber(17, value)

    def _initialize(self):
        super(SubcategoryAdvancedAchievementModel, self)._initialize()
        self._addNumberProperty('prevValue', 0)
        self._addNumberProperty('prevAchievementScore', 0)
        self._addNumberProperty('bubbles', 0)
