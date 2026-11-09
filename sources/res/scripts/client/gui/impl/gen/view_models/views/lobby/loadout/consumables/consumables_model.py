# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/consumables/consumables_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/consumables/consumables_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.loadout.base_loadout_model import BaseLoadoutModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.consumable_slot_model import ConsumableSlotModel

class ConsumablesModel(BaseLoadoutModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=1):
        super(ConsumablesModel, self).__init__(properties=properties, commands=commands)

    def getHasChanges(self):
        return self._getBool(1)

    def setHasChanges(self, value):
        self._setBool(1, value)

    def getAutoloadEnabled(self):
        return self._getBool(2)

    def setAutoloadEnabled(self, value):
        self._setBool(2, value)

    def getConsumables(self):
        return self._getArray(3)

    def setConsumables(self, value):
        self._setArray(3, value)

    @staticmethod
    def getConsumablesType():
        return ConsumableSlotModel

    def _initialize(self):
        super(ConsumablesModel, self)._initialize()
        self._addBoolProperty('hasChanges', False)
        self._addBoolProperty('autoloadEnabled', False)
        self._addArrayProperty('consumables', Array())
