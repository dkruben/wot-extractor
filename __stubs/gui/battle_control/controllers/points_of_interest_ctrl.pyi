# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/points_of_interest_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import Event as Event
from gui.battle_control.arena_info.interfaces import IPointsOfInterestController as IPointsOfInterestController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from points_of_interest.managers import PoiStateUpdateSystem as PoiStateUpdateSystem
from shared_utils import findFirst as findFirst
from EmptyEntity import EmptyEntity as EmptyEntity
from gui.battle_control.controllers.repositories import BattleSessionSetup as BattleSessionSetup
from points_of_interest.components import PoiStateComponent as PoiStateComponent
_logger: Any

class PointsOfInterestController(IPointsOfInterestController):
    __eManager: Any
    onPoiEquipmentUsed: Any
    onPoiCaptured: Any
    onPoiInvaderDestroyed: Any
    __vehPoiRegistry: Any
    def __init__(self, setup):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    @staticmethod
    def getPoiState(poiID):
        ...
    @staticmethod
    def getPoiEntity(poiID):
        ...
    def getVehicleCapturingPoiGO(self, poiName, entityGameObject, vehicleID, spaceID):
        ...
