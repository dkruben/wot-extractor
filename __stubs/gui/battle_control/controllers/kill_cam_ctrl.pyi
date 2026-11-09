# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/kill_cam_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from decimal import ROUND_HALF_EVEN as ROUND_HALF_EVEN
from enum import Enum as Enum
import Event as Event
import Math as Math
import logging as logging
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.shared.events import DeathCamEvent as DeathCamEvent
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional
_logger: Any
DistanceMarkerData: Any
GunMarkerData: Any
ImpactMarkerData: Any

class KillCamInfoMarkerType(Enum):
    GUN = 'gunMarker'
    DISTANCE = 'distanceMarker'
    IMPACT = 'gunImpact'
    HIDDEN = 'hidden'

class KillCameraController(IBattleController):
    __guiSessionProvider: Any
    __isKillCamActive: Any
    __gunMarkerData: Any
    __distanceMarkerData: Any
    __impactMarkerData: Any
    __totalSceneDuration: Any
    killCtrlState: Any
    __eManager: Any
    onKillCamModeStateChanged: Any
    onMarkerDisplayChanged: Any
    onKillCamInterrupted: Any
    onKillCamModeEffectsPlaced: Any
    onSimulationSceneActive: Any
    onRespawnRequested: Any
    def __init__(self):
        ...
    def getControllerID(self):
        ...
    def stopControl(self):
        ...
    def startControl(self, *args):
        ...
    def killCamModeActive(self, unspottedOrigin, simulatedKillerGunInfo, projectile, phaseDurations, hasSpottedData, hasAttackerVehicle, playerRelativeArmor, playerIsSpotted, totalSceneDuration, causeOfDeath, mechanicsInfo):
        ...
    def killCamModeEffectsPlaced(self, isSpotted=False):
        ...
    def killCamInterrupted(self):
        ...
    def respawnRequested(self):
        ...
    def simulationSceneActive(self, active=True):
        ...
    def changeKillCamModeState(self, state):
        ...
    def changeCameraState(self, state, ctx):
        ...
    def __buildImpactMarkerData(self, projectile, phaseDuration, playerRelativeArmor, playerIsSpotted, causeOfDeath):
        ...
    def __buildGunMarkerData(self, projectile, phaseDuration, simulatedKillerGunInfo, hasSpottedData, hasAttackerVehicle, unspottedOrigin, mechanicsInfo):
        ...
    def __buildDistanceMarkerData(self, projectile, phaseDuration, hasSpottedData, mechanicsInfo):
        ...
