# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/controllers/sound_ctrls/fun_random_battle_sounds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/controllers/sound_ctrls/fun_random_battle_sounds.py
from __future__ import absolute_import
import typing
from functools import partial
import WWISE, BattleReplay
from fun_random_common.fun_constants import UNKNOWN_WWISE_REMAPPING
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController
from shared_utils import nextTick
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers import BattleSessionSetup
    from gui.battle_control.controllers.sound_ctrls.common import SoundPlayer
    from skeletons.gui.battle_session import IClientArenaVisitor

class FunRandomBattleSoundController(SoundPlayersBattleController, FunSubModesWatcher):

    def __init__(self, setup):
        super(FunRandomBattleSoundController, self).__init__()
        self._remappingName = self._getRemappingName(setup.arenaVisitor)

    def startControl(self, *args):
        self._activateRemapping()
        super(FunRandomBattleSoundController, self).startControl()

    def stopControl(self):
        self._deactivateRemapping()
        super(FunRandomBattleSoundController, self).stopControl()

    def _initializeSoundPlayers(self):
        return ()

    def _activateRemapping(self):
        if self._remappingName and self._remappingName != UNKNOWN_WWISE_REMAPPING:
            WWISE.activateRemapping(self._remappingName)

    def _deactivateRemapping(self):
        if self._remappingName and self._remappingName != UNKNOWN_WWISE_REMAPPING:
            nextTick(partial(WWISE.deactivateRemapping, self._remappingName))()

    @hasBattleSubMode()
    def _getRemappingName(self, arenaVisitor=None):
        return self.getBattleSubMode(arenaVisitor).getSettings().client.wwiseRemapping


class FunRandomBattleReplaySoundController(FunRandomBattleSoundController):

    def startControl(self, *args):
        super(FunRandomBattleReplaySoundController, self).startControl(args)
        self.startSubSettingsListening(self.__onSubModesLoaded)

    def stopControl(self):
        self.stopSubSettingsListening(self.__onSubModesLoaded)
        super(FunRandomBattleReplaySoundController, self).stopControl()

    def _activateRemapping(self):
        if not BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            super(FunRandomBattleReplaySoundController, self)._activateRemapping()

    def _deactivateRemapping(self):
        if not BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            super(FunRandomBattleReplaySoundController, self)._deactivateRemapping()

    def _startPlayers(self):
        if self._remappingName is not None:
            super(FunRandomBattleReplaySoundController, self)._startPlayers()
        return

    def __onSubModesLoaded(self, *_):
        self._remappingName = self._getRemappingName()
        self._activateRemapping()
        self._startPlayers()


def createFunRandomBattleSoundsController(setup):
    if BattleReplay.g_replayCtrl.isPlaying:
        return FunRandomBattleReplaySoundController(setup)
    return FunRandomBattleSoundController(setup)
