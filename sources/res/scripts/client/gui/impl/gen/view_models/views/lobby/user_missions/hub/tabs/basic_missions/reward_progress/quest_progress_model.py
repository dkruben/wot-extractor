# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/reward_progress/quest_progress_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/reward_progress/quest_progress_model.py
from frameworks.wulf import ViewModel

class QuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QuestProgressModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getCurrent(self):
        return self._getNumber(1)

    def setCurrent(self, value):
        self._setNumber(1, value)

    def getTotal(self):
        return self._getNumber(2)

    def setTotal(self, value):
        self._setNumber(2, value)

    def getEarned(self):
        return self._getNumber(3)

    def setEarned(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(QuestProgressModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addNumberProperty('current', 0)
        self._addNumberProperty('total', 0)
        self._addNumberProperty('earned', 0)
