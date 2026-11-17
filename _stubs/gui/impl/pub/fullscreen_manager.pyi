# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/fullscreen_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
from frameworks_common.state_machine.observers import StateIdsObserver as StateIdsObserver
from frameworks.wulf import WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.impl.gen import R as R
from gui.shared.system_factory import collectLowPriorityWindows as collectLowPriorityWindows, registerLowPriorityWulfWindows as registerLowPriorityWulfWindows
from helpers import dependency as dependency
from skeletons.gameplay import GameplayStateID as GameplayStateID, IGameplayLogic as IGameplayLogic
from skeletons.gui.impl import IGuiLoader as IGuiLoader, IFullscreenManager as IFullscreenManager, INotificationWindowController as INotificationWindowController
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow
from frameworks.wulf import Window as Window
_logger: Any
_LOW_PRIORITY_WINDOWS: tuple

class FullscreenManager(IFullscreenManager):
    __gui: Any
    __gameplay: Any
    __notificationMgr: Any
    __observer: Any
    __isEnabled: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def setEnabled(self, value):
        ...
    def __onWindowStatusChanged(self, uniqueID, newState):
        ...
    def __onWindowOpen(self, newWindow):
        ...
    @classmethod
    def __isParent(cls, pWindow, window):
        ...
    @staticmethod
    def __fullscreenPredicate(window):
        ...
    @staticmethod
    def __isAllowed(window):
        ...

class _LobbyStateObserver(StateIdsObserver):
    __gui: Any
    __manager: Any
    def __init__(self, manager):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
    def clear(self):
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...
