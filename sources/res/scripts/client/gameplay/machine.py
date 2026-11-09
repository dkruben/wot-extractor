# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gameplay/machine.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gameplay/machine.py
from __future__ import absolute_import
import logging, BattleReplay
from constants import HAS_DEV_RESOURCES
from frameworks_common.state_machine import StateMachine
from gameplay import states
from gameplay.observers import BlockingStateClearObserver
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

class GameplayStateMachine(StateMachine):
    __slots__ = ()

    def start(self, doValidate=True):
        self.connect(BlockingStateClearObserver())
        super(GameplayStateMachine, self).start(doValidate)

    @property
    def offline(self):
        return self.getChildByIndex(0)

    @property
    def online(self):
        return self.getChildByIndex(1)

    def configure(self):
        offline = states.OfflineState()
        offline.configure()
        online = states.OnlineState()
        online.configure(offline)
        self.addState(offline)
        self.addState(online)


class BattleReplayMachine(StateMachine):
    __slots__ = ()

    def configure(self):
        initialization = states.BattleReplayInitState()
        initialization.configure()
        playing = states.BattleReplayPlayingState()
        playing.configure(initialization)
        self.addState(initialization)
        self.addState(playing)


def create():
    if BattleReplay.g_replayCtrl.getAutoStartFileName():
        return BattleReplayMachine()
    if HAS_DEV_RESOURCES:
        try:
            from gui.development.dev_gameplay import DevGameplayStateMachine
        except ImportError:
            _logger.exception('Development state machine is not found')
            return GameplayStateMachine()

        return DevGameplayStateMachine()
    return GameplayStateMachine()
