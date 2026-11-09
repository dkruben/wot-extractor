# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_vehicle_appearance_system.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_vehicle_appearance_system.py
from __future__ import absolute_import
import typing, BigWorld, CGF, Vehicular
from gui.hangar_vehicle_appearance import ActivateContext
from vehicle_appearance.component import VehicleAppearanceComponent
if typing.TYPE_CHECKING:
    from gui.hangar_vehicle_appearance import HangarVehicleAppearance

class HangarAppearanceSystem(CGF.System):
    Activate = CGF.ActivateReaction(CGF.ReactRo(VehicleAppearanceComponent), CGF.Rw(BigWorld.CollisionComponent), CGF.OptRo(Vehicular.GeneralWheelsAnimator), CGF.OptRo(Vehicular.DirtComponent))
    Reactions = CGF.Reactions(Activate)

    def update(self):
        for reactions in self.reaction(self.Activate):
            self.__activateAppearance(reactions)

    def __activateAppearance(self, reactions):
        appearanceCmp = reactions[0]
        appearance = appearanceCmp.appearance
        if appearance is not None:
            appearance.onActivate(ActivateContext(*reactions[1:]))
        return
