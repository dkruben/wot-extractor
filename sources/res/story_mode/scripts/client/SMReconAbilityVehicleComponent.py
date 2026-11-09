# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMReconAbilityVehicleComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMReconAbilityVehicleComponent.py
from __future__ import absolute_import
import typing
from Event import Event
from gui.impl.gen import R
from script_component.DynamicScriptComponent import DynamicScriptComponent
from story_mode_common.story_mode_constants import RECON_ABILITY, EQUIPMENT_STAGES as STAGES
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.consumables.equipment_ctrl import _EquipmentItem

class SMReconAbilityVehicleComponent(DynamicScriptComponent):
    _EQUIPMENT_NAME = RECON_ABILITY
    onSMReconAbilityActivated = Event()

    def __init__(self):
        super(SMReconAbilityVehicleComponent, self).__init__()
        self.entity.guiSessionProvider.shared.equipments.onEquipmentUpdated += self._onEquipmentUpdated

    def onDestroy(self):
        super(SMReconAbilityVehicleComponent, self).onDestroy()
        self.entity.guiSessionProvider.shared.equipments.onEquipmentUpdated -= self._onEquipmentUpdated

    def _onEquipmentUpdated(self, _, item):
        itemDescriptor = item.getDescriptor()
        isReconAbility = itemDescriptor.name == self._EQUIPMENT_NAME
        if isReconAbility:
            if item.getStage() == STAGES.ACTIVATING:
                self.onSMReconAbilityActivated(True)
            if item.getStage() == STAGES.COOLDOWN and item.getPrevStage() == STAGES.DEACTIVATING:
                self.onSMReconAbilityActivated(False)
            equipmentInfo = {}
            if item.getStage() in (STAGES.ACTIVATING, STAGES.DEACTIVATING):
                res = R.strings.ingame_gui.abilities.recon
                equipmentInfo = {'totalTime': (item.getTotalTime()), 
                   'finishTime': 0, 
                   'text': (res.stopVehicle() if item.getStage() == STAGES.ACTIVATING else res.startVehicle())}
            self.entity.guiSessionProvider.shared.vehicleState.onEquipmentComponentUpdated(self._EQUIPMENT_NAME, self.entity.id, equipmentInfo)
