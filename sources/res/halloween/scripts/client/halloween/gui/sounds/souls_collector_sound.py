# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/sounds/souls_collector_sound.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/sounds/souls_collector_sound.py
from __future__ import absolute_import, division
import SoundGroups
from halloween.gui.sounds.sound_constants import SoulsCollectorSounds, SOULS_COLLECTOR_OBJ_NAME
from halloween.gui.sounds import playSound

class SoulsCollectorSound(object):

    def __init__(self, collectorComp):
        self._soulsCollectorSoundObject = SoundGroups.g_instance.WWgetSoundObject(SOULS_COLLECTOR_OBJ_NAME, collectorComp.entity.matrix)
        self._soulsCollectorSoundObject.play(SoulsCollectorSounds.LOOP)
        self._needNotifyCollectorFullFilled = True

    def destroy(self):
        if self._soulsCollectorSoundObject:
            self._soulsCollectorSoundObject.stopAll()
            self._soulsCollectorSoundObject = None
        return

    def updateSoulsCollectorState(self, collected, capacity, isCollecting):
        self._soulsCollectorSoundObject.setRTPC(SoulsCollectorSounds.RTPC, float(collected) / capacity * 100)
        if collected > 0 and self._needNotifyCollectorFullFilled and collected >= capacity:
            self._needNotifyCollectorFullFilled = False
            playSound(SoulsCollectorSounds.FULL)
        elif collected <= 0:
            self._needNotifyCollectorFullFilled = True

    def onFilling(self, collected):
        if collected > 0:
            playSound(SoulsCollectorSounds.COLLECT)
