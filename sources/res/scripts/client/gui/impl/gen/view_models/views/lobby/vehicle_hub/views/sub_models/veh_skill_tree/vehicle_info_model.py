# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/vehicle_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/vehicle_info_model.py
from frameworks.wulf import ViewModel

class VehicleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleInfoModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)

    def getIsPremium(self):
        return self._getBool(3)

    def setIsPremium(self, value):
        self._setBool(3, value)

    def getPrestigeLevel(self):
        return self._getNumber(4)

    def setPrestigeLevel(self, value):
        self._setNumber(4, value)

    def getIsBroken(self):
        return self._getBool(5)

    def setIsBroken(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(VehicleInfoModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addStringProperty('type', '')
        self._addStringProperty('name', '')
        self._addBoolProperty('isPremium', False)
        self._addNumberProperty('prestigeLevel', 0)
        self._addBoolProperty('isBroken', False)
