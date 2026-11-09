# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from uilogging.player_satisfaction_rating.loggers import InviteToPlatoonLogger

class StatsBase(StatsBaseMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(StatsBase, self).__init__()
        self._logger = InviteToPlatoonLogger()

    @property
    def hasTabs(self):
        return False

    def acceptSquad(self, sessionID):
        self.sessionProvider.invitations.accept(sessionID)

    def addToSquad(self, sessionID, source):
        self._logger.logPlatoonInvite(source)
        self.sessionProvider.invitations.send(sessionID)

    def onToggleVisibility(self, isVisible):
        self._onToggleVisibility(isVisible)

    def _populate(self):
        self.addListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._populate()

    def _dispose(self):
        self.__invitations = None
        self.removeListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._dispose()
        return

    def _onToggleVisibility(self, isVisible):
        pass

    def __handleShowCursor(self, _):
        self.as_setIsInteractiveS(True)

    def __handleHideCursor(self, _):
        self.as_setIsInteractiveS(False)
