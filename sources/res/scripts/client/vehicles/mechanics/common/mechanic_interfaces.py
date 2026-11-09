# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/common/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/common/mechanic_interfaces.py
from __future__ import absolute_import
import typing
from vehicles.components.component_interfaces import IVehicleSlotComponent
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicVariant, VehicleMechanicKey

class IMechanicComponentLogic(object):

    @property
    def isValid(self):
        raise NotImplementedError

    @property
    def vehicleMechanicKey(self):
        raise NotImplementedError


class IMechanicComponent(IVehicleSlotComponent, IMechanicComponentLogic):
    pass


class IMechanicWithVariants(object):

    @property
    def mechanicVariant(self):
        raise NotImplementedError
