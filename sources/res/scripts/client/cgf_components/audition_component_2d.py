# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/audition_component_2d.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/audition_component_2d.py
from __future__ import absolute_import
import CGF
from Sound import Audition2D
from constants import IS_EDITOR, IS_CGF_DUMP
if IS_EDITOR or IS_CGF_DUMP:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle

class AuditionsSystem(CGF.System):
    Activated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(Audition2D))
    VehicleAccess = CGF.AccessReaction(CGF.Rw(Vehicle))
    Reactions = CGF.Reactions(Activated, VehicleAccess)

    def update(self):
        vehicleAccess = self.reaction(self.VehicleAccess)
        for go, audition in self.reaction(self.Activated):
            vehicle = CGF.findParentWithReaction(go, vehicleAccess)
            if vehicle is not None:
                audition.isPlayer = vehicle.isPlayerVehicle

        return
