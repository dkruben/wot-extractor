# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/vehicle_selection_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/vehicle_selection_model.py
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class VehicleSelectionModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=2, commands=2):
        super(VehicleSelectionModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(VehicleSelectionModel, self)._initialize()
        self._addNumberProperty('count', 0)
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')
