# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievement_section_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievement_section_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.achievement_model import AchievementModel

class AchievementSectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AchievementSectionModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getAchievements(self):
        return self._getArray(1)

    def setAchievements(self, value):
        self._setArray(1, value)

    @staticmethod
    def getAchievementsType():
        return AchievementModel

    def _initialize(self):
        super(AchievementSectionModel, self)._initialize()
        self._addStringProperty('type', 'epic')
        self._addArrayProperty('achievements', Array())
