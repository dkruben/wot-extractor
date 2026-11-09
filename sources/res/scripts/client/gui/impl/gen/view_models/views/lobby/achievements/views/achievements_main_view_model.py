# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievements_main_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievements_main_view_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements.advanced_achievements_view_model import AdvancedAchievementsViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.summary_view_model import SummaryViewModel

class AchievementsViews(IntEnum):
    SUMMARY = 0
    ACHIEVEMENTS = 1


class AchievementsMainViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=4, commands=1):
        super(AchievementsMainViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def summaryModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getSummaryModelType():
        return SummaryViewModel

    @property
    def achievementsModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getAchievementsModelType():
        return AdvancedAchievementsViewModel

    def getViewType(self):
        return AchievementsViews(self._getNumber(2))

    def setViewType(self, value):
        self._setNumber(2, value.value)

    def getIsOtherPlayer(self):
        return self._getBool(3)

    def setIsOtherPlayer(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(AchievementsMainViewModel, self)._initialize()
        self._addViewModelProperty('summaryModel', SummaryViewModel())
        self._addViewModelProperty('achievementsModel', AdvancedAchievementsViewModel())
        self._addNumberProperty('viewType', AchievementsViews.SUMMARY.value)
        self._addBoolProperty('isOtherPlayer', False)
        self.onClose = self._addCommand('onClose')
