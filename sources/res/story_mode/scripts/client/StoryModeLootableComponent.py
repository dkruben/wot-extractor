# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/StoryModeLootableComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/StoryModeLootableComponent.py
from __future__ import absolute_import
import CGF, Math
from script_component.DynamicScriptComponent import DynamicScriptComponent
from Event import SafeEvent, EventManager
from typing import List

class StoryModeLootableComponent(DynamicScriptComponent):
    _PREFAB_URL_BY_STYLE = {'SM_LOOT_EQUIPMENT': 'content/CGFPrefabs/Storymode/loot.prefab', 
       'SM_LOOT_PLAN': 'content/CGFPrefabs/Storymode/loot.prefab', 
       'SM_LOOT_TANK': 'content/CGFPrefabs/Storymode/loot_yellow.prefab'}

    def __init__(self, *args, **kwargs):
        super(StoryModeLootableComponent, self).__init__(*args, **kwargs)
        self._eventManager = EventManager()
        self.onStartCapturing = SafeEvent(self._eventManager)
        self.onStopCapturing = SafeEvent(self._eventManager)
        self._loadPrefab()

    def set_startTime(self, prevValue):
        if self.startTime == -1:
            self.onStopCapturing()
            return
        self.onStartCapturing(self.startTime, self.captureTime)

    def onDestroy(self):
        self._eventManager.clear()
        super(StoryModeLootableComponent, self).onDestroy()

    def _loadPrefab(self):
        if self.markerStyle in self._PREFAB_URL_BY_STYLE:
            CGF.loadAndCreatePrefabWithParent(self._PREFAB_URL_BY_STYLE[self.markerStyle], self.entity.entityGameObject, Math.Vector3(), self._onPrefabLoaded)

    def _onPrefabLoaded(self, objects, queue):
        root = objects[0]
        queue.activateGameObject(root)
        transform = queue.component(root, CGF.TransformComponent)
        if transform:
            transform.scale = Math.Vector3(self.radius, 1.0, self.radius)
