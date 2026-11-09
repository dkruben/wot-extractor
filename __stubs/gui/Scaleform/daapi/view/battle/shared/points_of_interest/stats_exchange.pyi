# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import enum as enum
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.constants import POI_TYPE_UI_MAPPING as POI_TYPE_UI_MAPPING
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.poi_helpers import getPoiEquipmentByType as getPoiEquipmentByType
from helpers import dependency as dependency
from points_of_interest.mixins import PointsOfInterestListener as PointsOfInterestListener
from points_of_interest_shared import ENEMY_VEHICLE_ID as ENEMY_VEHICLE_ID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from points_of_interest_shared import PoiStatus as PoiStatus
from points_of_interest.managers import PoiStateUpdateSystem as PoiStateUpdateSystem
from points_of_interest.components import PoiStateComponent as PoiStateComponent
_logger: Any

class PoiStatusItemUpdateResult(enum.IntEnum):
    VALID = 1
    INVALID = 2
    UPDATED = 3

class PointsOfInterestStatsController(PointsOfInterestListener):
    __sessionProvider: Any
    __statsDataController: Any
    __poiStatusItems: Any
    def __init__(self, statsDataController):
        ...
    def startControl(self, *_, **__):
        ...
    def stopControl(self):
        ...
    def onPoiAdded(self, poiState):
        ...
    def onProcessPoi(self, poiState):
        ...
    def __onPoiEquipmentUsed(self, equipment, vehicleID):
        ...
    def __onPoiCaptured(self, poiID, vehicleID):
        ...
    def __addCapturedPoint(self, poiID, vehicleID, poiState):
        ...
    def __onPoiInvaderDestroyed(self, vehicleID):
        ...

class PoiStatusItem(object):
    __stateUUID: Any
    __invader: Any
    __type: Any
    __progress: Any
    __status: Any
    __system: Any
    __isCaptured: Any
    def __init__(self, poiState):
        ...
    @property
    def invader(self):
        ...
    @property
    def type(self):
        ...
    @property
    def progress(self):
        ...
    @property
    def isCaptured(self):
        ...
    def update(self):
        ...
    def setCaptured(self, isCaptured):
        ...
    def setInvader(self, vehId):
        ...
    def getVO(self):
        ...
