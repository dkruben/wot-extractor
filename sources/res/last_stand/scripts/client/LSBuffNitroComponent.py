# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSBuffNitroComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSBuffNitroComponent.py
from __future__ import absolute_import
import weakref
from dyn_components_groups import groupComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from xml_config_specs import IntParam
_NITRO_APPEARED = 1
_NITRO_HIDDEN = 0

@groupComponent(nitro=IntParam())
class LSBuffNitroComponent(DynamicScriptComponent):

    def __init__(self):
        super(LSBuffNitroComponent, self).__init__()
        self._appearanceRef = weakref.ref(self.entity.appearance)

    def _onAvatarReady(self):
        super(LSBuffNitroComponent, self)._onAvatarReady()
        nitro = getattr(self.groupComponentConfig, 'nitro', _NITRO_APPEARED)
        self._setType(nitro)

    def onDestroy(self):
        nitroComponents = [c for c in self.entity.dynamicComponents.values() if isinstance(c, LSBuffNitroComponent)]
        if len(nitroComponents) <= 1:
            self._setType(_NITRO_HIDDEN)
        super(LSBuffNitroComponent, self).onDestroy()

    def _setType(self, nitro):
        appearance = self._appearanceRef()
        if appearance is not None:
            effectMgr = appearance.customEffectManager
            if effectMgr:
                effectMgr.variables['Nitro'] = nitro
        return
