# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AvatarInputHandler/spg_marker_helpers/spg_marker_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
import BigWorld as BigWorld
import math_utils as math_utils
from AvatarInputHandler import AimingSystems as AimingSystems
from AvatarInputHandler.AimingSystems import CollisionStrategy as CollisionStrategy
from Vehicle import Vehicle as VehicleEntity
from items.utils import getVehicleShotSpeedByFactors as getVehicleShotSpeedByFactors
_SPG_SHOT_RESULT_TOLERANCE = 0.25

class SPGShotResultEnum(IntEnum):
    NOT_HIT = 0
    HIT = 1

def getSPGShotResult(targetPosition, shotIdx, shotPos, shotVel, shotGravity, player=None, target=None):
    ...
def getSPGShotFlyTime(targetPosition, shotVelVector, shotPos, maxDistance, shotVel, vehAttrs):
    ...
