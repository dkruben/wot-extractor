# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/opt_devices_preset_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/opt_devices_preset_model.py
from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.opt_devices_preset_slot_model import OptDevicesPresetSlotModel

class OptDevicesPresetType(Enum):
    STANDARD = 'standard'
    ADVANCED = 'advanced'


class OptDevicesPresetModel(PresetModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(OptDevicesPresetModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return OptDevicesPresetType(self._getString(5))

    def setType(self, value):
        self._setString(5, value.value)

    def getItems(self):
        return self._getArray(6)

    def setItems(self, value):
        self._setArray(6, value)

    @staticmethod
    def getItemsType():
        return OptDevicesPresetSlotModel

    def getDemountKitsCount(self):
        return self._getNumber(7)

    def setDemountKitsCount(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(OptDevicesPresetModel, self)._initialize()
        self._addStringProperty('type')
        self._addArrayProperty('items', Array())
        self._addNumberProperty('demountKitsCount', 0)
