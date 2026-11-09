# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/difficulty_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/difficulty_item_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class StateEnum(Enum):
    DEFAULT = 'default'
    SELECTED = 'selected'


class DifficultyItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(DifficultyItemModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def getIsNew(self):
        return self._getBool(1)

    def setIsNew(self, value):
        self._setBool(1, value)

    def getIsLocked(self):
        return self._getBool(2)

    def setIsLocked(self, value):
        self._setBool(2, value)

    def getState(self):
        return StateEnum(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)

    def getMissionCount(self):
        return self._getNumber(4)

    def setMissionCount(self, value):
        self._setNumber(4, value)

    def getModifier(self):
        return self._getNumber(5)

    def setModifier(self, value):
        self._setNumber(5, value)

    def getCompletedMissions(self):
        return self._getString(6)

    def setCompletedMissions(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(DifficultyItemModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addBoolProperty('isNew', False)
        self._addBoolProperty('isLocked', False)
        self._addStringProperty('state')
        self._addNumberProperty('missionCount', 0)
        self._addNumberProperty('modifier', 0)
        self._addStringProperty('completedMissions', '')
