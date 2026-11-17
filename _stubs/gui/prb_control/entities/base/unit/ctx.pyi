# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/unit/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import gameplay_ctx as gameplay_ctx
from external_strings_utils import truncate_utf8 as truncate_utf8
from UnitBase import UNIT_SLOT as UNIT_SLOT
from gui.prb_control import settings as settings, prb_getters as prb_getters
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
_CTRL_ENTITY_TYPE = settings.CTRL_ENTITY_TYPE
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

# decorador original: @ReprInjector.withParent(...)
class UnitRequestCtx(PrbCtrlRequestCtx):
    __slots__: tuple
    def __init__(self, **kwargs):
        ...
    def getID(self):
        ...
    def getCooldown(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class CreateUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __rosterID: Any
    def __init__(self, prbType, flags=..., waitingID='', rosterID=0):
        ...
    def getRequestType(self):
        ...
    def getRosterID(self):
        ...

class JoinUnitModeCtx(UnitRequestCtx):
    __slots__: tuple
    def __init__(self, prbType, waitingID='', flags=...):
        ...
    def getID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class JoinUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __unitMgrID: Any
    __slotIdx: Any
    def __init__(self, unitMgrID, prbType, slotIdx=None, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getID(self):
        ...
    def getSlotIdx(self):
        ...

class LeaveUnitCtx(UnitRequestCtx):
    def __init__(self, waitingID='', flags=..., entityType=0):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class LockUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __isLocked: Any
    def __init__(self, isLocked=True, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isLocked(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class CloseSlotUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __slotIdx: Any
    __isClosed: Any
    def __init__(self, slotIdx, isClosed=True, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getSlotIdx(self):
        ...
    def isClosed(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetVehicleUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __vehTypeCD: Any
    __vehInvID: Any
    setReady: Any
    def __init__(self, vTypeCD=0, vehInvID=0, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getVehTypeCD(self):
        ...
    def getVehInvID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeOpenedUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __isOpened: Any
    def __init__(self, isOpened, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isOpened(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeCommentUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __comment: Any
    def __init__(self, comment, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getComment(self):
        ...
    def isCommentChanged(self, unit):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetReadyUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __isReady: Any
    resetVehicle: Any
    def __init__(self, isReady=True, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isReady(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class AssignUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __pID: Any
    __slotIdx: Any
    def __init__(self, pID, slotIdx, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...
    def getSlotIdx(self):
        ...
    def isRemove(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class AutoSearchUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __action: Any
    __vehTypes: Any
    def __init__(self, waitingID='', action=1, vehTypes=None):
        ...
    def getRequestType(self):
        ...
    def getAction(self):
        ...
    def getActionName(self):
        ...
    def isRequestToStart(self):
        ...
    def getVehTypes(self):
        ...

class AcceptSearchUnitCtx(UnitRequestCtx):
    __slots__: tuple
    def getRequestType(self):
        ...

class DeclineSearchUnitCtx(UnitRequestCtx):
    __slots__: tuple
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class BattleQueueUnitCtx(AutoSearchUnitCtx):
    __slots__: tuple
    selectVehInvID: Any
    mmData: Any
    def __init__(self, waitingID='', action=1, vehTypes=None):
        ...
    def getRequestType(self):
        ...
    def getGamePlayMask(self):
        ...
    def getDemoArenaTypeID(self):
        ...

class RosterSlotCtx(object):
    __vehTypeCD: Any
    __nationNames: Any
    __vehLevels: Any
    __vehClassNames: Any
    def __init__(self, vehTypeCD=None, nationNames=None, levels=None, vehClassNames=None):
        ...
    def getCriteria(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetRostersSlotsUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __items: Any
    def __init__(self, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def addRosterSlot(self, rosterSlotIdx, ctx):
        ...
    def getRosterSlots(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class KickPlayerUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __databaseID: Any
    def __init__(self, databaseID, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class GiveLeadershipUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __databaseID: Any
    def __init__(self, databaseID, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeDivisionUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __divisionID: Any
    def __init__(self, divisionID, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getDivisionID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetVehiclesUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __vehsList: Any
    def __init__(self, vehsList, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...
    def getVehsList(self):
        ...
