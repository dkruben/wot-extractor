# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/br_battle_messages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/game_control/br_battle_messages.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency, int2roman
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener
from skeletons.gui.battle_session import IBattleSessionProvider
import BattleReplay

class ProgressionMessagesPlayer(IProgressionListener):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def updateData(self, arenaLevelData):
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        else:
            if arenaLevelData.level == 1 or not arenaLevelData.levelIsChanged:
                return
            ctrl = self._sessionProvider.shared.messages
            isObserver = BigWorld.player().isObserver()
            if ctrl is not None and not isObserver:
                ctrl.onShowPlayerMessageByKey('VEHICLE_LEVEL_UP', {'level': (int2roman(arenaLevelData.level))})
            return

    def onMaxLvlAchieved(self):
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        else:
            ctrl = self._sessionProvider.shared.messages
            isObserver = BigWorld.player().isObserver()
            if ctrl is not None and not isObserver:
                ctrl.onShowPlayerMessageByKey('VEHICLE_LEVEL_MAXED')
            return
