# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/battle_results/comp7_weekly_quest_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/battle_results/comp7_weekly_quest_progress_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class Comp7WeeklyQuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(Comp7WeeklyQuestProgressModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)

    def getTotalProgress(self):
        return self._getNumber(3)

    def setTotalProgress(self, value):
        self._setNumber(3, value)

    def getEarned(self):
        return self._getNumber(4)

    def setEarned(self, value):
        self._setNumber(4, value)

    def getIconKey(self):
        return self._getString(5)

    def setIconKey(self, value):
        self._setString(5, value)

    def getDescription(self):
        return self._getString(6)

    def setDescription(self, value):
        self._setString(6, value)

    def getBonuses(self):
        return self._getArray(7)

    def setBonuses(self, value):
        self._setArray(7, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(Comp7WeeklyQuestProgressModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addBoolProperty('isCompleted', False)
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('totalProgress', 0)
        self._addNumberProperty('earned', 0)
        self._addStringProperty('iconKey', '')
        self._addStringProperty('description', '')
        self._addArrayProperty('bonuses', Array())
