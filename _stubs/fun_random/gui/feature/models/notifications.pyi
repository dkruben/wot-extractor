# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import typing as typing
from account_helpers.AccountSettings import FUN_RANDOM_NOTIFICATIONS_FROZEN as FUN_RANDOM_NOTIFICATIONS_FROZEN, FUN_RANDOM_NOTIFICATIONS_SUB_MODES as FUN_RANDOM_NOTIFICATIONS_SUB_MODES, FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS as FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS
from fun_random.gui.feature.fun_constants import FunNotificationSubModeState as FunNotificationSubModeState, FunNotificationType as FunNotificationType
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from fun_random.gui.feature.models.progressions import FunProgression as FunProgression
from skeletons.gui.game_control import IFunRandomController as IFunRandomController

class FunNotificationCtx(object):
    __slots__: tuple
    isInFunRandom: Any
    progression: Any
    subModes: Any
    transactions: Any
    newStates: Any
    settings: Any
    def __init__(self, isInFunRandom, subModes, progression, transactions, newStates, settings):
        ...

# decorador original: @ReprInjector.simple(...)
class FunNotification(object):
    __slots__: tuple
    notificationType: Any
    def __init__(self, notificationType):
        ...
    @classmethod
    def aggregateNotifications(cls, notifications):
        ...
    @classmethod
    def buildNotifications(cls, ctx):
        ...
    @classmethod
    def updateStoredSubModes(cls, subModes, subModesIDs, settings, isRemove=False, isFrozen=False):
        ...
    @classmethod
    def _isNewProgression(cls, ctx):
        ...
    @classmethod
    def _getSettingsKeys(cls, subModes, subModesIDs):
        ...
    @classmethod
    def _markProgressionAsSeen(cls, progression, settings):
        ...

# decorador original: @ReprInjector.withParent(...)
class FunStopSubModesNotification(FunNotification):
    __slots__: tuple
    _FINISH_STATES: tuple
    _STOP_NOTIFICATIONS: tuple
    _PROGRESSION_NOTIFICATION = FunNotificationType.NEW_PROGRESSION
    isNewProgression: Any
    subModesIDs: Any
    def __init__(self, notificationType, subModesIDs=..., isNewProgression=False):
        ...
    @classmethod
    def aggregateNotifications(cls, notifications):
        ...
    @classmethod
    def buildNotifications(cls, ctx):
        ...

# decorador original: @ReprInjector.withParent(...)
class FunNewSubModesNotification(FunNotification):
    __slots__: tuple
    _PROGRESSION_NOTIFICATION = FunNotificationType.NEW_PROGRESSION
    _NEW_STATES: tuple
    _NEW_NOTIFICATION = FunNotificationType.NEW_SUB_MODES
    isNewProgression: Any
    subModesIDs: Any
    def __init__(self, notificationType, subModesIDs=..., isNewProgression=False):
        ...
    @classmethod
    def aggregateNotifications(cls, notifications):
        ...
    @classmethod
    def buildNotifications(cls, ctx):
        ...

class FunNewProgressionNotification(FunNotification):
    @classmethod
    def buildNotifications(cls, ctx):
        ...

# decorador original: @ReprInjector.withParent(...)
class FunSwitchOnSubModesNotification(FunNotification):
    __slots__: tuple
    _AVAILABLE_STATE = FunNotificationSubModeState.AVAILABLE
    subModesIDs: Any
    def __init__(self, notificationType, subModesIDs=...):
        ...
    @classmethod
    def buildNotifications(cls, ctx):
        ...

# decorador original: @ReprInjector.withParent(...)
class FunSwitchOffSubModesNotification(FunNotification):
    __slots__: tuple
    _AVAILABLE_STATE = FunNotificationSubModeState.AVAILABLE
    _FROZEN_STATE = FunNotificationSubModeState.FROZEN
    subModesIDs: Any
    def __init__(self, notificationType, subModesIDs=...):
        ...
    @classmethod
    def buildNotifications(cls, ctx):
        ...
