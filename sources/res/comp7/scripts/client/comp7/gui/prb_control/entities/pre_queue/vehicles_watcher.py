# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/vehicles_watcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/prb_control/entities/pre_queue/vehicles_watcher.py
from __future__ import absolute_import
from itertools import chain
import typing
from comp7_common.comp7_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7, Configs
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher
from helpers import dependency, server_settings
from skeletons.gui.game_control import IComp7Controller
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class Comp7VehiclesWatcher(LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher):
    __comp7Ctrl = dependency.descriptor(IComp7Controller)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7

    def start(self):
        super(Comp7VehiclesWatcher, self).start()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged

    def stop(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        super(Comp7VehiclesWatcher, self).stop()

    def _getUnsuitableVehicles(self, onClear=False):
        return chain.from_iterable((
         LimitedLevelVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         RestrictedVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         self._getUnsuitableVehiclesBase()))

    def _getAllowedVehicleTypes(self):
        return self.__comp7Ctrl.getModeSettings().allowedVehTypes

    def _getValidLevels(self):
        return self.__comp7Ctrl.getModeSettings().levels

    @server_settings.serverSettingsChangeListener(Configs.COMP7_CONFIG.value)
    def __onServerSettingsChanged(self, diff):
        self._update()
