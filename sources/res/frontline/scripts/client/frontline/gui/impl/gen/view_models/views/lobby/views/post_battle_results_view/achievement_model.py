# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/post_battle_results_view/achievement_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/post_battle_results_view/achievement_model.py
from frameworks.wulf import ViewModel

class AchievementModel(ViewModel):
    __slots__ = ()
    ACHIEVEMENT_LEFT_BLOCK = 'left'
    ACHIEVEMENT_RIGHT_BLOCK = 'right'
    RANK = 'rank'

    def __init__(self, properties=5, commands=0):
        super(AchievementModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getGroupID(self):
        return self._getString(1)

    def setGroupID(self, value):
        self._setString(1, value)

    def getIconName(self):
        return self._getString(2)

    def setIconName(self, value):
        self._setString(2, value)

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def getTooltipArgs(self):
        return self._getString(4)

    def setTooltipArgs(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(AchievementModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('groupID', '')
        self._addStringProperty('iconName', '')
        self._addStringProperty('tooltipId', '')
        self._addStringProperty('tooltipArgs', '')
