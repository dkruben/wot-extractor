# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/view_points_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import functools as functools
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.battle_control.arena_info.interfaces import IViewPointsController as IViewPointsController
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey as VehicleInfoSortKey, VehiclesItemsCollection as VehiclesItemsCollection
from gui.battle_control.arena_info.vos_collections import AllyItemsCollection as AllyItemsCollection, SquadmanVehicleInfoSortKey as SquadmanVehicleInfoSortKey
from gui.battle_control.arena_info.vos_collections import AliveItemsCollection as AliveItemsCollection
from gui.battle_control.arena_info.vos_collections import SpawnGroupVehicleInfoSortKey as SpawnGroupVehicleInfoSortKey
from gui.battle_control.arena_info.vos_collections import SquadmanSpawnGroupVehicleInfoSortKey as SquadmanSpawnGroupVehicleInfoSortKey
from gui.battle_control.arena_info.vos_collections import RankedVehicleInfoSortKey as RankedVehicleInfoSortKey
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID

class ViewPointsController(IViewPointsController):
    __slots__: tuple
    __points: Any
    __arenaDP: Any
    __currentViewPointID: Any
    __currentVehicleID: Any
    __normalSortKey: Any
    __squadManSortKey: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def updateViewPoints(self, viewPoints):
        ...
    def updateAttachedVehicle(self, vehicleID):
        ...
    def selectVehicle(self, vehicleID):
        ...
    def unselectVehicle(self):
        ...
    def selectViewPoint(self, pointID):
        ...
    def switch(self, isNext=True):
        ...
    def __doSwitch(self, switchToNext, items, currentItem):
        ...
    def __doSelect(self, isViewpoint, vehOrPointId):
        ...
    def __defineSortKeys(self, arenaVisitor):
        ...
