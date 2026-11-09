# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMSound3DObjectComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMSound3DObjectComponent.py
from __future__ import absolute_import
import typing, SoundGroups
from script_component.DynamicScriptComponent import DynamicScriptComponent

class SMSound3DObjectComponent(DynamicScriptComponent):
    _SOUND_OBJ_NAME_PATTERN = 'SMSound3DObjectComponent_{}'

    def __init__(self):
        super(SMSound3DObjectComponent, self).__init__()
        self._soundObject = SoundGroups.g_instance.WWgetSoundObject(self._SOUND_OBJ_NAME_PATTERN.format(self.entity.id), self.entity.matrix)

    def onDestroy(self):
        self._soundObject.stopAll()
        self._soundObject = None
        super(SMSound3DObjectComponent, self).onDestroy()
        return

    @property
    def soundObject(self):
        return self._soundObject
