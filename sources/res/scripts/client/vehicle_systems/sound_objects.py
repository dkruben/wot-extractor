# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/sound_objects.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/sound_objects.py
from __future__ import absolute_import
import BigWorld
from constants import IS_EDITOR
from vehicle_systems.tankStructure import TankSoundObjectsIndexes

def getGunSoundObject(vehicle):
    if vehicle.appearance is not None and vehicle.appearance.engineAudition:
        soundObject = vehicle.appearance.engineAudition.getSoundObject(TankSoundObjectsIndexes.GUN)
        if soundObject is not None:
            return soundObject
        return SOUND_OBJECT_STUB
    return SOUND_OBJECT_STUB


def getGunSoundObjectDistance(vehicle):
    if IS_EDITOR:
        return vehicle.position.length
    return (BigWorld.camera().position - vehicle.position).length


class SoundObjectStub(object):

    def play(self, *_, **__):
        pass

    def setRTPC(self, *_, **__):
        pass


SOUND_OBJECT_STUB = SoundObjectStub()
