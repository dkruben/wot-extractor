# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/field_modification_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/field_modification_model.py
from frameworks.wulf import ViewModel

class FieldModificationModel(ViewModel):
    __slots__ = ('onVehiclePostProgression', )
    HIDDEN = 0
    LOCKED = 1
    UNLOCKED = 2

    def __init__(self, properties=2, commands=1):
        super(FieldModificationModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return self._getNumber(0)

    def setState(self, value):
        self._setNumber(0, value)

    def getCounter(self):
        return self._getNumber(1)

    def setCounter(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(FieldModificationModel, self)._initialize()
        self._addNumberProperty('state', 0)
        self._addNumberProperty('counter', 0)
        self.onVehiclePostProgression = self._addCommand('onVehiclePostProgression')
