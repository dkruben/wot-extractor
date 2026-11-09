# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/crew_helpers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_helpers/__init__.py
import logging, typing
from helpers.dependency import replace_none_kwargs
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Tuple
    from gui.shared.gui_items.Vehicle import Vehicle
    from gui.shared.gui_items.Tankman import Tankman
_logger = logging.getLogger(__name__)

@replace_none_kwargs(itemsCache=IItemsCache)
def _getVehicleFromTankman(tankman, itemsCache=None):
    if tankman.vehicleDescr:
        return itemsCache.items.getVehicle(tankman.vehicleInvID)
    return itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)


@replace_none_kwargs(wotPlusCtrl=IWotPlusController)
def tankmanHasCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    vehicle = _getVehicleFromTankman(tankman)
    if not vehicle:
        _logger.warning("Couldn't find a Vehicle for %r.", tankman)
        return (
         False, False)
    return wotPlusCtrl.hasCrewAssistOrderSets(vehicle.intCD, tankmanRole)


@replace_none_kwargs(wotPlusCtrl=IWotPlusController)
def getTankmanCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    vehicle = _getVehicleFromTankman(tankman)
    if not vehicle:
        _logger.warning("Couldn't find a Vehicle for %r.", tankman)
        return {}
    return wotPlusCtrl.getCrewAssistOrderSets(vehicle.intCD, tankmanRole)
