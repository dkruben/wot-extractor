# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/external_battle_unit/base_external_battle_ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control import settings as settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from external_strings_utils import truncate_utf8 as truncate_utf8
from gui.prb_control.settings import INVITE_COMMENT_MAX_LENGTH as INVITE_COMMENT_MAX_LENGTH, REQUEST_TYPE as REQUEST_TYPE
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

class TimeoutCtx(UnitRequestCtx):
    __slots__: tuple
    __onTimeoutCallback: Any
    def __init__(self, prbType, flags=..., waitingID='', onTimeoutCallback=None):
        ...
    def callTimeoutCallback(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class CreateBaseExternalUnitCtx(TimeoutCtx):
    __slots__: tuple
    __rosterID: Any
    def __init__(self, prbType, flags=..., waitingID='', rosterID=0, onTimeoutCallback=None):
        ...
    def getRequestType(self):
        ...
    def getRosterID(self):
        ...

class JoinBaseExternalUnitCtx(TimeoutCtx):
    __slots__: tuple
    __unitMgrID: Any
    __onErrorCallback: Any
    def __init__(self, unitMgrID, prbType, onErrorCallback=None, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getID(self):
        ...
    def callErrorCallback(self, errorData):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeVehTypesInSlotFilterCtx(UnitRequestCtx):
    __slots__: tuple
    __slotIdx: Any
    __vehTypes: Any
    def __init__(self, slotIdx, vehTypes, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getSlotIdx(self):
        ...
    def getVehTypes(self):
        ...
    def getCooldown(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeVehiclesInSlotFilterCtx(UnitRequestCtx):
    __slots__: tuple
    __slotIdx: Any
    __vehicles: Any
    def __init__(self, slotIdx, vehicles, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getSlotIdx(self):
        ...
    def getVehicles(self):
        ...
    def getCooldown(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SendInvitesExternalBattleUnitCtx(PrbCtrlRequestCtx):
    __databaseIDs: Any
    __comment: Any
    def __init__(self, databaseIDs, comment, waitingID=''):
        ...
    def getDatabaseIDs(self):
        ...
    def getComment(self):
        ...
    def getRequestType(self):
        ...

class StopPlayersMatchingBaseExternalUnitCtx(UnitRequestCtx):
    __slots__: tuple
    def getRequestType(self):
        ...
