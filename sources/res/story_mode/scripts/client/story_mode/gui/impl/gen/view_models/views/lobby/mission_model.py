# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class MissionsDifficulty(Enum):
    UNDEFINED = ''
    NORMAL = 'normal'
    HARD = 'hard'
    VERY_HARD = 'very_hard'


class MissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MissionModel, self).__init__(properties=properties, commands=commands)

    def getMissionId(self):
        return self._getNumber(0)

    def setMissionId(self, value):
        self._setNumber(0, value)

    def getDisplayName(self):
        return self._getString(1)

    def setDisplayName(self, value):
        self._setString(1, value)

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)

    def getLocked(self):
        return self._getBool(3)

    def setLocked(self, value):
        self._setBool(3, value)

    def getDifficulty(self):
        return MissionsDifficulty(self._getString(4))

    def setDifficulty(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(MissionModel, self)._initialize()
        self._addNumberProperty('missionId', 0)
        self._addStringProperty('displayName', '')
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('locked', False)
        self._addStringProperty('difficulty')
