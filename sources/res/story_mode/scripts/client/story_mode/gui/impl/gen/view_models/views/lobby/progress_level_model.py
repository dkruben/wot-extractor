# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/progress_level_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/progress_level_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class StatEnum(Enum):
    MISSIONS = 'missions'
    ASSIST = 'assist'
    KILLS = 'kills'
    DAMAGE = 'damage'
    ARMOR_USE = 'armorUse'


class ProgressLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ProgressLevelModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)

    def getName(self):
        return self._getResource(2)

    def setName(self, value):
        self._setResource(2, value)

    def getStat(self):
        return StatEnum(self._getString(3))

    def setStat(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(ProgressLevelModel, self)._initialize()
        self._addStringProperty('icon', '')
        self._addNumberProperty('value', 0)
        self._addResourceProperty('name', R.invalid())
        self._addStringProperty('stat')
