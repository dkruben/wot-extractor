# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/PoiVehicleComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/PoiVehicleComponent.py
from __future__ import absolute_import
import CGF
from PoiBaseComponent import PoiBaseComponent
from points_of_interest.components import PoiVehicleStateComponent

class PoiVehicleComponent(PoiBaseComponent):

    def __init__(self):
        super(PoiVehicleComponent, self).__init__()
        self.__isDead = False

    def onDestroy(self):
        if self._poiGameObject:
            self._poiGameObject.removeComponent(PoiVehicleStateComponent)
        self.__isDead = True
        super(PoiVehicleComponent, self).onDestroy()

    def _onAvatarReady(self):
        if not self.__isDead:
            queue = CGF.CommandQueue(self.spaceID)
            queue.removeComponent(self._poiGameObject, PoiVehicleStateComponent)
            queue.createComponent(self._poiGameObject, PoiVehicleStateComponent, self.pointID)
