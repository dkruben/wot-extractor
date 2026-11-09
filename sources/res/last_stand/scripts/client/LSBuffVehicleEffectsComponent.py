# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSBuffVehicleEffectsComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSBuffVehicleEffectsComponent.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from LSBuffSequencesComponent import LSBuffSequencesComponent
from skeletons.gui.battle_session import IBattleSessionProvider
from dyn_components_groups import groupComponent
from xml_config_specs import StrParam
from VehicleEffects import DamageFromShotDecoder
from constants import VEHICLE_HIT_EFFECT

@groupComponent(moduleName=StrParam())
class LSBuffVehicleEffectsComponent(LSBuffSequencesComponent):
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    _START_TRIGGER = 'start_trigger'
    _DEATH_MODULE = 'death'

    def onDestroy(self):
        self.entity.events.onShowDamageFromShot -= self._onShowDamageFromShot
        BigWorld.player().arena.onVehicleKilled -= self._onVehicleKilled
        super(LSBuffVehicleEffectsComponent, self).onDestroy()

    def _onAvatarReady(self):
        super(LSBuffVehicleEffectsComponent, self)._onAvatarReady()
        self.entity.events.onShowDamageFromShot += self._onShowDamageFromShot
        BigWorld.player().arena.onVehicleKilled += self._onVehicleKilled

    def _onShowDamageFromShot(self, attackerID, points, effectsIndex, damageFactor, lastMaterialIsShield):
        decodedPoints = DamageFromShotDecoder.decodeHitPoints(points, self.entity.appearance.collisions)
        if not decodedPoints:
            return
        maxPriorityHitPoint = decodedPoints[-1]
        maxHitEffectCode = maxPriorityHitPoint.hitEffectCode
        hasPiercedHit = maxHitEffectCode in VEHICLE_HIT_EFFECT.PIERCED_HITS
        moduleName = maxPriorityHitPoint.componentName
        if hasPiercedHit and moduleName == self.groupComponentConfig.moduleName:
            self._triggerEffects(self._START_TRIGGER)

    def _onVehicleKilled(self, victimID, *_):
        if self.entity.id == victimID:
            if self.groupComponentConfig.moduleName == self._DEATH_MODULE:
                self._triggerEffects(self._START_TRIGGER)
