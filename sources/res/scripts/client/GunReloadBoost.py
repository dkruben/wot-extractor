# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/GunReloadBoost.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/GunReloadBoost.py
from __future__ import absolute_import
from cache import cached_property
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from view_state_component import ViewStateComponent

class GunReloadBoost(ViewStateComponent):

    @cached_property
    def _sessionProvider(self):
        return dependency.instance(IBattleSessionProvider)

    def onReloadBoost(self):
        from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
        if self.entity.id == self._sessionProvider.shared.vehicleState.getControllingVehicleID():
            self._sessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.GUN_RELOAD_BOOST, None)
        return
