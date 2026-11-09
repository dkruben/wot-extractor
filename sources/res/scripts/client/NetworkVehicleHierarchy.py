# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/NetworkVehicleHierarchy.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/NetworkVehicleHierarchy.py
from __future__ import absolute_import
from vehicle_hierarchy import createClientVehicleHierarchy, removeClientVehicleHierarchy
from vehicles.components.vehicle_component import VehicleDynamicComponent

class NetworkVehicleHierarchy(VehicleDynamicComponent):

    def __init__(self):
        super(NetworkVehicleHierarchy, self).__init__()
        self._initComponent()

    def onDestroy(self):
        gameObject = self.entity.entityGameObject
        if gameObject is not None:
            removeClientVehicleHierarchy(gameObject)
        super(NetworkVehicleHierarchy, self).onDestroy()
        return

    def _onAppearanceReady(self):
        super(NetworkVehicleHierarchy, self)._onAppearanceReady()
        self.__create()

    def __create(self):
        gameObject = self.entity.entityGameObject
        if gameObject is None:
            return
        else:
            createClientVehicleHierarchy(gameObject, self.hierarchyInfo, True)
            return
