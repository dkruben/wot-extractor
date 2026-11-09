# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/strongholds/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from gui.clans import items as items
from gui.clans.settings import DEFAULT_COOLDOWN as DEFAULT_COOLDOWN
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.clan.contexts import ClanRequestBaseCtx as ClanRequestBaseCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from shared_utils import makeTupleByDict as makeTupleByDict
from soft_exception import SoftException as SoftException

# decorador original: @ReprInjector.withParent(...)
class StrongholdInfoCtx(ClanRequestBaseCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def getDefDataObj(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class StrongholdStatisticsCtx(ClanRequestBaseCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def getDefDataObj(self):
        ...
    def isAuthorizationRequired(self):
        ...
    def isCaching(self):
        ...

class StrongholdRequestCtx(CommonWebRequestCtx):
    __slots__: tuple
    __unitMgrId: Any
    def __init__(self, unitMgrId=None, **kwargs):
        ...
    def getUnitMgrID(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...

class StrongholdLeaveCtx(StrongholdRequestCtx):
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...

class StrongholdSetVehicleCtx(StrongholdRequestCtx):
    __slots__: tuple
    __vehTypeCD: Any
    def __init__(self, vehTypeCD, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getVehTypeCD(self):
        ...

class StrongholdAssignCtx(StrongholdRequestCtx):
    __slots__: tuple
    __pID: Any
    __slotIdx: Any
    __isRemove: Any
    def __init__(self, pID, isRemove, slotIdx, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...
    def getSlotIdx(self):
        ...

class StrongholdUnassignCtx(StrongholdRequestCtx):
    __slots__: tuple
    __pID: Any
    __isRemove: Any
    def __init__(self, pID, isRemove, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...

class StrongholdChangeOpenedCtx(StrongholdRequestCtx):
    __slots__: tuple
    __isOpened: Any
    def __init__(self, isOpened, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def isOpened(self):
        ...

class StrongholdSetReadyCtx(StrongholdRequestCtx):
    __slots__: tuple
    __isReady: Any
    def __init__(self, isReady, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def isReady(self):
        ...

class StrongholdSetReserveCtx(StrongholdRequestCtx):
    __slots__: tuple
    __reserveID: Any
    __isRemove: Any
    def __init__(self, reserveID, isRemove, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getReserveID(self):
        ...
    def getIsRemove(self):
        ...

class StrongholdUnsetReserveCtx(StrongholdRequestCtx):
    __slots__: tuple
    __reserveID: Any
    __isRemove: Any
    def __init__(self, reserveID, isRemove, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getReserveID(self):
        ...
    def getIsRemove(self):
        ...

class StrongholdBattleQueueCtx(StrongholdRequestCtx):
    __slots__: tuple
    __action: Any
    def __init__(self, action, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def isRequestToStart(self):
        ...

class StrongholdKickPlayerCtx(StrongholdRequestCtx):
    __slots__: tuple
    __pID: Any
    def __init__(self, pID, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...

class StrongholdGiveLeadershipCtx(StrongholdRequestCtx):
    __slots__: tuple
    __pID: Any
    def __init__(self, pID, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...

class StrongholdSetEquipmentCommanderCtx(StrongholdRequestCtx):
    __slots__: tuple
    __pID: Any
    __role: Any
    def __init__(self, pID=None, role=None, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...
    def getRole(self):
        ...

class StrongholdUpdateCtx(StrongholdRequestCtx):
    __slots__: tuple
    __rev: Any
    def __init__(self, rev, **kwargs):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...
    def getRev(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class StrongholdSendInvitesCtx(StrongholdRequestCtx):
    __slots__: tuple
    __databaseIDs: Any
    __comment: Any
    def __init__(self, databaseIDs, comment, **args):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getDatabaseIDs(self):
        ...
    def getComment(self):
        ...
    def getRequestType(self):
        ...

class StrongholdJoinBattleCtx(StrongholdRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class StrongholdMatchmakingInfoCtx(StrongholdRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class StrongholdSetSlotVehicleTypeFilter(StrongholdRequestCtx):
    __slots__: tuple
    __slotIdx: Any
    __vehicleTypes: Any
    def __init__(self, slotIdx, vehicleTypes, **args):
        ...
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getSlotIdx(self):
        ...
    def getVehicleTypes(self):
        ...

class StrongholdSetSlotVehiclesFilter(StrongholdRequestCtx):
    __slots__: tuple
    __slotIdx: Any
    __vehicles: Any
    def __init__(self, slotIdx, vehicles, **args):
        ...
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getSlotIdx(self):
        ...
    def getVehicles(self):
        ...

class StrongholdStopPlayersMatchingCtx(StrongholdRequestCtx):
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...

class SlotVehicleFiltersUpdateCtx(StrongholdRequestCtx):
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class StrongholdLeaveModeCtx(StrongholdRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class StrongholdEventGetFrozenVehiclesCtx(CommonWebRequestCtx):
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...

class StrongholdEventUnfreezeVehicleCtx(CommonWebRequestCtx):
    __playerSpaID: Any
    __vehicleCD: Any
    __price: Any
    def __init__(self, playerSpaID, vehicleCD, price, **kwargs):
        ...
    def getRequestType(self):
        ...
    def getRequestArgs(self):
        ...
    def isAuthorizationRequired(self):
        ...
