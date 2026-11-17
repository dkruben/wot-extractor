# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_notifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import FUN_RANDOM_NOTIFICATIONS as FUN_RANDOM_NOTIFICATIONS
from fun_random.gui.feature.fun_constants import FunNotificationSubModeState as FunNotificationSubModeState, FunTimersShifts as FunTimersShifts
from fun_random.gui.feature.models.notifications import FunNotificationCtx as FunNotificationCtx, FunNotification as FunNotification, FunStopSubModesNotification as FunStopSubModesNotification, FunNewSubModesNotification as FunNewSubModesNotification, FunNewProgressionNotification as FunNewProgressionNotification, FunSwitchOnSubModesNotification as FunSwitchOnSubModesNotification, FunSwitchOffSubModesNotification as FunSwitchOffSubModesNotification
from fun_random.gui.feature.util.fun_wrappers import ifNotificationsAllowed as ifNotificationsAllowed, ifNotificationsEnabled as ifNotificationsEnabled, skipNoSubModesAction as skipNoSubModesAction
from gui.impl.gen import R as R
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from fun_random.gui.fun_gui_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode
from fun_random.helpers.server_settings import FunRandomConfig as FunRandomConfig
_NOTIFICATIONS_AGGREGATORS: tuple
_NOTIFICATIONS_BUILDERS: tuple

class FunNotifications(IFunRandomController.IFunNotifications, Notifiable):
    __gui: Any
    __systemMessages: Any
    __isNotificationsAllowed: Any
    __notificationsQueue: Any
    __subModesStates: Any
    __funRandomSettings: Any
    __progressions: Any
    __subModes: Any
    def __init__(self, progressions, subModesHolder):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def isNotificationsAllowed(self):
        ...
    def isNotificationsEnabled(self):
        ...
    def addToQueue(self, notification):
        ...
    # decorador original: @skipNoSubModesAction
    def markSeenAsFrozen(self, subModesIDs):
        ...
    # decorador original: @ifNotificationsEnabled
    # decorador original: @ifNotificationsAllowed(...)
    def pushNotification(self, notification):
        ...
    def startNotificationPushing(self):
        ...
    def stopNotificationPushing(self):
        ...
    def updateSettings(self, settings):
        ...
    def __isModeSelectorOpen(self):
        ...
    def __getNotificationsTimer(self):
        ...
    def __clearNotificationsQueue(self):
        ...
    def __defineSubModesStates(self):
        ...
    def __processNotifications(self):
        ...
    def __processNotificationsQueue(self):
        ...
    # decorador original: @ifNotificationsEnabled
    # decorador original: @ifNotificationsAllowed(...)
    def __pushNotification(self, notification):
        ...

def _modeSelectorPredicate(view):
    ...
def _defineSubModeState(subMode, now):
    ...
