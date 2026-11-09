# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/sounds/vehicle_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/sounds/vehicle_components.py
from __future__ import absolute_import
import BigWorld, SoundGroups
from last_stand.gui.sounds import SoundComponentBase, playSound
from last_stand.gui.sounds.sound_constants import BOTS_ENGINE, BOTS_EXPLOSION, LootSounds, ObeliskBattleSound

class LSCommonEnemySounds(SoundComponentBase):

    def onAvatarReady(self):
        engineEvent = BOTS_ENGINE.get(self.parent.entity.typeDescriptor.name)
        if engineEvent is not None:
            self.parent.soundObject.play(engineEvent)
        return

    def onVehicleKilled(self, victimID, *_):
        if self.parent.entity.id == victimID:
            destroyEvent = BOTS_EXPLOSION.get(self.parent.entity.typeDescriptor.name)
            if destroyEvent is not None:
                SoundGroups.g_instance.playSoundPos(destroyEvent, self.parent.entity.position)
        return


class LSObeliskSounds(SoundComponentBase):

    def onDamageReceived(self, attackerID, _, damage):
        if damage <= 0:
            return
        if BigWorld.player().playerVehicleID == attackerID:
            playSound(ObeliskBattleSound.HIT_2D)
        self.parent.soundObject.play(ObeliskBattleSound.HIT_3D)


class LSLootSounds(SoundComponentBase):

    def onLootSucceed(self, lootID, vehicleIDs):
        player = BigWorld.player()
        if player is None:
            return
        else:
            if player.playerVehicleID == self.parent.entity.id:
                playSound(LootSounds.Player.PICKUP_SUCCEED.get(lootID))
            elif not vehicleIDs or player.playerVehicleID in vehicleIDs:
                self.parent.soundObject.play(LootSounds.Ally.PICKUP_SUCCEED)
            return
