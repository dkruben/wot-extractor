# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/shared/event_dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import wraps as wraps
from logging import getLogger as getLogger
import typing as typing
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.impl.gen import R as R
from gui.impl.pub.notification_commands import WindowNotificationCommand as WindowNotificationCommand
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.scaleform.daapi.view.model.video_settings_model import getIntroVideoSettings as getIntroVideoSettings
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME, MissionId as MissionId
_logger: Any

class _ArenaLoadedChecker(IArenaLoadController):
    __slots__: tuple
    _sessionProvider: Any
    _isLoaded: Any
    def __init__(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def isLoaded(self):
        ...

def ifNotArenaLoaded(func):
    ...
def isViewLoaded(layoutID):
    ...
# decorador original: @ifNotArenaLoaded
def showIntro(missionId):
    ...
# decorador original: @ifNotArenaLoaded
def showIntroVideo(missionId):
    ...
def showOutroVideo(missionId, arenaUniqueID):
    ...
# decorador original: @ifNotArenaLoaded
# decorador original: @UseStoryModeFading(...)
def showPrebattleWindow(missionId):
    ...
# decorador original: @UseStoryModeFading(...)
def showPrebattleAndGoToQueue(missionId):
    ...
# decorador original: @UseStoryModeFading(...)
def showEpilogueWindow():
    ...
# decorador original: @UseStoryModeFading(...)
def showOnboardingBattleResultWindow(finishReason, missionId):
    ...
def showQueueWindow(isSkipButtonVisible=False):
    ...
# decorador original: @UseStoryModeFading(...)
def showCongratulationsWindow(isCloseVisible=False, onClose=None, awardData=None):
    ...
def showBattleResultWindow(arenaUniqueId):
    ...
def sendViewLoadedEvent(layoutID):
    ...
def showEventWelcomeWindow():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def showNewbieAdvertisingWindow(notificationMgr=None):
    ...
