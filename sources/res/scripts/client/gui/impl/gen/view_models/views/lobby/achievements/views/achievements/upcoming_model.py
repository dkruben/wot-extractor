# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievements/upcoming_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievements/upcoming_model.py
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel

class UpcomingModel(AdvancedAchievementModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(UpcomingModel, self).__init__(properties=properties, commands=commands)

    def getSpecificItemName(self):
        return self._getString(15)

    def setSpecificItemName(self, value):
        self._setString(15, value)

    def getSpecificItemLevel(self):
        return self._getNumber(16)

    def setSpecificItemLevel(self, value):
        self._setNumber(16, value)

    def getIsResearchable(self):
        return self._getBool(17)

    def setIsResearchable(self, value):
        self._setBool(17, value)

    def _initialize(self):
        super(UpcomingModel, self)._initialize()
        self._addStringProperty('specificItemName', '')
        self._addNumberProperty('specificItemLevel', 0)
        self._addBoolProperty('isResearchable', False)
