# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_preset_model_type.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_preset_model_type.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class OptionalDevicesAssistantPresetTypeEnum(IntEnum):
    COMMON = 0
    LEGENDARY = 1


class OptionalDevicesAssistantPresetModelType(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(OptionalDevicesAssistantPresetModelType, self).__init__(properties=properties, commands=commands)

    def getMType(self):
        return OptionalDevicesAssistantPresetTypeEnum(self._getNumber(0))

    def setMType(self, value):
        self._setNumber(0, value.value)

    def _initialize(self):
        super(OptionalDevicesAssistantPresetModelType, self)._initialize()
        self._addNumberProperty('mType')
