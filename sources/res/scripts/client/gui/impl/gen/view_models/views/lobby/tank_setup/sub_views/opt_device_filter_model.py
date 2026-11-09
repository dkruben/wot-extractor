# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/opt_device_filter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/opt_device_filter_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.filters_model import FiltersModel

class OptDeviceFilterModel(FiltersModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=2):
        super(OptDeviceFilterModel, self).__init__(properties=properties, commands=commands)

    def getSelectedCount(self):
        return self._getNumber(4)

    def setSelectedCount(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(OptDeviceFilterModel, self)._initialize()
        self._addNumberProperty('selectedCount', 0)
