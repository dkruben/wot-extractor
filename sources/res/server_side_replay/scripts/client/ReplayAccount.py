# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/ReplayAccount.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/ReplayAccount.py
from __future__ import absolute_import
import logging, enum, BigWorld, BattleReplay
from PlayerEvents import g_playerEvents
from ReplayEvents import g_replayEvents
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from external_strings_utils import unicode_from_utf8
import os
_logger = logging.getLogger(__name__)

class State(enum.IntEnum):
    PRE_START_REPLAY = 0
    STARTED_PLAYBACK = 1
    FINISHED_PLAYBACK = 2


class ReplayAccount(BigWorld.Entity):
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        self.state = State.PRE_START_REPLAY

    def onBecomePlayer(self):
        _logger.info('ReplayAccount.onBecomePlayer: state=%s', self.state)
        g_replayEvents.onReplayTerminated += self.__onReplayTerminated
        if self.state == State.PRE_START_REPLAY:
            self.__start()
        elif self.state == State.STARTED_PLAYBACK:
            self.__stop()

    def onBecomeNonPlayer(self):
        _logger.info('ReplayAccount.onBecomeNonPlayer')
        g_replayEvents.onReplayTerminated -= self.__onReplayTerminated

    def onKickedFromServer(self, reason, kickReasonType, expiryTime):
        _logger.info('ReplayAccount: onKickedFromServer: %s %d %d', reason, kickReasonType, expiryTime)
        self.connectionMgr.setKickedFromServer(reason, kickReasonType, expiryTime)

    def handleKeyEvent(self, *args, **kwargs):
        return False

    def __onReplayTerminated(self, reason):
        if reason != BigWorld.ReplayTerminatedReason.REPLAY_STOPPED_PLAYBACK:
            _logger.warning('Replay has finished abnormally, stopping')
            self.__stop()

    def __start(self):
        self.state = State.STARTED_PLAYBACK
        g_playerEvents.onServerReplayEntering()
        prefsFilePath = unicode_from_utf8(BigWorld.wg_getPreferencesFilePath())[1]
        filename = os.path.join(os.path.dirname(prefsFilePath), self.filename)
        if not BattleReplay.g_replayCtrl.play(filename):
            self.__stop()

    def __stop(self):
        self.state = State.FINISHED_PLAYBACK
        g_playerEvents.onServerReplayExiting()
        self.base.stopReplay()


PlayerReplayAccount = ReplayAccount
