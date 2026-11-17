# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/lobby_entry.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from frameworks.wulf import WindowLayer as WindowLayer
from frameworks.wulf.gui_constants import ShowingStatus as ShowingStatus, ViewFlags as ViewFlags
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.states import UntrackedState as UntrackedState
from gui.shared.events import NavigationEvent as NavigationEvent, GUICommonEvent as GUICommonEvent
from gui.shared.system_factory import collectLobbyTooltipsBuilders as collectLobbyTooltipsBuilders
from gui.Scaleform import SCALEFORM_SWF_PATH_V3 as SCALEFORM_SWF_PATH_V3
from gui.Scaleform.daapi.settings.config import ADVANCED_COMPLEX_TOOLTIPS as ADVANCED_COMPLEX_TOOLTIPS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.tooltip_mgr import ToolTip as ToolTip
from gui.Scaleform.framework.ui_logging_manager import UILoggerManager as UILoggerManager
from gui.Scaleform.framework.application import AppEntry as AppEntry
from gui.Scaleform.framework.managers import LoaderManager as LoaderManager, ContainerManager as ContainerManager
from gui.Scaleform.framework.managers.CacheManager import CacheManager as CacheManager
from gui.Scaleform.framework.managers.ImageManager import ImageManager as ImageManager
from gui.Scaleform.framework.managers.TutorialManager import ScaleformTutorialManager as ScaleformTutorialManager
from gui.Scaleform.framework.managers.containers import DefaultContainer as DefaultContainer
from gui.Scaleform.framework.managers.containers import PopUpContainer as PopUpContainer
from gui.Scaleform.framework.managers.context_menu import ContextMenuManager as ContextMenuManager
from gui.Scaleform.framework.managers.event_logging import EventLogManager as EventLogManager
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.framework.managers.optimization_manager import GraphicsOptimizationManager as GraphicsOptimizationManager
from gui.Scaleform.managers.ColorSchemeManager import ColorSchemeManager as ColorSchemeManager
from gui.Scaleform.managers.cursor_mgr import CursorManager as CursorManager
from gui.Scaleform.managers.GameInputMgr import GameInputMgr as GameInputMgr
from gui.Scaleform.managers.GlobalVarsManager import GlobalVarsManager as GlobalVarsManager
from gui.Scaleform.managers.PopoverManager import PopoverManager as PopoverManager
from gui.Scaleform.required_libraries_config import LOBBY_REQUIRED_LIBRARIES as LOBBY_REQUIRED_LIBRARIES
from gui.sounds.SoundManager import SoundManager as SoundManager
from gui.Scaleform.managers.TweenSystem import TweenManager as TweenManager
from gui.Scaleform.managers.UtilsManager import UtilsManager as UtilsManager
from gui.Scaleform.managers.voice_chat import LobbyVoiceChatManager as LobbyVoiceChatManager
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.subhangar.subhangar_observer import SubhangarObserver as SubhangarObserver
from helpers import uniprof as uniprof, dependency as dependency
from skeletons.gui.app_loader import GuiGlobalSpaceID as GuiGlobalSpaceID
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from logging import getLogger as getLogger
_logger: Any
_UntrackedStateForwardedParams: Any

class _UntrackedStateObserver(BaseStateObserver):
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...

class LobbyEntry(AppEntry):
    __stateMachine: Any
    __untrackedStateObserver: Any
    __subhangarObserver: Any
    def __init__(self, appNS, ctrlModeFlags):
        ...
    @property
    def stateMachine(self):
        ...
    @property
    def waitingManager(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def afterCreate(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def beforeDelete(self):
        ...
    def loadView(self, loadParams, *args, **kwargs):
        ...
    def _createLoaderManager(self):
        ...
    def _createContainerManager(self):
        ...
    def _createToolTipManager(self):
        ...
    def _createGlobalVarsManager(self):
        ...
    def _createSoundManager(self):
        ...
    def _createCursorManager(self):
        ...
    def _createColorSchemeManager(self):
        ...
    def _createEventLogMgr(self):
        ...
    def _createContextMenuManager(self):
        ...
    def _createPopoverManager(self):
        ...
    def _createVoiceChatManager(self):
        ...
    def _createUtilsManager(self):
        ...
    def _createTweenManager(self):
        ...
    def _createGameInputManager(self):
        ...
    def _createCacheManager(self):
        ...
    def _createImageManager(self):
        ...
    def _createUILoggerManager(self):
        ...
    def _createTutorialManager(self):
        ...
    def _createGraphicsOptimizationManager(self):
        ...
    def _setup(self):
        ...
    def _loadWaiting(self):
        ...
    def _getRequiredLibraries(self):
        ...
    def __initLSM(self, _):
        ...
    def __finiLSM(self):
        ...
    def __getWaitingFromContainer(self):
        ...

def getLobbyStateMachine():
    ...
