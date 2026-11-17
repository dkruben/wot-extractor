# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/legacy/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, PREBATTLE_COMMENT_MAX_LENGTH as PREBATTLE_COMMENT_MAX_LENGTH
from external_strings_utils import truncate_utf8 as truncate_utf8
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx as PrbCtrlRequestCtx
from gui.prb_control.settings import CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
_REQUEST_TYPE = prb_settings.REQUEST_TYPE
_CTRL_ENTITY_TYPE = prb_settings.CTRL_ENTITY_TYPE
_FUNCTIONAL_FLAG = prb_settings.FUNCTIONAL_FLAG

class LegacyRequestCtx(PrbCtrlRequestCtx):
    __slots__: tuple
    def __init__(self, **kwargs):
        ...
    def getPrbTypeName(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class TeamSettingsCtx(LegacyRequestCtx):
    __slots__: tuple
    __isOpened: Any
    __comment: Any
    _isRequestToCreate: Any
    def __init__(self, prbType, waitingID='', isOpened=True, comment='', isRequestToCreate=True, flags=...):
        ...
    def getRequestType(self):
        ...
    def isOpened(self):
        ...
    def setOpened(self, isOpened):
        ...
    def getComment(self):
        ...
    def setComment(self, comment):
        ...
    def isOpenedChanged(self, settings):
        ...
    def isCommentChanged(self, settings):
        ...
    def areSettingsChanged(self, settings):
        ...

# decorador original: @ReprInjector.withParent(...)
class JoinLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    __prbID: Any
    __prbClusterId: Any
    def __init__(self, prbID, prbType, prbClusterId, waitingID='', flags=...):
        ...
    def getID(self):
        ...
    def getPrbClusterId(self):
        ...
    def getRequestType(self):
        ...
    def getBonusType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class LeaveLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    def getID(self):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class AssignLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    __pID: Any
    __roster: Any
    __errorString: Any
    def __init__(self, pID, roster, waitingID=''):
        ...
    def getPlayerID(self):
        ...
    def getRoster(self):
        ...
    def getLastErrorString(self):
        ...
    def getRequestType(self):
        ...
    def setErrorString(self, errorString):
        ...
    def onResponseReceived(self, code, errorStr=''):
        ...

# decorador original: @ReprInjector.withParent(...)
class GroupSwapInTeamLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    __roster: Any
    __fromLane: Any
    __toLane: Any
    def __init__(self, roster, fLane, tLane, waitingID=''):
        ...
    def getRoster(self):
        ...
    def getGroups(self):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class GroupSwapBetweenTeamLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    __lane: Any
    def __init__(self, lane, waitingID=''):
        ...
    def getGroup(self):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class GroupAssignLegacyCtx(LegacyRequestCtx):
    __slots__: tuple
    __group: Any
    __pID: Any
    __roster: Any
    def __init__(self, pID, roster, group, waitingID=''):
        ...
    def getPlayerID(self):
        ...
    def getRoster(self):
        ...
    def getRequestType(self):
        ...
    def getGroup(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetTeamStateCtx(LegacyRequestCtx):
    __slots__: tuple
    __team: Any
    __isReadyState: Any
    __gamePlayMask: Any
    def __init__(self, team, isReadyState, waitingID='', isForced=True, gamePlayMask=0):
        ...
    def getTeam(self):
        ...
    def isReadyState(self):
        ...
    def getGamePlayMask(self):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetPlayerStateCtx(LegacyRequestCtx):
    __slots__: tuple
    __isReadyState: Any
    __isInitial: Any
    __errorString: Any
    silently: Any
    def __init__(self, isReadyState, isInitial=False, waitingID='', silently=False):
        ...
    def doVehicleValidation(self):
        ...
    def isReadyState(self):
        ...
    def isInitial(self):
        ...
    def getRequestType(self):
        ...
    def getVehicleInventoryID(self):
        ...
    def getLastErrorString(self):
        ...
    def setErrorString(self, errorString):
        ...
    def onResponseReceived(self, code, errorStr=''):
        ...

class SwapTeamsCtx(LegacyRequestCtx):
    __slots__: tuple
    def __init__(self, **kwargs):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeOpenedCtx(LegacyRequestCtx):
    __slots__: tuple
    __isOpened: Any
    def __init__(self, isOpened, waitingID=''):
        ...
    def isOpened(self):
        ...
    def isOpenedChanged(self, settings):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeCommentCtx(LegacyRequestCtx):
    __slots__: tuple
    __comment: Any
    def __init__(self, comment, waitingID=''):
        ...
    def getComment(self):
        ...
    def isCommentChanged(self, settings):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeDivisionCtx(LegacyRequestCtx):
    __slots__: tuple
    __division: Any
    def __init__(self, division, waitingID=''):
        ...
    def getDivision(self):
        ...
    def isDivisionChanged(self, settings):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class KickPlayerCtx(LegacyRequestCtx):
    __slots__: tuple
    __pID: Any
    def __init__(self, pID, waitingID=''):
        ...
    def getPlayerID(self):
        ...
    def getRequestType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class GetLegacyRosterCtx(LegacyRequestCtx):
    __slots__: tuple
    __prbID: Any
    def __init__(self, prbID, prbType, waitingID=''):
        ...
    def getPrbID(self):
        ...
    def getRequestType(self):
        ...

class JoinLegacyModeCtx(LegacyRequestCtx):
    __slots__: tuple
    def __init__(self, prbType, waitingID='', flags=...):
        ...
    def getID(self):
        ...
    def getBonusType(self):
        ...
