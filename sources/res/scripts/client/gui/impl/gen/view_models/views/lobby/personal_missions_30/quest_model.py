# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/quest_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/quest_model.py
from frameworks.wulf import ViewModel

class QuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QuestModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getQuestCondition(self):
        return self._getString(1)

    def setQuestCondition(self, value):
        self._setString(1, value)

    def getSummary(self):
        return self._getString(2)

    def setSummary(self, value):
        self._setString(2, value)

    def getQuestType(self):
        return self._getString(3)

    def setQuestType(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(QuestModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('questCondition', '')
        self._addStringProperty('summary', '')
        self._addStringProperty('questType', '')
