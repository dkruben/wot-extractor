# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/crosshair_settings_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/crosshair_settings_updater.py
from __future__ import absolute_import
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class CrosshairSettingsUpdater(ViewUpdater):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def initialize(self):
        super(CrosshairSettingsUpdater, self).initialize()
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onGunSettingsSet += self.__onGunSettingsSet
        return

    def finalize(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onGunSettingsSet -= self.__onGunSettingsSet
        super(CrosshairSettingsUpdater, self).finalize()
        return

    def __onGunSettingsSet(self, gunSettings):
        self.view.setGunSettings(gunSettings)
