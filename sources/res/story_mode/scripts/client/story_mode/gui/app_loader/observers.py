# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/app_loader/observers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/app_loader/observers.py
from __future__ import absolute_import
import typing
from gui.Scaleform.framework.entities.View import ViewKey
from gui.app_loader.observers import BattleLoadingObserver, registerBattleObserverOverrideHandler, SwitchToBattleObserver, BattlePageObserver, SwitchToLobbyObserver
from helpers import dependency
from skeletons.gameplay import GameplayStateID
from skeletons.gui.app_loader import IAppLoader
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS, IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON
from story_mode.skeletons.story_mode_controller import IStoryModeController
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.application import AppEntry
    from story_mode.gui.scaleform.daapi.view.battle.page_base import StoryModeBattlePageBase

def getStoryModeBattle():
    appLoader = dependency.instance(IAppLoader)
    app = appLoader.getApp()
    if app is None:
        return
    else:
        containerManager = app.containerManager
        if containerManager is None:
            return
        return containerManager.getViewByKey(ViewKey(VIEW_ALIAS.ONBOARDING_BATTLE_PAGE)) or containerManager.getViewByKey(ViewKey(VIEW_ALIAS.STORY_MODE_BATTLE_PAGE))


def isInStoryModeBattle():
    return getStoryModeBattle() is not None


class StoryModeSwitchToBattleObserver(SwitchToBattleObserver):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def _destroyLobby(self):
        if not self._storyModeCtrl.isOnboarding or self._proxy.getDefLobbyApp() is not None:
            super(StoryModeSwitchToBattleObserver, self)._destroyLobby()
        return

    def _createBattle(self, arenaGuiType):
        if not self._storyModeCtrl.isOnboarding or self._proxy.getDefBattleApp() is None:
            super(StoryModeSwitchToBattleObserver, self)._createBattle(arenaGuiType)
        return


class StoryModeBattlePageObserver(BattlePageObserver):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def onExitState(self, state, event):
        if not self._storyModeCtrl.isOnboarding or self._storyModeCtrl.isQuittingBattle:
            super(StoryModeBattlePageObserver, self).onExitState(state, event)
        else:
            battlePage = getStoryModeBattle()
            if battlePage is not None:
                battlePage.hideAndStop()
        return


class StoryModeSwitchToLobbyObserver(SwitchToLobbyObserver):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def _createLobby(self):
        if not self._storyModeCtrl.isOnboarding or self._storyModeCtrl.isQuittingBattle:
            super(StoryModeSwitchToLobbyObserver, self)._createLobby()


class StoryModeObserverPredicate(object):
    __slots__ = ()
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def __call__(self, *_, **__):
        return self._storyModeCtrl.isEnabled() and isInStoryModeBattle()


def registerObservers(proxy):
    return (
     StoryModeObserverPredicate(),
     (
      StoryModeSwitchToBattleObserver(GameplayStateID.AVATAR_ENTERING, proxy),
      BattleLoadingObserver(GameplayStateID.AVATAR_ARENA_INFO, proxy),
      BattleLoadingObserver(GameplayStateID.AVATAR_SHOW_GUI, proxy),
      StoryModeBattlePageObserver(GameplayStateID.AVATAR_ARENA_LOADED, proxy),
      StoryModeSwitchToLobbyObserver(GameplayStateID.ACCOUNT_ENTERING, GameplayStateID.AVATAR_EXITING, proxy)))


def preInit():
    if IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON:
        registerBattleObserverOverrideHandler(registerObservers)
