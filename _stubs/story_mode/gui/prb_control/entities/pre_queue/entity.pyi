# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import QUEUE_TYPE as QUEUE_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.prb_control.entities.base.pre_queue.ctx import DequeueCtx as DequeueCtx
from gui.prb_control.entities.base.pre_queue.entity import PreQueueSubscriber as PreQueueSubscriber, PreQueueEntryPoint as PreQueueEntryPoint, PreQueueEntity as PreQueueEntity
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.settings import REQUEST_TYPE as REQUEST_TYPE
from gui.prb_control.storages import storage_getter as storage_getter, RECENT_PRB_STORAGE as RECENT_PRB_STORAGE
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from story_mode.gui.impl.battle.prebattle_window import getOpenedPrebattleView as getOpenedPrebattleView
from story_mode.gui.prb_control.entities.pre_queue import tasksAvailableCheck as tasksAvailableCheck
from story_mode.gui.prb_control.entities.pre_queue.actions_validator import StoryModeActionsValidator as StoryModeActionsValidator
from story_mode.gui.prb_control.entities.pre_queue.ctx import StoryModeQueueCtx as StoryModeQueueCtx
from story_mode.gui.prb_control.entities.pre_queue.permissions import StoryModePermissions as StoryModePermissions
from story_mode.gui.shared.event_dispatcher import showQueueWindow as showQueueWindow
from story_mode.gui.shared.utils import waitForLobby as waitForLobby
from story_mode.gui.story_mode_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from wg_async import wg_async as wg_async, wg_await as wg_await

class StoryModeEntryPoint(PreQueueEntryPoint):
    def __init__(self):
        ...

class StoryModeEntity(PreQueueEntity):
    storyModeCtrl: Any
    lobbyContext: Any
    uiLoader: Any
    _queueWindow: Any
    _modeFlags: Any
    _requestCtx: Any
    def __init__(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    # decorador original: @storage_getter(...)
    def storage(self):
        ...
    def canDoActionWithoutVehicle(self):
        ...
    def init(self, ctx=None):
        ...
    def doAction(self, action=None):
        ...
    def onEnqueued(self, *args):
        ...
    def exitFromQueue(self):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def doSelectAction(self, action):
        ...
    def getConfirmDialogMeta(self, ctx):
        ...
    # decorador original: @tasksAvailableCheck
    def queue(self, ctx, callback=None):
        ...
    # decorador original: @wg_async
    def _loadHangar(self):
        ...
    @property
    def _guiCtx(self):
        ...
    @property
    def _skippedShowGUI(self):
        ...
    @property
    def _accountComponent(self):
        ...
    def _doQueue(self, ctx):
        ...
    def _doDequeue(self, ctx):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _createActionsValidator(self):
        ...
    def getPermissions(self, *_, **__):
        ...
    def _validateParentControl(self):
        ...
