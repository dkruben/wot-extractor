# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/consumables_preset_slot_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/consumables_preset_slot_model.py
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.slot_info_model import SlotInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class ConsumablesPresetSlotModel(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(ConsumablesPresetSlotModel, self).__init__(properties=properties, commands=commands)

    @property
    def info(self):
        return self._getViewModel(13)

    @staticmethod
    def getInfoType():
        return SlotInfoModel

    def _initialize(self):
        super(ConsumablesPresetSlotModel, self)._initialize()
        self._addViewModelProperty('info', SlotInfoModel())
