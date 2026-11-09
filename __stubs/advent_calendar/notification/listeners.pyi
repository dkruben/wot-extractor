# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/notification/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import uuid as uuid
import BigWorld as BigWorld
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from account_helpers.AccountSettings import AdventCalendar as AdventCalendar
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME as ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME, MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION as MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState as DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.notifications.available_doors_view_model import State as AvailableDoorsNotificationState
from advent_calendar.gui.impl.lobby.feature.advent_helper import getAdventCalendarSetting as getAdventCalendarSetting, getDoorState as getDoorState, setAdventCalendarSetting as setAdventCalendarSetting
from advent_calendar.notification.decorators import DoorsAvailableDecorator as DoorsAvailableDecorator
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency, time_utils as time_utils
from notification.listeners import BaseReminderListener as BaseReminderListener
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE, NotificationData as NotificationData

class DoorsAvailableListener(BaseReminderListener):
    _adventController: Any
    _itemsCache: Any
    MSG_ID = 0
    _POPUP_NOTIFICATION_DELAY = 30
    _popUpNotificationCallbackID: Any
    _finalDayNotifier: Any
    def __init__(self):
        ...
    def start(self, model):
        ...
    def stop(self):
        ...
    def _createNotificationData(self, savedData, priorityLevel, **kwargs):
        ...
    def _createDecorator(self, data):
        ...
    def _tryNotify(self):
        ...
    def _notifyOrRemoveOrDelay(self, isAdding, isStateChanged=False, isDelayed=False, **ctx):
        ...
    def _getNotificationInfo(self, availableDoorsAmount):
        ...
    def _isFirstDayPostEvent(self):
        ...
    def _getFinalDayDelta(self):
        ...
    def _isLastDayPostEvent(self):
        ...
    def _cancelPopUpNotificationCallback(self):
        ...
    def _startFinalDayNotifier(self):
        ...
    def _stopFinalDayNotifier(self):
        ...
    def _getDelay(self):
        ...
    def _getNotificationName(self):
        ...
