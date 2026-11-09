# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/progression/mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/progression/mission_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class MissionModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(MissionModel, self).__init__(properties=properties, commands=commands)

    def getBonuses(self):
        return self._getArray(12)

    def setBonuses(self, value):
        self._setArray(12, value)

    @staticmethod
    def getBonusesType():
        return TokenBonusModel

    def _initialize(self):
        super(MissionModel, self)._initialize()
        self._addArrayProperty('bonuses', Array())
