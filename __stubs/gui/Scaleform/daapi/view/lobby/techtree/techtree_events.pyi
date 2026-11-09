# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/techtree_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from future.utils import lmap as lmap, lfilter as lfilter
import nations as nations
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import TOP_OF_TREE_CONFIG as TOP_OF_TREE_CONFIG
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from helpers import dependency as dependency
from helpers.time_utils import ONE_DAY as ONE_DAY
from Event import Event as Event, EventManager as EventManager
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
from skeletons.gui.techtree_events import ITechTreeEventsListener as ITechTreeEventsListener
from gui.server_events.events_constants import TECH_TREE_ACTION_POSTFIX as TECH_TREE_ACTION_POSTFIX
from gui.Scaleform.daapi.view.lobby.store.actions_helpers import getActionInfoData as getActionInfoData
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
_GROUP_NAME_SEPARATOR = '!'
_NOTIFY_THRESHOLD: Any

class _SettingsCache(object):
    _NATIONS = 'nations'
    _NOTIFIED = 'notified'
    def update(self, actionIDs):
        ...
    def viewedNations(self):
        ...
    def selectNation(self, actionID, nationID):
        ...
    def isNotified(self, actionID):
        ...
    def setNotified(self, actionID):
        ...
    @staticmethod
    def _defaultValue():
        ...
    @staticmethod
    def _setSettings(actionID, value):
        ...
    @staticmethod
    def _getSettings(actionID=None):
        ...

class TechTreeEventsListener(ITechTreeEventsListener):
    __eventsCache: Any
    __itemsCache: Any
    __systemMessages: Any
    actions: Any
    __actions: Any
    __items: Any
    __settings: Any
    __em: Any
    onEventsUpdated: Any
    onSettingsChanged: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getUserName(self, actionID):
        ...
    def getVehicles(self, nationID=None):
        ...
    def setNationViewed(self, nationID):
        ...
    def getNations(self, unviewed=False, actionID=None):
        ...
    def getTimeTillEnd(self, actionID):
        ...
    def getFinishTime(self, actionID):
        ...
    def hasActiveAction(self, vehicleCD, nationID=None):
        ...
    def getActiveAction(self, vehicleCD=None, nationID=None):
        ...
    def __update(self):
        ...
    def __getVehicles(self, actionID, nationID=None):
        ...
    def __getNations(self, actionID):
        ...
    def __getUserName(self, actionID):
        ...
    def __getActualEventID(self, actionIDs):
        ...
    def __onAccountShowGUI(self, ctx):
        ...
    def __notifyAboutExpiration(self):
        ...
    def __actionNotifierCondition(self, actionID):
        ...
    def __getVehicleCDsWereInBattle(self):
        ...
    def __getActions(self, vehicleCD=None, nationID=None):
        ...
    def __onInventoryUpdated(self, _):
        ...
    @staticmethod
    def __eventFilter():
        ...
