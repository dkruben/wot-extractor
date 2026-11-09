# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/event_platform/respawns/respawns.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/event_platform/respawns/respawns.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
import CGF
from RespawnPolicyVehicleLinkComponent import RespawnPolicyVehicleLinkComponent
if TYPE_CHECKING:
    from typing import Optional

class RespawnPolicySystem(CGF.System):
    PolicyIterate = CGF.IterateReaction(CGF.GameObject, CGF.Ro(RespawnPolicyVehicleLinkComponent))
    Reactions = CGF.Reactions(PolicyIterate)

    def update(self):
        pass

    def findPolicyGameObject(self, vehicleId):
        for policyGO, link in self.reaction(self.PolicyIterate):
            if link.vehicleId == vehicleId:
                return policyGO

        return
