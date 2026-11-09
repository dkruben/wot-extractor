# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/training/legacy/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, OBSERVER_VEH_INVENTORY_ID as OBSERVER_VEH_INVENTORY_ID
from gui.prb_control import settings as prb_settings
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.entities.base.legacy.ctx import TeamSettingsCtx as TeamSettingsCtx, JoinLegacyCtx as JoinLegacyCtx, SetPlayerStateCtx as SetPlayerStateCtx, LegacyRequestCtx as LegacyRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
_REQUEST_TYPE = prb_settings.REQUEST_TYPE
_FUNCTIONAL_FLAG = prb_settings.FUNCTIONAL_FLAG

# decorador original: @ReprInjector.withParent(...)
class TrainingSettingsCtx(TeamSettingsCtx):
    __slots__: tuple
    __arenaTypeID: Any
    __roundLen: Any
    __isDevBattle: Any
    def __init__(self, waitingID='', isOpened=True, comment='', isRequestToCreate=True, arenaTypeID=0, roundLen=900, flags=..., isDevBattle=False):
        ...
    @classmethod
    def fetch(cls, settings):
        ...
    @property
    def isDevBattle(self):
        ...
    def getArenaTypeID(self):
        ...
    def setArenaTypeID(self, arenaTypeID):
        ...
    def getRoundLen(self):
        ...
    def setRoundLen(self, roundLen):
        ...
    def isArenaTypeIDChanged(self, settings):
        ...
    def isRoundLenChanged(self, settings):
        ...
    def areSettingsChanged(self, settings):
        ...

class JoinTrainingCtx(JoinLegacyCtx):
    __slots__: tuple
    def __init__(self, prbID, prbClusterID, waitingID='', flags=...):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChangeArenaVoipCtx(LegacyRequestCtx):
    __slots__: tuple
    __channels: Any
    def __init__(self, channels, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getChannels(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class SetPlayerObserverStateCtx(SetPlayerStateCtx):
    __slots__: tuple
    __isObserver: Any
    def __init__(self, isObserver, isReadyState, isInitial=False, waitingID=''):
        ...
    def doVehicleValidation(self):
        ...
    def getRequestType(self):
        ...
    def getVehicleInventoryID(self):
        ...
    def isObserver(self):
        ...

class ChangeArenaGuiCtx(LegacyRequestCtx):
    __slots__: tuple
    def __init__(self, waitingID=''):
        ...
    def getRequestType(self):
        ...
