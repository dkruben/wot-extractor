# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/achievements_earning_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from frameworks.wulf import WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow as SFWindow
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared.event_dispatcher import showAdvancedAchievementsRewardView as showAdvancedAchievementsRewardView
from helpers import dependency as dependency
from functools import partial as partial
from advanced_achievements_client.getters import getAchievementsEarnedBeforeTime as getAchievementsEarnedBeforeTime, getBonusTuples as getBonusTuples
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IAchievements20EarningController as IAchievements20EarningController, IAchievementsController as IAchievementsController, ILimitedUIController as ILimitedUIController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from typing import Optional as Optional, Generator as Generator, List as List, Tuple as Tuple
from advanced_achievements_client.items import _BaseGuiAchievement as _BaseGuiAchievement

class Achievements20EarningController(IAchievements20EarningController):
    __slots__: tuple
    __settingsCore: Any
    __lobbyContext: Any
    __advAchmntCtrl: Any
    __guiLoader: Any
    __RESTRICTED_LAYERS: set
    __ACTIVE_WINDOW_STATUSES: tuple
    __HIGH_PRIORITY_WINDOWS: tuple
    __HIGH_PRIORITY_WULF_WINDOWS: tuple
    __commandQueueManager: Any
    __commandBuilder: Any
    def __init__(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onDisconnected(self):
        ...
    def __stop(self):
        ...
    def __clearQueue(self):
        ...
    def __addFlowListeners(self):
        ...
    def __addControllerListeners(self):
        ...
    def __removeFlowListeners(self):
        ...
    def __removeControllerListeners(self):
        ...
    def __onWindowStatusChanged(self, _, newStatus):
        ...
    def __isEarningLockedByLayer(self):
        ...
    def __isEarningLockedByViews(self):
        ...
    # decorador original: @replace_none_kwargs(...)
    def __getDossierDescr(self, userId=None, itemsCache=None):
        ...
    def __diffToCommands(self):
        ...
    def __onAchievementsEarned(self, achievementsData):
        ...
    def __achievementsEarned(self, achievementsData):
        ...
    def fini(self):
        ...
    def pause(self):
        ...
    def resume(self):
        ...

class CommandQueueManager(object):
    __slots__: tuple
    __commandQueue: Any
    __commandChains: Any
    __currentCommand: Any
    __isPaused: Any
    def __init__(self):
        ...
    def pushChain(self, command):
        ...
    def executeNextCommand(self):
        ...
    def stop(self):
        ...
    def pause(self):
        ...
    def resume(self):
        ...

class CommandBuilder(object):
    __settingsCore: Any
    __advAchmntCtrl: Any
    __limitedUICtrl: Any
    def _isTrophy(self, achievementsData):
        ...
    def _isMultiple(self, achievementsData):
        ...
    def _getMultipleText(self, isMultiple):
        ...
    def _getTrophyText(self, isTrophy):
        ...
    def _getNewAchievementIterator(self, achievementsData):
        ...
    def _createAchievementDataDebugCommand(self, receiver, achievementData):
        ...
    def _createDebugMessageCommand(self, receiver, message):
        ...
    def _createTimeStampUpdateCommand(self, receiver, achievementsData):
        ...
    def _createNotificationCommand(self, receiver, achievementsData):
        ...
    def _createEarningAnimationCommand(self, receiver, achievementsData):
        ...
    def _createRewardScreenCommand(self, receiver, achievementsData):
        ...
    def createEarnAchievementChain(self, receiver, achievementsData):
        ...

class Command(object):
    __slots__: tuple
    __receiver: Any
    __isReleased: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...
    def release(self, *args, **kwargs):
        ...
    def isReleased(self):
        ...
    def stop(self):
        ...

class TimeStampUpdateCommand(Command):
    __slots__: tuple
    __settingsCore: Any
    __timestamp: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...

class PrintCommand(Command):
    __slots__: tuple
    __message: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...

class NotificationCommand(Command):
    __systemMessages: Any
    __slots__: tuple
    __header: Any
    __body: Any
    __isMultiple: Any
    __targetData: Any
    __isTrophy: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...

class EarningAnimationCommand(Command):
    __slots__: tuple
    __isTrophy: Any
    __isMultiple: Any
    __data: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...
    def stop(self):
        ...

class RewardScreenCommand(Command):
    __slots__: tuple
    __bonusTuples: Any
    def __init__(self, args):
        ...
    def execute(self):
        ...
