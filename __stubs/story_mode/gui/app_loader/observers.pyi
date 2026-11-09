# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/app_loader/observers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.app_loader.observers import BattleLoadingObserver as BattleLoadingObserver, registerBattleObserverOverrideHandler as registerBattleObserverOverrideHandler, SwitchToBattleObserver as SwitchToBattleObserver, BattlePageObserver as BattlePageObserver, SwitchToLobbyObserver as SwitchToLobbyObserver
from helpers import dependency as dependency
from skeletons.gameplay import GameplayStateID as GameplayStateID
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS, IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON as IS_ONBOARDING_SEAMLESS_MISSION_CHANGING_ON
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from gui.Scaleform.framework.application import AppEntry as AppEntry
from story_mode.gui.scaleform.daapi.view.battle.page_base import StoryModeBattlePageBase as StoryModeBattlePageBase

class StoryModeSwitchToBattleObserver(SwitchToBattleObserver):
    __slots__: tuple
    _storyModeCtrl: Any
    def _destroyLobby(self):
        ...
    def _createBattle(self, arenaGuiType):
        ...

class StoryModeBattlePageObserver(BattlePageObserver):
    __slots__: tuple
    _storyModeCtrl: Any
    def onExitState(self, state, event):
        ...

class StoryModeSwitchToLobbyObserver(SwitchToLobbyObserver):
    __slots__: tuple
    _storyModeCtrl: Any
    def _createLobby(self):
        ...

class StoryModeObserverPredicate(object):
    __slots__: tuple
    _storyModeCtrl: Any
    def __call__(self, *_, **__):
        ...

def getStoryModeBattle():
    ...
def isInStoryModeBattle():
    ...
def registerObservers(proxy):
    ...
def preInit():
    ...
