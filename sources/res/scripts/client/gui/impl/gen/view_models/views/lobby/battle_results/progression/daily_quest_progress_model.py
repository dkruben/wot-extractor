# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/daily_quest_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/daily_quest_progress_model.py
from enum import Enum
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class DailyQuestTypes(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    BONUS = 'bonus'
    PREMIUM = 'premium'
    EPIC = 'epic'


class DailyQuestProgressModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(DailyQuestProgressModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return DailyQuestTypes(self._getString(12))

    def setLevel(self, value):
        self._setString(12, value.value)

    def getNavigationEnabled(self):
        return self._getBool(13)

    def setNavigationEnabled(self, value):
        self._setBool(13, value)

    def _initialize(self):
        super(DailyQuestProgressModel, self)._initialize()
        self._addStringProperty('level')
        self._addBoolProperty('navigationEnabled', False)
