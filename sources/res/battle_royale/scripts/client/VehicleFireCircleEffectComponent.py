# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleFireCircleEffectComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleFireCircleEffectComponent.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent
from items import vehicles
from shared_utils import first
if TYPE_CHECKING:
    from battle_royale_artefacts import FireCircle

class VehicleFireCircleEffectComponent(VehicleAbilityBaseComponent):
    __CLASS_NAME = 'VehicleFireCircleEffectComponent'
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.FIRE_CIRCLE
    __MARKER_ID = BATTLE_MARKER_STATES.FIRE_CIRCLE_STATE

    def __init__(self):
        super(VehicleFireCircleEffectComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _getDuration(self):
        return int(self.getEquipment().influenceZone.timer)

    @staticmethod
    def getEquipment():
        equipmentID = vehicles.g_cache.equipmentIDs().get(BattleRoyaleEquipments.FIRE_CIRCLE)
        equipment = vehicles.g_cache.equipments()[equipmentID]
        return equipment

    def _destroy(self):
        super(VehicleFireCircleEffectComponent, self)._destroy()
        otherComp = first([comp for comp in self.entity.dynamicComponents.values() if isinstance(comp, VehicleFireCircleEffectComponent) and comp is not self])
        if otherComp:
            otherComp.set_finishTime()
