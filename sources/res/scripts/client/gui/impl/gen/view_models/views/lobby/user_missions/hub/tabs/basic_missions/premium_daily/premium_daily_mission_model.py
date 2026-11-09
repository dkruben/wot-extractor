# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/premium_daily/premium_daily_mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/premium_daily/premium_daily_mission_model.py
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.common.mission_base_model import MissionBaseModel

class PremiumDailyMissionModel(MissionBaseModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(PremiumDailyMissionModel, self).__init__(properties=properties, commands=commands)

    def getIsLocked(self):
        return self._getBool(11)

    def setIsLocked(self, value):
        self._setBool(11, value)

    def _initialize(self):
        super(PremiumDailyMissionModel, self)._initialize()
        self._addBoolProperty('isLocked', False)
