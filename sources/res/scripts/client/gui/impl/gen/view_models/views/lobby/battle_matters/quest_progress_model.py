# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/quest_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/quest_progress_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.intermediate_quest_model import IntermediateQuestModel

class QuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(QuestProgressModel, self).__init__(properties=properties, commands=commands)

    def getCountCompleted(self):
        return self._getNumber(0)

    def setCountCompleted(self, value):
        self._setNumber(0, value)

    def getTotalQuests(self):
        return self._getNumber(1)

    def setTotalQuests(self, value):
        self._setNumber(1, value)

    def getLastSeenProgress(self):
        return self._getNumber(2)

    def setLastSeenProgress(self, value):
        self._setNumber(2, value)

    def getMainRewardReceived(self):
        return self._getBool(3)

    def setMainRewardReceived(self, value):
        self._setBool(3, value)

    def getIntermediateQuests(self):
        return self._getArray(4)

    def setIntermediateQuests(self, value):
        self._setArray(4, value)

    @staticmethod
    def getIntermediateQuestsType():
        return IntermediateQuestModel

    def _initialize(self):
        super(QuestProgressModel, self)._initialize()
        self._addNumberProperty('countCompleted', 0)
        self._addNumberProperty('totalQuests', 0)
        self._addNumberProperty('lastSeenProgress', 0)
        self._addBoolProperty('mainRewardReceived', False)
        self._addArrayProperty('intermediateQuests', Array())
