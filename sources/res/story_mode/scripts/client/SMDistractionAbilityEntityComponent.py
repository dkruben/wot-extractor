# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMDistractionAbilityEntityComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMDistractionAbilityEntityComponent.py
from __future__ import absolute_import, division
import AnimationSequence, BigWorld, Math
from Event import Event
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
from story_mode_common.story_mode_constants import DISTRACTION_ABILITY

class SMDistractionAbilityEntityComponent(DynamicScriptComponent):
    _SEQUENCE_RADIUS = 200.0
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    onSMDistractionAbilityActivated = Event()

    def __init__(self):
        super(SMDistractionAbilityEntityComponent, self).__init__()
        self._animator = None
        return

    def _onAvatarReady(self):
        super(SMDistractionAbilityEntityComponent, self)._onAvatarReady()
        self._addEffect()

    def set_spottedVehiclesIDs(self, _):
        spottedVehicles = [BigWorld.entities.get(vID) for vID in self.spottedVehiclesIDs]
        self.onSMDistractionAbilityActivated(spottedVehicles)

    def onDestroy(self):
        if self._animator is not None:
            self._animator.stop()
            self._animator = None
        super(SMDistractionAbilityEntityComponent, self).onDestroy()
        return

    def _addEffect(self):
        distractionItem = self.guiSessionProvider.shared.equipments.getEquipmentByName(DISTRACTION_ABILITY)
        if distractionItem is None:
            return
        else:
            itemDescriptor = distractionItem.getDescriptor()
            if itemDescriptor.detectSequence:
                entity = BigWorld.player().vehicle if itemDescriptor.detectFromVehicle else self.entity
                if entity is None:
                    return
                matrix = Math.Matrix()
                scale = itemDescriptor.directVisionRadius / self._SEQUENCE_RADIUS
                matrix.setScale(Math.Vector3(scale, scale, scale))
                matrix.translation = entity.position
                loader = AnimationSequence.Loader(itemDescriptor.detectSequence, entity.spaceID)
                animator = loader.loadSync()
                animator.bindToWorld(matrix)
                animator.speed = 1
                animator.loopCount = 1
                animator.start()
                self._animator = animator
            return
