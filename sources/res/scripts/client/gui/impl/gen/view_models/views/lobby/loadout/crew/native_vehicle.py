# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/native_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/native_vehicle.py
from frameworks.wulf import ViewModel

class NativeVehicle(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NativeVehicle, self).__init__(properties=properties, commands=commands)

    def getShortName(self):
        return self._getString(0)

    def setShortName(self, value):
        self._setString(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getTier(self):
        return self._getNumber(2)

    def setTier(self, value):
        self._setNumber(2, value)

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(NativeVehicle, self)._initialize()
        self._addStringProperty('shortName', '')
        self._addStringProperty('type', '')
        self._addNumberProperty('tier', 0)
        self._addStringProperty('nation', '')
