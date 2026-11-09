# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/state_tracker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/state_tracker.py
from __future__ import absolute_import, print_function
import logging, operator
from gui.shared import g_eventBus, events
from shared_utils import safeForEach
from skeletons.gui.game_control import IGameStateTracker, IGameController
_logger = logging.getLogger(__name__)

class GameStateTracker(IGameStateTracker):

    def __init__(self):
        super(GameStateTracker, self).__init__()
        self._controllers = []

    def init(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)

    def fini(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)
        del self._controllers[:]

    def onAccountShowGUI(self, ctx):
        self.onLobbyStarted(ctx)

    def onConnected(self):
        self._invoke('onConnected')

    def onDisconnected(self):
        self._invoke('onDisconnected')

    def onAvatarBecomePlayer(self):
        self._invoke('onAvatarBecomePlayer')

    def onAccountBecomePlayer(self):
        self._invoke('onAccountBecomePlayer')

    def onAccountBecomeNonPlayer(self):
        self._invoke('onAccountBecomeNonPlayer')

    def onLobbyStarted(self, ctx):
        self._invoke('onLobbyStarted', ctx)

    def onLobbyInited(self, event):
        self._invoke('onLobbyInited', event)

    def onServerReplayEntering(self):
        self._invoke('onServerReplayEntering')

    def onServerReplayExiting(self):
        self._invoke('onServerReplayExiting')

    def addController(self, controller):
        if not isinstance(controller, IGameController):
            _logger.error('Controller should implements IGameController')
        self._controllers.append(controller)

    def removeController(self, controller):
        if not isinstance(controller, IGameController):
            _logger.error('Controller should implements IGameController')
        self._controllers.remove(controller)

    def _invoke(self, method, *args):
        safeForEach(operator.methodcaller(method, *args), self._controllers)
