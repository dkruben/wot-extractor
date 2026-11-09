# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/screencast_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/screencast_controller.py
from __future__ import absolute_import
import BigWorld
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.shared.utils import getPlayerDatabaseID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.game_control import IScreenCastController

class ScreenCastController(IScreenCastController, IArenaVehiclesController):
    __slots__ = ('_isSet', '_isBattleCtrlInit', '_dbID')
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(ScreenCastController, self).__init__()
        self._isSet = False
        self._isBattleCtrlInit = False
        self._dbID = 0

    def fini(self):
        if self._isBattleCtrlInit:
            self.sessionProvider.removeArenaCtrl(self)

    def onAvatarBecomePlayer(self):
        if not self._isBattleCtrlInit:
            self.sessionProvider.addArenaCtrl(self)
            self._isBattleCtrlInit = True
            self.__checkDbID()

    def onAccountBecomePlayer(self):
        if self._isBattleCtrlInit:
            self.sessionProvider.removeArenaCtrl(self)
            self._isBattleCtrlInit = False

    def invalidateArenaInfo(self):
        self.__checkDbID()

    def invalidateVehiclesInfo(self, _):
        self.__checkDbID()

    def onLobbyInited(self, event):
        self.__checkDbID()

    def onDisconnected(self):
        self._dbID = 0
        self._isSet = False
        BigWorld.Screener.setUserId(0)

    def __checkDbID(self):
        if self._dbID == 0:
            self._dbID = getPlayerDatabaseID()
            self.__update()

    def __update(self):
        if self._dbID != 0 and not self._isSet:
            BigWorld.Screener.setUserId(self._dbID)
            self._isSet = True
