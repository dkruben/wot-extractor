# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/StoryModeAvatarComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/StoryModeAvatarComponent.py
from __future__ import absolute_import
from Event import Event
from script_component.ScriptComponent import ScriptComponent

class StoryModeAvatarComponent(ScriptComponent):
    onSMAbilityWrongPoint = Event()
    onPositionValidChanged = Event()

    def set_wrongApplicationPoint(self, _):
        self.onSMAbilityWrongPoint(self.wrongApplicationPoint)

    def set_isPositionValid(self, prevValue):
        self.onPositionValidChanged()

    def checkPositionForEquipment(self, equipmentId, position):
        self.cell.checkPositionForEquipment(equipmentId, position)
