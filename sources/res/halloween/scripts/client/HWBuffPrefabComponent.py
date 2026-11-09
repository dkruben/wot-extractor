# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWBuffPrefabComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWBuffPrefabComponent.py
from __future__ import absolute_import
import functools, CGF, Math
from WeakMethod import WeakMethod
from dyn_components_groups import groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from xml_config_specs import StrParam, Vector3Param

def _onPrefabLoaded(weakCb, objects, queue):
    callback = weakCb()
    if callback is not None:
        return callback(objects, queue)
    else:
        return False


@groupComponent(prefab=StrParam(), offset=Vector3Param(), scale=Vector3Param(default=(1.0,
                                                                                      1.0,
                                                                                      1.0)), rotationYPR=Vector3Param())
class HWBuffPrefabComponent(DynamicScriptComponent):

    def __init__(self):
        super(HWBuffPrefabComponent, self).__init__()
        self.go = None
        return

    def onDestroy(self):
        if self.go:
            self.go.destroy()
            self.go = None
        return

    def _onAvatarReady(self):
        appearance = self.entity.appearance
        if appearance is not None:
            config = self.groupComponentConfig
            transform = Math.createSRTMatrix(config.scale, config.rotationYPR, config.offset)
            CGF.loadAndCreatePrefabWithParent(config.prefab, appearance.gameObject, transform, functools.partial(_onPrefabLoaded, WeakMethod(self._onPrefabLoaded)))
        return

    def _onPrefabLoaded(self, objects, queue):
        root = objects[0]
        self.go = queue.gameObject(root)
        queue.activateGameObject(root)
        return True
