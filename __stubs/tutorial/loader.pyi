# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
import BigWorld as BigWorld
import account_helpers as account_helpers
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from tutorial.gui.Scaleform.gui_impl import ScaleformGuiImpl as ScaleformGuiImpl
from tutorial.gui.controller import GuiController as GuiController
from tutorial.gui.impl import WulfGuiImpl as WulfGuiImpl
from tutorial import core as core
from tutorial import settings as _settings
from tutorial import cache as _cache
from tutorial.control.context import GlobalStorage as GlobalStorage
from tutorial.control.listener import AppLoaderListener as AppLoaderListener
from tutorial.doc_loader import loadDescriptorData as loadDescriptorData
from tutorial.hints_manager import HintsManager as HintsManager
from soft_exception import SoftException as SoftException
from tutorial.core import Tutorial as Tutorial
from skeletons.tutorial import IGuiController as IGuiController
_SETTINGS = _settings.TUTORIAL_SETTINGS
_LOBBY_DISPATCHER = _settings.TUTORIAL_LOBBY_DISPATCHER
_BATTLE_DISPATCHER = _settings.TUTORIAL_BATTLE_DISPATCHER
_LOBBY_GUI_CONFIG = 'gui/tutorial-lobby-gui.xml'
_BATTLE_GUI_CONFIG = ''
_logger: Any

class RunCtx(object):
    __slots__: tuple
    cache: Any
    databaseID: Any
    restart: Any
    isFirstStart: Any
    isAfterBattle: Any
    bonusCompleted: Any
    battlesCount: Any
    newbieBattlesCount: Any
    initialChapter: Any
    globalFlags: Any
    canResolveChapterOnStart: Any
    byRequest: Any
    def __init__(self, cache, **kwargs):
        ...
    def __repr__(self):
        ...

class TutorialLoader(ITutorialLoader):
    __loggedDBIDs: Any
    __afterBattle: Any
    __tutorial: Any
    __dispatcher: Any
    __restoreID: Any
    __settings: Any
    __hintsManager: Any
    __listener: Any
    __guiController: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def tutorial(self):
        ...
    @property
    def tutorialID(self):
        ...
    @property
    def hintsManager(self):
        ...
    @property
    def isRunning(self):
        ...
    @property
    def gui(self):
        ...
    def isTutorialStopped(self):
        ...
    def run(self, settingsID, state=None):
        ...
    def stop(self, restore=True):
        ...
    def refuse(self):
        ...
    def goToLobby(self):
        ...
    def leaveLobby(self):
        ...
    def goToBattleLoading(self):
        ...
    def goToBattle(self):
        ...
    def leaveBattle(self):
        ...
    def goToLogin(self):
        ...
    def beforeEnterLobby(self):
        ...
    def beforeEnterBattle(self):
        ...
    def __doAutoRun(self, seq, state):
        ...
    def __doRun(self, settings, state):
        ...
    def __doStop(self):
        ...
    def __doStopHints(self):
        ...
    def __doClear(self):
        ...
    def __doRestore(self):
        ...
    def __setDispatcher(self, settings):
        ...
    def __onTutorialStopped(self):
        ...
    def __updateConditionalState(self, state):
        ...

def _getGuiImplementations():
    ...
