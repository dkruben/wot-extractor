# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_vehicle_module.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_vehicle_module.py
from frameworks.wulf import Array, ViewModel

class ArmorVehicleModule(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ArmorVehicleModule, self).__init__(properties=properties, commands=commands)

    def getCompactDescr(self):
        return self._getNumber(0)

    def setCompactDescr(self, value):
        self._setNumber(0, value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getImage(self):
        return self._getString(2)

    def setImage(self, value):
        self._setString(2, value)

    def getDependencies(self):
        return self._getArray(3)

    def setDependencies(self, value):
        self._setArray(3, value)

    @staticmethod
    def getDependenciesType():
        return int

    def getMechanics(self):
        return self._getArray(4)

    def setMechanics(self, value):
        self._setArray(4, value)

    @staticmethod
    def getMechanicsType():
        return unicode

    def _initialize(self):
        super(ArmorVehicleModule, self)._initialize()
        self._addNumberProperty('compactDescr', 0)
        self._addNumberProperty('level', 0)
        self._addStringProperty('image', '')
        self._addArrayProperty('dependencies', Array())
        self._addArrayProperty('mechanics', Array())
