# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/VisualScriptEquipmentPublic.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/VisualScriptEquipmentPublic.py
from __future__ import absolute_import
from constants import EQUIPMENT_STAGES as STAGES
from VisualScriptEquipment import VisualScriptEquipment
from helpers.fixed_dict import getVisualScriptEquipmentPublicState

class VisualScriptEquipmentPublic(VisualScriptEquipment):

    def _onAvatarReady(self):
        super(VisualScriptEquipmentPublic, self)._onAvatarReady()
        self.set_equipmentStatePublic()

    def set_equipmentStatePublic(self, _=None):
        if self._context is None:
            return
        else:
            if not self.entity.isMyVehicle:
                state = getVisualScriptEquipmentPublicState(self.equipmentStatePublic)
                getattr(self._context, STAGES.toString(state.stage))()
            return
