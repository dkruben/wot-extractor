# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/predefined_hosts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
import random as random
import time as time
import threading as threading
from collections import namedtuple as namedtuple
from future.moves.urllib import parse as parse
from future.moves.urllib import request as request
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import ResMgr as ResMgr
import constants as constants
from Event import Event as Event, EventManager as EventManager
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from shared_utils import BitmaskHelper as BitmaskHelper
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING, LOG_NOTE as LOG_NOTE
from helpers import i18n as i18n
AUTO_LOGIN_QUERY_ENABLED: Any
AUTO_LOGIN_QUERY_URL = 'auto.login.app:0000'
AUTO_LOGIN_QUERY_TIMEOUT = 5
CSIS_REQUEST_TIMEOUT = 10
CSIS_REQUEST_TIMER: Any
_PING_FORCE_COOLDOWN_TIME = ONE_MINUTE
_PING_COOLDOWN_TIME: Any
UNDEFINED_PING_VAL = -1
_DEFINED_PING_VAL = 0
_LOW_PING_BOUNDARY_VAL = 59
_NORM_PING_BOUNDARY_VAL = 119
PingData: Any
_DEFAULT_PING_DATA: Any
_csisQueryMutex: Any
_HostItem: Any
g_preDefinedHosts: Any

class PING_STATUSES(object):
    UNDEFINED = 0
    HIGH = 1
    NORM = 2
    LOW = 3
    REQUESTED = 4

class HOST_AVAILABILITY(object):
    NOT_AVAILABLE = -1
    NOT_RECOMMENDED = 0
    RECOMMENDED = 1
    REQUESTED = 2
    IGNORED = 3
    UNKNOWN = 4

class REQUEST_RATE(object):
    NEVER = 0
    ON_REQUEST = 1
    ALWAYS = 2

class AUTO_LOGIN_QUERY_STATE(object):
    DEFAULT = 0
    START = 1
    PING_PERFORMED = 2
    CSIS_RESPONSE_RECEIVED = 4
    COMPLETED: Any

class CSIS_ACTION(BitmaskHelper):
    DEFAULT = 0
    UPDATE_ON_TIME = 1
    AUTO_LOGIN_REQUEST = 2

class _CSISRequestWorker(threading.Thread):
    __url: Any
    __callback: Any
    __params: Any
    def __init__(self, url, callback, params=None):
        ...
    def run(self):
        ...
    def _makeUrl(self):
        ...

class _LoginAppUrlIterator(list):
    cursor: Any
    primary: Any
    __lock: Any
    def __init__(self, *args):
        ...
    def end(self):
        ...
    def suspend(self):
        ...
    def resume(self):
        ...
    def nextUrl(self):
        ...

class _PingRequester(object):
    __pingResult: Any
    __pingPerformedCallback: Any
    __isRequestPingInProgress: Any
    __lastUpdateTime: Any
    __setPingCallback: Any
    def __init__(self, pingPerformedCallback):
        ...
    def request(self, peripheries, forced=False):
        ...
    def result(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def __pingCallback(self, result):
        ...
    def __updatePing(self, pingData, state=None):
        ...

class _PreDefinedHostList(object):
    _eManager: Any
    onCsisQueryStart: Any
    onCsisQueryComplete: Any
    onPingPerformed: Any
    _hosts: Any
    _urlMap: Any
    _nameMap: Any
    _peripheryMap: Any
    _isDataLoaded: Any
    _isCSISQueryInProgress: Any
    __csisUrl: Any
    __csisResponse: Any
    __lastRoamingHosts: Any
    __csisCallbackID: Any
    __lastCsisUpdateTime: Any
    __queryCallback: Any
    __autoLoginQueryState: Any
    __csisAction: Any
    __recommended: Any
    __pingRequester: Any
    __availablePeripheriesByRoutingGroup: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    @property
    def lastRoamingHosts(self):
        ...
    def startCSISUpdate(self):
        ...
    def stopCSISUpdate(self):
        ...
    def requestPing(self, forced=False):
        ...
    def getPingResult(self):
        ...
    def getHostPingData(self, host):
        ...
    def autoLoginQuery(self, callback):
        ...
    def resetQueryResult(self):
        ...
    def readScriptConfig(self, dataSection, userDataSection=None):
        ...
    def predefined(self, url):
        ...
    def roaming(self, url):
        ...
    def first(self):
        ...
    def byUrl(self, url):
        ...
    def byName(self, name):
        ...
    def hosts(self):
        ...
    def shortList(self):
        ...
    def getSimpleHostsList(self, hosts, withShortName=False):
        ...
    def getDefaultCSISStatus(self):
        ...
    def urlIterator(self, primary):
        ...
    def periphery(self, peripheryID, useRoaming=True):
        ...
    def peripheries(self):
        ...
    def roamingHosts(self):
        ...
    def hostsWithRoaming(self):
        ...
    def isRoamingPeriphery(self, peripheryID):
        ...
    def setAvailablePeripheriesByRoutingGroup(self, availablePeripheries):
        ...
    def _makeHostItem(self, name, shortName, url, urlToken='', urlIterator=None, keyPath=None, areaID=None, peripheryID=0):
        ...
    def _determineRecommendHost(self):
        ...
    def __startCsisTimer(self):
        ...
    def __cleanCsisTimerCallback(self):
        ...
    def __onCsisTimer(self):
        ...
    def __sendCsisQuery(self):
        ...
    def __receiveCsisResponse(self, response):
        ...
    def __finishCsisQuery(self):
        ...
    def __onPingPerformed(self, result):
        ...
    def __receiveAutoLoginCSISResponse(self, response):
        ...
    def __autoLoginQueryCompleted(self, state):
        ...
    def __filterRecommendedByPing(self, recommended):
        ...
    def __choiceFromRecommended(self):
        ...

def _getPingStatus(pingVal):
    ...
def _isReplay(opType=''):
    ...
def _CSISResponseParser(out, requestedIDs):
    ...
def _createDefaultCSISResponse(requestedIDs):
    ...
def _getCSISWorker(csisUrl, receiveCsisResponse, peripheries):
    ...
def getHostURL(item, token2=None, useIterator=False):
    ...
