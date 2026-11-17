# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/ClientUnitMgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.moves import pickle as pickle
from future.utils import iteritems as iteritems, listvalues as listvalues
import Event as Event
from ClientUnit import ClientUnit as ClientUnit
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from UnitBase import UNIT_SLOT as UNIT_SLOT, UNIT_BROWSER_CMD as UNIT_BROWSER_CMD, UNIT_BROWSER_TYPE as UNIT_BROWSER_TYPE, UNIT_ERROR as UNIT_ERROR, CMD_NAMES as CMD_NAMES
from unit_roster_config import UnitRosterSlot as UnitRosterSlot
from AccountUnitAPI import UnitClientAPI as UnitClientAPI

class ClientUnitMgr(UnitClientAPI):
    __eManager: Any
    onUnitJoined: Any
    onUnitJoining: Any
    onUnitLeft: Any
    onUnitRestored: Any
    onUnitErrorReceived: Any
    onUnitNotifyReceived: Any
    onUnitResponseReceived: Any
    id: Any
    battleID: Any
    __account: Any
    __requestID: Any
    __unit: Any
    def __init__(self, account):
        ...
    @property
    def unit(self):
        ...
    def clear(self):
        ...
    def __getNextRequestID(self):
        ...
    def onUnitUpdate(self, unitMgrID, packedUnit, packedOps):
        ...
    def onUnitError(self, requestID, unitMgrID, errorCode, errorString):
        ...
    def onUnitNotify(self, unitMgrID, notifyCode, notifyString='', argsList=None):
        ...
    def onUnitCallOk(self, requestID):
        ...
    def join(self, unitMgrID, slotIdx=...):
        ...
    def invite(self, accountsToInvite, comment):
        ...
    def setAllRosterSlots(self, rosterDefsDict):
        ...
    def _callAPI(self, methodName, *args):
        ...
    def _doUnitCmd(self, cmd, uint64Arg=0, int32Arg=0, strArg='', unitMgrID=0):
        ...
    def doCustomUnitCmd(self, cmd, unitMgrID=0, uint64Arg=0, int32Arg=0, strArg=''):
        ...
    def _clearUnit(self):
        ...
    def _restore(self):
        ...

class ClientUnitBrowser(object):
    __account: Any
    __eManager: Any
    onResultsReceived: Any
    onResultsUpdated: Any
    onErrorReceived: Any
    results: Any
    _acceptUnitMgrID: Any
    _acceptDeadlineUTC: Any
    def __init__(self, account):
        ...
    def clear(self):
        ...
    def subscribe(self, unitTypeFlags=..., showOtherLocations=False):
        ...
    def unsubscribe(self):
        ...
    def recenter(self, targetRating, unitTypeFlags=..., showOtherLocations=False):
        ...
    def left(self):
        ...
    def right(self):
        ...
    def refresh(self):
        ...
    def onError(self, errorCode, errorString):
        ...
    def onResultsSet(self, pickledBrowserResultsList):
        ...
    def onResultsUpdate(self, pickledBrowserUpdatesDict):
        ...
