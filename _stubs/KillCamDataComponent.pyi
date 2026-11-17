# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/KillCamDataComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from GenericComponents import Sequence as Sequence, StateSwitcherComponent as StateSwitcherComponent
from cgf_components_common.vehicle_components import VehicleSequenceParamsAttachedComponent as VehicleSequenceParamsAttachedComponent
from avatar_components.avatar_postmortem_component import SimulatedVehicleType as SimulatedVehicleType
from constants import KILL_CAM_STATUS_CODE as KILL_CAM_STATUS_CODE, BATTLE_LOG_SHELL_TYPES as BATTLE_LOG_SHELL_TYPES
from gun_rotation_shared import decodeGunAngles as decodeGunAngles
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr
from AvatarInputHandler.kill_cam_mode_helpers.kill_cam_helpers import calculateSPGTrajectory as calculateSPGTrajectory
from shared_utils import first as first
_logger: Any
_UNSPOTTED_PIVOT_DISTANCE_FACTOR = 12
_UNSPOTTED_MARKER_DISTANCE_FACTOR = 4

class KillCamDataComponent(BigWorld.DynamicScriptComponent):
    processedData: Any
    def __init__(self):
        ...
    @property
    def __killerIsSpotted(self):
        ...
    @property
    def __isRicochet(self):
        ...
    def set_capturedKillCamData(self, _=None):
        ...
    def getSimulationData(self):
        ...
    def __updateSimulationData(self):
        ...
    def __captureKillCamSimulationData(self, vehicles, playerID):
        ...
    def __getAttackerData(self):
        ...
    def __updateLateAttackerData(self):
        ...
    def __collectOtherVehiclesForKillCam(self, vehicles, attackerID, playerID):
        ...
    def __captureVehSimulationData(self, vehicle):
        ...
    def __captureUnspottedVehSimulationData(self, vehicleID):
        ...
    def __getGunAngles(self, veh):
        ...
    def __getTurretAndGunSpeed(self, veh):
        ...
    def __getDynAttachmentsInfo(self, vehicle):
        ...
    def __unpackShellData(self, shellCompDescr):
        ...
    def __setupTrajectory(self):
        ...
