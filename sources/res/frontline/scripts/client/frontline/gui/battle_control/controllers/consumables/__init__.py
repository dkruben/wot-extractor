# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/battle_control/controllers/consumables/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/battle_control/controllers/consumables/__init__.py
from __future__ import absolute_import
from constants import ARENA_BONUS_TYPE
from frontline.gui.battle_control.controllers.consumables import epic_equipment_ctrl

def registerFLEquipmentController():
    from gui.battle_control.controllers.consumables import extendEquipmentController
    extendEquipmentController({(ARENA_BONUS_TYPE.EPIC_BATTLE): (epic_equipment_ctrl.EpicEquipmentsController)}, {(ARENA_BONUS_TYPE.EPIC_BATTLE): (epic_equipment_ctrl.EpicReplayEquipmentController)})
