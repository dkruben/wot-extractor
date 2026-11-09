# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/widget_quest_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/widget_quest_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.user_missions.common.base_quest_model import BaseQuestModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.bonus_model import BonusModel

class WidgetQuestModel(BaseQuestModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(WidgetQuestModel, self).__init__(properties=properties, commands=commands)

    def getCountdown(self):
        return self._getNumber(10)

    def setCountdown(self, value):
        self._setNumber(10, value)

    def getMissionType(self):
        return self._getString(11)

    def setMissionType(self, value):
        self._setString(11, value)

    def getBonuses(self):
        return self._getArray(12)

    def setBonuses(self, value):
        self._setArray(12, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getCommonConditionId(self):
        return self._getNumber(13)

    def setCommonConditionId(self, value):
        self._setNumber(13, value)

    def getSpecialConditionIds(self):
        return self._getArray(14)

    def setSpecialConditionIds(self, value):
        self._setArray(14, value)

    @staticmethod
    def getSpecialConditionIdsType():
        return int

    def _initialize(self):
        super(WidgetQuestModel, self)._initialize()
        self._addNumberProperty('countdown', 0)
        self._addStringProperty('missionType', '')
        self._addArrayProperty('bonuses', Array())
        self._addNumberProperty('commonConditionId', 0)
        self._addArrayProperty('specialConditionIds', Array())
