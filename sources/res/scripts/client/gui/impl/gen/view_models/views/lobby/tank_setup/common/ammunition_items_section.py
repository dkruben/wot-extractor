# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_items_section.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_items_section.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class AmmunitionItemsSection(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(AmmunitionItemsSection, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getVehicle(self):
        return self._getString(2)

    def setVehicle(self, value):
        self._setString(2, value)

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)

    def getNewItemsCount(self):
        return self._getNumber(4)

    def setNewItemsCount(self, value):
        self._setNumber(4, value)

    def getSlots(self):
        return self._getArray(5)

    def setSlots(self, value):
        self._setArray(5, value)

    @staticmethod
    def getSlotsType():
        return BaseAmmunitionSlot

    def _initialize(self):
        super(AmmunitionItemsSection, self)._initialize()
        self._addStringProperty('type', '')
        self._addStringProperty('name', '')
        self._addStringProperty('vehicle', '')
        self._addStringProperty('vehicleType', '')
        self._addNumberProperty('newItemsCount', 0)
        self._addArrayProperty('slots', Array())
