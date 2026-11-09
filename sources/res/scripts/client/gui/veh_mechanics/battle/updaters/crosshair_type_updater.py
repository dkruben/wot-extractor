# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/crosshair_type_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/crosshair_type_updater.py
from __future__ import absolute_import
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class CrosshairTypeUpdater(ViewUpdater):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def initialize(self):
        super(CrosshairTypeUpdater, self).initialize()
        crosshairCtrl = self.__sessionProvider.shared.crosshair
        if crosshairCtrl is not None:
            crosshairCtrl.onCrosshairViewChanged += self.__onCrosshairViewChanged
            self.__onCrosshairViewChanged(crosshairCtrl.getViewID())
        return

    def finalize(self):
        crosshairCtrl = self.__sessionProvider.shared.crosshair
        if crosshairCtrl is not None:
            crosshairCtrl.onCrosshairViewChanged -= self.__onCrosshairViewChanged
        return

    def __onCrosshairViewChanged(self, viewID):
        self.view.setCrosshairType(viewID)
