# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gameplay/listeners.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gameplay/listeners.py
from __future__ import absolute_import
import weakref, BigWorld
from PlayerEvents import g_playerEvents
from constants import ARENA_GUI_TYPE
from frameworks_common.state_machine.events import StringEvent
from skeletons.gameplay import PlayerEventID, ReplayEventID

class PlayerEventsAdaptor(object):
    __slots__ = ('_machine', )

    def __init__(self, machine):
        super(PlayerEventsAdaptor, self).__init__()
        self._machine = weakref.proxy(machine)

    def startListening(self):
        g_playerEvents.onAccountBecomePlayer += self.__onAccountBecomePlayer
        g_playerEvents.onAccountBecomeNonPlayer += self.__onAccountBecomeNonPlayer
        g_playerEvents.onAvatarBecomePlayer += self.__onAvatarBecomePlayer
        g_playerEvents.onAvatarBecomeNonPlayer += self.__onAvatarBecomeNonPlayer
        g_playerEvents.onServerReplayEntering += self.__onServerReplayEntering
        g_playerEvents.onServerReplayExiting += self.__onServerReplayExiting

    def stopListening(self):
        g_playerEvents.onAccountBecomePlayer -= self.__onAccountBecomePlayer
        g_playerEvents.onAccountBecomeNonPlayer -= self.__onAccountBecomeNonPlayer
        g_playerEvents.onAvatarBecomePlayer -= self.__onAvatarBecomePlayer
        g_playerEvents.onAvatarBecomeNonPlayer -= self.__onAvatarBecomeNonPlayer
        g_playerEvents.onServerReplayEntering -= self.__onServerReplayEntering
        g_playerEvents.onServerReplayExiting -= self.__onServerReplayExiting

    def __onAccountBecomePlayer(self):
        self._machine.post(StringEvent(PlayerEventID.ACCOUNT_BECOME_PLAYER))

    def __onAccountBecomeNonPlayer(self):
        self._machine.post(StringEvent(PlayerEventID.ACCOUNT_BECOME_NON_PLAYER))

    def __onAvatarBecomePlayer(self):
        self._machine.post(StringEvent(PlayerEventID.AVATAR_BECOME_PLAYER, arenaGuiType=getattr(BigWorld.player(), 'arenaGuiType', ARENA_GUI_TYPE.UNKNOWN)))

    def __onAvatarBecomeNonPlayer(self):
        self._machine.post(StringEvent(PlayerEventID.AVATAR_BECOME_NON_PLAYER))

    def __onServerReplayEntering(self):
        self._machine.post(StringEvent(ReplayEventID.SERVER_REPLAY_ENTERING))

    def __onServerReplayExiting(self):
        self._machine.post(StringEvent(ReplayEventID.SERVER_REPLAY_EXITING))
