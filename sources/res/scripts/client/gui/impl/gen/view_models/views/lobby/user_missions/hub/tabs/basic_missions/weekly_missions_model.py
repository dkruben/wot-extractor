# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/weekly_missions_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/weekly_missions_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.weekly.weekly_mission_model import WeeklyMissionModel

class WeeklyMissionsModel(ViewModel):
    __slots__ = ('onReroll', )

    def __init__(self, properties=2, commands=1):
        super(WeeklyMissionsModel, self).__init__(properties=properties, commands=commands)

    def getMissionsList(self):
        return self._getArray(0)

    def setMissionsList(self, value):
        self._setArray(0, value)

    @staticmethod
    def getMissionsListType():
        return WeeklyMissionModel

    def getUpdateWeekDay(self):
        return self._getNumber(1)

    def setUpdateWeekDay(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(WeeklyMissionsModel, self)._initialize()
        self._addArrayProperty('missionsList', Array())
        self._addNumberProperty('updateWeekDay', 0)
        self.onReroll = self._addCommand('onReroll')
