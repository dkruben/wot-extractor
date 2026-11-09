# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_script/entity_dyn_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_script/entity_dyn_components.py
from __future__ import absolute_import
from cgf_network import processCreateDynamicComponent, processDestroyDynamicComponent

class BWEntitiyComponentTracker(object):

    def onDynamicComponentCreated(self, component):
        networkID = getattr(component, 'game_object_network_id', None)
        if networkID is not None:
            processCreateDynamicComponent(networkID, self.spaceID, component)
        elif not self.entityGameObject.hasComponent(type(component)):
            self.entityGameObject.assignComponent(component)
        supMethod = getattr(super(BWEntitiyComponentTracker, self), 'onDynamicComponentCreated', None)
        if callable(supMethod):
            supMethod(component)
        return

    def onDynamicComponentDestroyed(self, component):
        networkID = getattr(component, 'game_object_network_id', None)
        if networkID is not None:
            processDestroyDynamicComponent(networkID, self.spaceID, component)
        else:
            tp = type(component)
            if self.entityGameObject.hasComponent(tp):
                self.entityGameObject.removeComponent(tp)
        supMethod = getattr(super(BWEntitiyComponentTracker, self), 'onDynamicComponentDestroyed', None)
        if callable(supMethod):
            supMethod(component)
        return
