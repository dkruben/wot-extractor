# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/vehicle_as_polyline_target_rule.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/vehicle_as_polyline_target_rule.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerModule
from constants import IS_CLIENT, HAS_DEV_RESOURCES
if IS_CLIENT:
    from Vehicle import Vehicle
else:

    class Vehicle(object):
        pass


if HAS_DEV_RESOURCES:
    from GameplayDebug import PolylineDebugTargetComponent
else:

    class PolylineDebugTargetComponent(object):
        pass


class VehicleAsPolylineTargetConfiguratorSystem(CGF.System):
    VehicleCreated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactHas(Vehicle))
    Reactions = CGF.Reactions(VehicleCreated)

    def update(self):
        queue = CGF.CommandQueue(self.spaceID)
        for go in self.reaction(self.VehicleCreated):
            if not go.hasComponent(PolylineDebugTargetComponent):
                queue.createComponent(go, PolylineDebugTargetComponent)


@registerModule
class VehicleAsPolylineTargetModule(object):
    name = 'PolyLine Debug Target'
    group = 'Fall Tanks'
    systems = [
     CGF.RegisterSystem(VehicleAsPolylineTargetConfiguratorSystem, domain=CGF.Domain.Client)]
