# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/tournament/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from gui.clans.settings import DEFAULT_COOLDOWN as DEFAULT_COOLDOWN
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from soft_exception import SoftException as SoftException

class TournamentRequestCtx(CommonWebRequestCtx):
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

class TournamentJoinBattleCtx(TournamentRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class TournamentLeaveModeCtx(TournamentRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...

class TournamentUpdateCtx(TournamentRequestCtx):
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

class TournamentAssignCtx(TournamentRequestCtx):
    __slots__: tuple
    __pID: Any
    __slotIdx: Any
    __isRemove: Any
    def __init__(self, pID, isRemove, slotIdx, **kwargs):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...

class TournamentUnassignCtx(TournamentRequestCtx):
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

class TournamentChangeOpenedCtx(TournamentRequestCtx):
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

class TournamentSetVehicleCtx(TournamentRequestCtx):
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

class TournamentSetReadyCtx(TournamentRequestCtx):
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

class TournamentBattleQueueCtx(TournamentRequestCtx):
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

class TournamentKickPlayerCtx(TournamentRequestCtx):
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

class TournamentGiveLeadershipCtx(TournamentRequestCtx):
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

class TournamentSendInvitesCtx(TournamentRequestCtx):
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

class TournamentSetSlotVehicleTypeFilter(TournamentRequestCtx):
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

class TournamentSetSlotVehiclesFilter(TournamentRequestCtx):
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

class TournamentStopPlayersMatchingCtx(TournamentRequestCtx):
    @classmethod
    def fromPrbCtx(cls, prbCtx, unitMgrId):
        ...
    def getRequestType(self):
        ...

class SlotVehicleFiltersUpdateCtx(TournamentRequestCtx):
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...

class TournamentMatchmakingInfoCtx(TournamentRequestCtx):
    def getRequestType(self):
        ...
    @classmethod
    def fromPrbCtx(cls, prbCtx):
        ...
