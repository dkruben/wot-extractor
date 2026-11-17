# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/restore_contoller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
import time as time
from operator import itemgetter as itemgetter
import BigWorld as BigWorld
import Event as Event
from account_helpers.AccountSettings import AccountSettings as AccountSettings, LAST_RESTORE_NOTIFICATION as LAST_RESTORE_NOTIFICATION
from gui import SystemMessages as SystemMessages
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import MONEY_UNDEFINED as MONEY_UNDEFINED
from gui.shared.utils.requesters.ItemsRequester import IntCDProtectionRequestCriteria as IntCDProtectionRequestCriteria
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache
DEFAULT_MAX_TANKMEN_BUFFER_LENGTH = 100

class RestoreController(IRestoreController, Notifiable):
    itemsCache: Any
    __eventManager: Any
    __restoreNotifyTimeCallback: Any
    __vehiclesForUpdate: Any
    __tankmenList: Any
    __tankmanLiveTime: Any
    __maxTankmenBufferLength: Any
    __checkForNotify: Any
    __waitNextUpdate: Any
    onRestoreChangeNotify: Any
    onTankmenBufferUpdated: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def onLobbyInited(self, _):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def fini(self):
        ...
    def getMaxTankmenBufferLength(self):
        ...
    def getDismissedTankmen(self):
        ...
    def getTankmenBeingDeleted(self, newTankmenCount=1):
        ...
    def getTankmenDeletedBySelling(self, *vehicles):
        ...
    def _stop(self):
        ...
    def _update(self, _, invalidItems):
        ...
    def __startRestoreTimeNotifyCallback(self):
        ...
    def __notifyRestoreTime(self):
        ...
    def __clearRestoreTimeNotifyCallback(self):
        ...
    def __updateTankmenList(self):
        ...
    def __getClosestTankmanUpdateTime(self):
        ...
    def __checkLimitedRestoreNotification(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getTankmenRestoreInfo(tankman, itemsCache=None):
    ...
def _hasLimitedRestore(item):
    ...
def _doRestoreFilter(item):
    ...
