# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/discount_vehicle_bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/discount_vehicle_bonus_model.py
from gui.impl.gen.view_models.views.lobby.winback.vehicle_bonus_model import VehicleBonusModel

class DiscountVehicleBonusModel(VehicleBonusModel):
    __slots__ = ()

    def __init__(self, properties=24, commands=0):
        super(DiscountVehicleBonusModel, self).__init__(properties=properties, commands=commands)

    def getOldPrice(self):
        return self._getNumber(19)

    def setOldPrice(self, value):
        self._setNumber(19, value)

    def getNewPrice(self):
        return self._getNumber(20)

    def setNewPrice(self, value):
        self._setNumber(20, value)

    def getOldExp(self):
        return self._getNumber(21)

    def setOldExp(self, value):
        self._setNumber(21, value)

    def getNewExp(self):
        return self._getNumber(22)

    def setNewExp(self, value):
        self._setNumber(22, value)

    def getIsSelected(self):
        return self._getBool(23)

    def setIsSelected(self, value):
        self._setBool(23, value)

    def _initialize(self):
        super(DiscountVehicleBonusModel, self)._initialize()
        self._addNumberProperty('oldPrice', 0)
        self._addNumberProperty('newPrice', 0)
        self._addNumberProperty('oldExp', 0)
        self._addNumberProperty('newExp', 0)
        self._addBoolProperty('isSelected', False)
