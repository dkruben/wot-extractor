# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/optional_devices_assistant_item.py
from frameworks.wulf import Array, ViewModel

class OptionalDevicesAssistantItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(OptionalDevicesAssistantItem, self).__init__(properties=properties, commands=commands)

    def getPopularity(self):
        return self._getReal(0)

    def setPopularity(self, value):
        self._setReal(0, value)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return unicode

    def _initialize(self):
        super(OptionalDevicesAssistantItem, self)._initialize()
        self._addRealProperty('popularity', 0.0)
        self._addArrayProperty('items', Array())
