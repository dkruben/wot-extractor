# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/banned_vehicle_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/banned_vehicle_model.py
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel

class BannedVehicleModel(Comp7VehicleModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(BannedVehicleModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(12)

    def setCount(self, value):
        self._setNumber(12, value)

    def _initialize(self):
        super(BannedVehicleModel, self)._initialize()
        self._addNumberProperty('count', 0)
