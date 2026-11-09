# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/ui_kit/vehicle_btn_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/vehicle_btn_model.py
from frameworks.wulf import ViewModel

class VehicleBtnModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleBtnModel, self).__init__(properties=properties, commands=commands)

    def getFlag(self):
        return self._getString(0)

    def setFlag(self, value):
        self._setString(0, value)

    def getVehType(self):
        return self._getString(1)

    def setVehType(self, value):
        self._setString(1, value)

    def getVehLvl(self):
        return self._getString(2)

    def setVehLvl(self, value):
        self._setString(2, value)

    def getVehIcon(self):
        return self._getString(3)

    def setVehIcon(self, value):
        self._setString(3, value)

    def getVehName(self):
        return self._getString(4)

    def setVehName(self, value):
        self._setString(4, value)

    def getVisible(self):
        return self._getBool(5)

    def setVisible(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(VehicleBtnModel, self)._initialize()
        self._addStringProperty('flag', '')
        self._addStringProperty('vehType', '')
        self._addStringProperty('vehLvl', '')
        self._addStringProperty('vehIcon', '')
        self._addStringProperty('vehName', '')
        self._addBoolProperty('visible', False)
