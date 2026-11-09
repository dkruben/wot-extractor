# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/additional_mission_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/additional_mission_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class AdditionalMissionType(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'


class AdditionalMissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AdditionalMissionModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return AdditionalMissionType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getMaxPoints(self):
        return self._getNumber(1)

    def setMaxPoints(self, value):
        self._setNumber(1, value)

    def getCurrentPoints(self):
        return self._getNumber(2)

    def setCurrentPoints(self, value):
        self._setNumber(2, value)

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)

    def getIsProgressHidden(self):
        return self._getBool(4)

    def setIsProgressHidden(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(AdditionalMissionModel, self)._initialize()
        self._addStringProperty('type')
        self._addNumberProperty('maxPoints', 0)
        self._addNumberProperty('currentPoints', 0)
        self._addBoolProperty('isEnabled', False)
        self._addBoolProperty('isProgressHidden', False)
