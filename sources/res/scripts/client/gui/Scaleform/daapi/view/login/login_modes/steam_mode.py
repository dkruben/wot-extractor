# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/login/login_modes/steam_mode.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/steam_mode.py
from __future__ import absolute_import
import WGC
from gui import DialogsInterface
from gui.Scaleform.daapi.view.login.login_modes.base_wgc_mode import BaseWgcMode
from helpers import dependency
from skeletons.gameplay import IGameplayLogic

class SteamMode(BaseWgcMode):
    __gameplay = dependency.descriptor(IGameplayLogic)

    def __init__(self, view):
        super(SteamMode, self).__init__(view, None)
        return

    def onPopulate(self):
        if self.__checkWgcAvailable():
            super(SteamMode, self).onPopulate()

    def updateForm(self):
        if self._loginManager.wgcAvailable:
            self._view.as_showSteamLoginFormS({'userName': (WGC.getUserName())})
        else:
            self._view.as_showSteamLoginFormS({})

    def _onWgcError(self):
        self._loginManager.tryPrepareWGCLogin()
        self.__checkWgcAvailable()

    def __checkWgcAvailable(self):
        if not self._loginManager.wgcAvailable:
            DialogsInterface.showI18nInfoDialog('steamStartNeeded', self.__onDialogCallback)
            return False
        return True

    def __onDialogCallback(self, _):
        self.__gameplay.quitFromGame()
