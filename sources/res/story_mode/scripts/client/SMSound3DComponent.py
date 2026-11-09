# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMSound3DComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMSound3DComponent.py
from __future__ import absolute_import
import typing
from SMSoundAbstractComponent import SMSoundAbstractComponent
from SMSound3DObjectComponent import SMSound3DObjectComponent

class SMSound3DComponent(SMSoundAbstractComponent):

    @property
    def soundObject(self):
        if self.entity is None or self.entity.isDestroyed:
            return
        component = self.entity.dynamicComponents.get(SMSound3DObjectComponent.__name__)
        if component:
            return component.soundObject
        else:
            return

    def _play(self, soundName):
        if self.soundObject is not None:
            self.soundObject.play(soundName)
        return
