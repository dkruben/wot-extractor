# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/vehicle_stats_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/vehicle_stats_helper.py
from __future__ import absolute_import
import typing
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    import Vehicle
DEFAULT_VEHICLE_STATS = 0

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getStatTrackersVehicleStats(vehCD, vehicle=None, databaseID=None, itemsCache=None):
    if vehicle:
        from PlatoonTank import PlatoonTank
        if isinstance(vehicle, PlatoonTank):
            return vehicle.getStFrags()
    accDossier = itemsCache.items.getAccountDossier(databaseID=databaseID)
    vehStats = accDossier.getStatTrackersVehicleStatsBlock().getVehicles().get(vehCD)
    if vehStats:
        return vehStats.frags
    return DEFAULT_VEHICLE_STATS
