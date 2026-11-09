# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/rq_cooldown.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
from debug_utils import LOG_WARNING as LOG_WARNING
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as I18N_SYSTEM_MESSAGES
from gui.impl import backport as backport
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import i18n as i18n
DEFAULT_COOLDOWN_TO_REQUEST = 5.0
_REQUEST_SCOPE_TO_EVENT: dict
_g_coolDowns: dict

class REQUEST_SCOPE(object):
    GLOBAL = 0
    PRB_CONTROL = 1
    FORTIFICATION = 2
    BW_CHAT2 = 3
    XMPP = 4
    BATTLE_CONTROL = 5
    WGCG = 6
    STRONGHOLD = 7
    BATTLE_ACTION = 8
    WGNP = 8

class RequestCooldownManager(object):
    _scopeID: Any
    __commonCooldown: Any
    _lastRqTime: Any
    def __init__(self, scopeID, commonCooldown=0.0):
        ...
    def getCommonCooldown(self):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...
    def isInProcess(self, rqTypeID):
        ...
    def getTime(self, rqTypeID):
        ...
    def getCoolDownMessage(self, rqTypeID, coolDown=None):
        ...
    def process(self, rqTypeID, coolDown=None):
        ...
    def adjust(self, rqTypeID, coolDown=None):
        ...
    def reset(self, rqTypeID):
        ...
    def validate(self, rqTypeID, coolDown=None):
        ...
    def fireEvent(self, rqTypeID, coolDown=None):
        ...
    def _showSysMessage(self, msg):
        ...
    def __getCommonCooldownTimeLeft(self):
        ...

def isRequestInCoolDown(scopeID, rqTypeID):
    ...
def getRequestCoolDown(scopeID, rqTypeID):
    ...
def getRequestInCoolDownMessage(requestName, coolDown=...):
    ...
def setRequestCoolDown(scopeID, rqTypeID, coolDown=...):
    ...
def adjustRequestCoolDown(scopeID, rqTypeID, coolDown=...):
    ...
def fireCoolDownEvent(scopeID, rqTypeID, coolDown=...):
    ...
