# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/missions_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/missions_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_categorizations_model import MissionsCategorizationsModel

class MissionsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MissionsModel, self).__init__(properties=properties, commands=commands)

    def getOperationId(self):
        return self._getNumber(0)

    def setOperationId(self, value):
        self._setNumber(0, value)

    def getOperationName(self):
        return self._getString(1)

    def setOperationName(self, value):
        self._setString(1, value)

    def getMinRequiredVehicle(self):
        return self._getNumber(2)

    def setMinRequiredVehicle(self, value):
        self._setNumber(2, value)

    def getMaxRequiredVehicle(self):
        return self._getNumber(3)

    def setMaxRequiredVehicle(self, value):
        self._setNumber(3, value)

    def getMissionsCategorizations(self):
        return self._getArray(4)

    def setMissionsCategorizations(self, value):
        self._setArray(4, value)

    @staticmethod
    def getMissionsCategorizationsType():
        return MissionsCategorizationsModel

    def _initialize(self):
        super(MissionsModel, self)._initialize()
        self._addNumberProperty('operationId', 0)
        self._addStringProperty('operationName', '')
        self._addNumberProperty('minRequiredVehicle', 0)
        self._addNumberProperty('maxRequiredVehicle', 0)
        self._addArrayProperty('missionsCategorizations', Array())
