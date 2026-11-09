# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/PoiBaseComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiBaseComponent.py
from __future__ import absolute_import
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class PoiBaseComponent(DynamicScriptComponent):
    _POI_GO_NAME = 'PointOfInterest{id}'
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(PoiBaseComponent, self).__init__()
        self._poiGameObject = self.__getPoiGameObject()

    def onDestroy(self):
        self._poiGameObject = None
        super(PoiBaseComponent, self).onDestroy()
        return

    def __getPoiGameObject(self):
        name = self._POI_GO_NAME.format(id=self.pointID)
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        return poiCtrl.getVehicleCapturingPoiGO(name, self.entity.entityGameObject, self.entity.id, self.spaceID)
