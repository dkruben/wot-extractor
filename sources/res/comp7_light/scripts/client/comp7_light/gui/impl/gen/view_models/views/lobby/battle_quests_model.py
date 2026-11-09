# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/battle_quests_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/battle_quests_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class BattleQuestsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleQuestsModel, self).__init__(properties=properties, commands=commands)

    def getTasksBattle(self):
        return self._getArray(0)

    def setTasksBattle(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTasksBattleType():
        return QuestModel

    def getCurrentTimerDate(self):
        return self._getNumber(1)

    def setCurrentTimerDate(self, value):
        self._setNumber(1, value)

    def getMissionsCompletedVisited(self):
        return self._getArray(2)

    def setMissionsCompletedVisited(self, value):
        self._setArray(2, value)

    def _initialize(self):
        super(BattleQuestsModel, self)._initialize()
        self._addArrayProperty('tasksBattle', Array())
        self._addNumberProperty('currentTimerDate', 0)
        self._addArrayProperty('missionsCompletedVisited', Array())
