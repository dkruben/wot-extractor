# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ImprovedRammingController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ImprovedRammingController.py
from __future__ import absolute_import
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent

@ReprInjector.withParent()
class ImprovedRammingController(VehicleDynamicComponent, IMechanicComponent):

    def __init__(self):
        super(ImprovedRammingController, self).__init__()
        self._initComponent()

    @property
    def vehicleMechanicKey(self):
        return VehicleMechanicKeys.IMPROVED_RAMMING
