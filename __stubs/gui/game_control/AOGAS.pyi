# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/AOGAS.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import weakref as weakref
from builtins import round as round
import BigWorld as BigWorld
import Event as Event
from constants import AOGAS_TIME as AOGAS_TIME, ACCOUNT_ATTR as ACCOUNT_ATTR
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from enumerations import AttributeEnumItem as AttributeEnumItem, Enumeration as Enumeration
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IAOGASController as IAOGASController
TIME_MODIFER = 3600
AOGAS_FORCE_START_NOTIFY = False
_DEFAULT_AOGAS_NOTIFY_TIMEOUT = 5000.0
AOGAS_NOTIFY_MSG: Any

class AOGAS_NOTIFY_TIME(object):
    AOND_1: Any
    AOND_2: Any
    AOND_3 = AOGAS_TIME.REDUCED_GAIN
    AOND_5 = AOGAS_TIME.NO_GAIN

class AOGAS_NOTIFY_PERIOD(object):
    AOND_START: Any
    AOND_2_3: Any
    AOND_3_5: Any
    AOND_END: Any

class AOGASController(IAOGASController):
    onNotifyAccount: Any
    __isNotifyAccount: Any
    __lastNotifyMessages: Any
    __aogasStartedAt: Any
    __isAogasEnabled: Any
    __notificator: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def __notifyAccount(self, message, collect=False):
        ...
    def __requestRequiredInfo(self):
        ...
    def __receiveAccountAttrs(self, resultID, attrs):
        ...
    def __receiveAccOnline(self, resultID, accOnline):
        ...

class _AOGASNotificator(object):
    __scope: Any
    __function: Any
    __started: Any
    __AOND: Any
    __callbackID: Any
    def __init__(self, scope, function):
        ...
    def start(self, AOND):
        ...
    def stop(self):
        ...
    def isStarted(self):
        ...
    def __getNotifyPeriod(self, AOND):
        ...
    def __getNextNotifyTime(self, AOND):
        ...
    def __getPrevNotifyTime(self, AOND):
        ...
    def __getNotifyMessages(self, AOND):
        ...
    def __doNotify(self, messages):
        ...
    def __notify(self, notifyPeriod):
        ...
