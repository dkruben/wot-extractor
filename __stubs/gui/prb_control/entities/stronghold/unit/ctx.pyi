# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/stronghold/unit/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control import settings as settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
_REQUEST_TYPE = settings.REQUEST_TYPE
_UNDEFINED = settings.FUNCTIONAL_FLAG.UNDEFINED

class SetReserveUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __reserveID: Any
    __isRemove: Any
    def __init__(self, reserveID, waitingID='', flags=..., entityType=0, isRemove=False):
        ...
    def getRequestType(self):
        ...
    def getReserveID(self):
        ...
    def getIsRemove(self):
        ...

class UnsetReserveUnitCtx(UnitRequestCtx):
    __slots__: tuple
    __reserveID: Any
    __isRemove: Any
    def __init__(self, reserveID, waitingID='', flags=..., entityType=0, isRemove=False):
        ...
    def getRequestType(self):
        ...
    def getReserveID(self):
        ...
    def getIsRemove(self):
        ...

class TimeoutCtx(UnitRequestCtx):
    __slots__: tuple
    __onTimeoutCallback: Any
    def __init__(self, prbType, flags=..., waitingID='', onTimeoutCallback=None):
        ...
    def callTimeoutCallback(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class CreateUnitCtx(TimeoutCtx):
    __slots__: tuple
    __rosterID: Any
    def __init__(self, prbType, flags=..., waitingID='', rosterID=0, onTimeoutCallback=None):
        ...
    def getRequestType(self):
        ...
    def getRosterID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class GiveEquipmentCommanderCtx(UnitRequestCtx):
    __slots__: tuple
    __databaseID: Any
    __role: Any
    def __init__(self, databaseID, role, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def getPlayerID(self):
        ...
    def getRole(self):
        ...
