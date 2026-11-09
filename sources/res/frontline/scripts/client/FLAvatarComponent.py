# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/FLAvatarComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/FLAvatarComponent.py
from __future__ import absolute_import
import BattleReplay
from ReservesEvents import randomReservesEvents
from frontline_common.constants import CallbackDataNames
from frontline.FLReplayController import FLReplayController
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent

class FLAvatarComponent(DynamicScriptComponent):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onDestroy(self):
        FLReplayController.delDataCallback(CallbackDataNames.FL_MODIFIER, randomReservesEvents.onChangedReservesModifier)
        super(FLAvatarComponent, self).onDestroy()

    def _onAvatarReady(self):
        if not BattleReplay.g_replayCtrl.isPlaying:
            modifier = self.entity.arenaExtraData.get('reservesModifier')
            FLReplayController.serializeCallbackData(CallbackDataNames.FL_MODIFIER, (modifier,))
            randomReservesEvents.onChangedReservesModifier(modifier)
        FLReplayController.setDataCallback(CallbackDataNames.FL_MODIFIER, randomReservesEvents.onChangedReservesModifier)

    def callCtrl(self, func, *args):
        respawnCtrl = self.__guiSessionProvider.dynamic.respawn
        if respawnCtrl:
            getattr(respawnCtrl, func, (lambda *x: None))(*args)

    def updateRespawnVehicles(self, vehsList):
        self.callCtrl('updateRespawnVehicles', vehsList)

    def updateRespawnCooldowns(self, cooldowns):
        cooldowns = {item['vehTypeCompDescr']: item['endOfCooldownPiT'] for item in cooldowns}
        self.callCtrl('updateRespawnCooldowns', cooldowns)

    def updateRespawnInfo(self, respawnInfo):
        self.callCtrl('updateRespawnInfo', respawnInfo)

    def updateVehicleLimits(self, respawnLimits):
        respawnLimits = {item['group']: item['vehTypeCompDescrs'] for item in respawnLimits}
        self.callCtrl('updateVehicleLimits', respawnLimits)

    def onTeamLivesRestored(self, teams):
        self.callCtrl('restoredTeamRespawnLives', teams)

    def updatePlayerLives(self, lives):
        self.callCtrl('updatePlayerRespawnLives', lives)
