# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/vehicles_watcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/vehicles_watcher.py
from __future__ import absolute_import
from itertools import chain
from fun_random_common.fun_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_FUN
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class FunRandomVehiclesWatcher(LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher, FunSubModesWatcher):
    __itemsCache = dependency.descriptor(IItemsCache)
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_FUN

    def start(self):
        super(FunRandomVehiclesWatcher, self).start()
        self.startSubSettingsListening(self._update, desiredOnly=True)
        self.startSubSelectionListening(self._update)

    def stop(self):
        self.stopSubSelectionListening(self._update)
        self.stopSubSettingsListening(self._update, desiredOnly=True)
        super(FunRandomVehiclesWatcher, self).stop()

    def _getUnsuitableVehicles(self, onClear=False):
        return chain.from_iterable((
         LimitedLevelVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         RestrictedVehiclesWatcher._getUnsuitableVehicles(self, onClear),
         self._getUnsuitableVehiclesBase()))

    @hasDesiredSubMode(defReturn=set())
    def _getAllowedVehicleTypes(self):
        return self.getDesiredSubMode().getSettings().filtration.allowedVehTypes

    @hasDesiredSubMode(defReturn=set())
    def _getForbiddenVehicleTypes(self):
        return self.getDesiredSubMode().getSettings().filtration.forbiddenVehTypes

    @hasDesiredSubMode(defReturn=set())
    def _getForbiddenVehicleClasses(self):
        return self.getDesiredSubMode().getSettings().filtration.forbiddenClassTags

    @hasDesiredSubMode(defReturn=())
    def _getValidLevels(self):
        return self.getDesiredSubMode().getSettings().filtration.levels
