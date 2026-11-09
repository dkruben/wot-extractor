# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/tutorial/control/listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/listener.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader, GuiGlobalSpaceID

class AppLoaderListener(object):
    appLoader = dependency.descriptor(IAppLoader)

    def __init__(self):
        super(AppLoaderListener, self).__init__()
        self.__loader = None
        return

    def start(self, loader):
        self.__loader = loader
        self.appLoader.onGUISpaceEntered += self.__onGUISpaceEntered
        self.appLoader.onGUISpaceLeft += self.__onGUISpaceLeft
        self.appLoader.onGUISpaceBeforeEnter += self.__onGUISpaceBeforeEnter

    def stop(self):
        self.appLoader.onGUISpaceEntered -= self.__onGUISpaceEntered
        self.appLoader.onGUISpaceLeft -= self.__onGUISpaceLeft
        self.appLoader.onGUISpaceBeforeEnter -= self.__onGUISpaceBeforeEnter

    def __onGUISpaceEntered(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOGIN:
            self.__loader.goToLogin()
        elif spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.goToLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE_LOADING:
            self.__loader.goToBattleLoading()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.goToBattle()

    def __onGUISpaceLeft(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.leaveLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.leaveBattle()

    def __onGUISpaceBeforeEnter(self, spaceID):
        if spaceID == GuiGlobalSpaceID.LOBBY:
            self.__loader.beforeEnterLobby()
        elif spaceID == GuiGlobalSpaceID.BATTLE:
            self.__loader.beforeEnterBattle()
