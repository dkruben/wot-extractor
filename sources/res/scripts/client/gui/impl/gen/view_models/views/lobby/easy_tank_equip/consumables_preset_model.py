# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/consumables_preset_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/consumables_preset_model.py
from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.consumables_preset_slot_model import ConsumablesPresetSlotModel

class ConsumablesPresetType(Enum):
    STANDARD = 'standard'
    ADVANCED = 'advanced'
    IMPROVED = 'improved'


class ConsumablesPresetModel(PresetModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ConsumablesPresetModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return ConsumablesPresetType(self._getString(5))

    def setType(self, value):
        self._setString(5, value.value)

    def getItems(self):
        return self._getArray(6)

    def setItems(self, value):
        self._setArray(6, value)

    @staticmethod
    def getItemsType():
        return ConsumablesPresetSlotModel

    def _initialize(self):
        super(ConsumablesPresetModel, self)._initialize()
        self._addStringProperty('type')
        self._addArrayProperty('items', Array())
