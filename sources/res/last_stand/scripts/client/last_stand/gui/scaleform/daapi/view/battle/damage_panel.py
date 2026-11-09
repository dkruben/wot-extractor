# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/damage_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/damage_panel.py
from __future__ import absolute_import
from gui.battle_control.arena_info.settings import INVALIDATE_OP
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel

class LSDamagePanel(DamagePanel):

    def updateVehiclesInfo(self, updated, arenaDP):
        updated = [item for item in updated if item[0] & INVALIDATE_OP.VEHICLE_INFO]
        if updated:
            super(LSDamagePanel, self).updateVehiclesInfo(updated, arenaDP)
