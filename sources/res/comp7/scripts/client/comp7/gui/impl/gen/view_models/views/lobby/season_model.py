# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/season_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/season_model.py
from enum import IntEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from frameworks.wulf import ViewModel

class SeasonState(IntEnum):
    NOTSTARTED = 0
    JUSTSTARTED = 1
    ACTIVE = 2
    ENDSOON = 3
    END = 4
    DISABLED = 5


class SeasonModel(ViewModel):
    __slots__ = ('pollServerTime', )

    def __init__(self, properties=6, commands=1):
        super(SeasonModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return SeasonName(self._getString(0))

    def setName(self, value):
        self._setString(0, value.value)

    def getStartTimestamp(self):
        return self._getNumber(1)

    def setStartTimestamp(self, value):
        self._setNumber(1, value)

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)

    def getServerTimestamp(self):
        return self._getNumber(3)

    def setServerTimestamp(self, value):
        self._setNumber(3, value)

    def getState(self):
        return SeasonState(self._getNumber(4))

    def setState(self, value):
        self._setNumber(4, value.value)

    def getHasTentativeDates(self):
        return self._getBool(5)

    def setHasTentativeDates(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(SeasonModel, self)._initialize()
        self._addStringProperty('name')
        self._addNumberProperty('startTimestamp', 0)
        self._addNumberProperty('endTimestamp', 0)
        self._addNumberProperty('serverTimestamp', 0)
        self._addNumberProperty('state')
        self._addBoolProperty('hasTentativeDates', False)
        self.pollServerTime = self._addCommand('pollServerTime')
