# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/pre_queue/vehicles_watcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/prb_control/entities/pre_queue/vehicles_watcher.py
from __future__ import absolute_import
import typing
from PlayerEvents import g_playerEvents
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class FortRushVehicleWatcher(BaseVehiclesWatcher):
    __itemsCache = dependency.descriptor(IItemsCache)
    __battleController = dependency.descriptor(IFortRushBattleController)

    def start(self):
        super(FortRushVehicleWatcher, self).start()
        g_playerEvents.onConfigModelUpdated += self.__onConfigModelUpdated

    def stop(self):
        g_playerEvents.onConfigModelUpdated -= self.__onConfigModelUpdated
        super(FortRushVehicleWatcher, self).stop()

    def _getUnsuitableVehicles(self, onClear=False):
        if onClear:
            return self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY).values()
        criteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.CUSTOM(self.__isUnsuitableVehicle)
        return self.__itemsCache.items.getVehicles(criteria).values()

    def __isUnsuitableVehicle(self, vehicle):
        return self.__battleController.isSuitableVehicle(vehicle) is not None

    def __onConfigModelUpdated(self, gpKey):
        if fortRushBattlesConfigGameParamsSchema.gpKey == gpKey:
            self._update()
