# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/components.py
from __future__ import absolute_import
import typing, account_helpers
from gui.prb_control.entities.base.squad.components import SquadRestrictionsProvider
from items.vehicles import getVehicleType
if typing.TYPE_CHECKING:
    from typing import List
    from items.vehicles import VehicleType

class FortRushSquadRestrictionsProvider(SquadRestrictionsProvider):

    def _getAllSelectedVehicles(self, ignoreOwnVehiclesInUnit):
        unitMgrId, unit = self._unitEntity.getUnit(safe=True)
        if unit is None:
            return []
        else:
            ownDbID = account_helpers.getAccountDatabaseID()
            vehicles = []
            for slot in self._unitEntity.getSlotsIterator(unitMgrId, unit):
                if slot.player is not None and slot.player.isReady and slot.vehicle is not None:
                    if ignoreOwnVehiclesInUnit and slot.player.dbID == ownDbID:
                        continue
                    vehicles.append(getVehicleType(slot.vehicle.vehTypeCompDescr))

            return vehicles
