# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/daily_missions_section_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/daily_missions_section_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.block_status_model import BlockStatusModel

class DailyMissionsSectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DailyMissionsSectionModel, self).__init__(properties=properties, commands=commands)

    @property
    def dailyMissionsBlockStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getDailyMissionsBlockStatusType():
        return BlockStatusModel

    @property
    def premiumDailyMissionsBlockStatus(self):
        return self._getViewModel(1)

    @staticmethod
    def getPremiumDailyMissionsBlockStatusType():
        return BlockStatusModel

    @property
    def rewardProgressBlockStatus(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardProgressBlockStatusType():
        return BlockStatusModel

    def getTargetQuestId(self):
        return self._getString(3)

    def setTargetQuestId(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(DailyMissionsSectionModel, self)._initialize()
        self._addViewModelProperty('dailyMissionsBlockStatus', BlockStatusModel())
        self._addViewModelProperty('premiumDailyMissionsBlockStatus', BlockStatusModel())
        self._addViewModelProperty('rewardProgressBlockStatus', BlockStatusModel())
        self._addStringProperty('targetQuestId', '')
