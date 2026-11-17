# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/VehicleEffects.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
import cgf_network as cgf_network
import Physics as Physics
from Math import Vector3 as Vector3, Vector4 as Vector4, Matrix as Matrix
from constants import VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT
from debug_utils import LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING, LOG_DEBUG_DEV as LOG_DEBUG_DEV
from items import vehicles as vehicles
from helpers_common import decodeSegment as decodeSegment, getComponentIndexFromEncodedSegment as getComponentIndexFromEncodedSegment, HitParamsEncoder as HitParamsEncoder
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes, TankPartNames as TankPartNames
from Entity import PyFixedDictDataInstance as PyFixedDictDataInstance
from BigWorld import CollisionComponent as CollisionComponent
from typing import Optional as Optional, Union as Union, TypeVar as TypeVar, List as List, Tuple as Tuple
TYPE_VEH_HIT_POINT: Any
DUMMY_NODE_PREFIX = 'DM'
MAX_FALLBACK_CHECK_DISTANCE = 10000.0
HitEffectMapping: Any

class DamageFromShotDecoder(object):
    ShotPoint: Any
    _PRIMARY_COLLISION_INDEX = 0
    _ENCODED_SEGMENT_BITS = 64
    @staticmethod
    def hasDamaged(vehicleHitEffectCode):
        ...
    @staticmethod
    def convertComponentIndex(compIdx, collisionComponent):
        ...
    @staticmethod
    def getPartName(partIndex, collisionComponent):
        ...
    @classmethod
    def encodeHitPoint(cls, hitPoint):
        ...
    @classmethod
    def getNetworkIDFromEncodedHitPoint(cls, code):
        ...
    @classmethod
    def collideHitPoint(cls, compIdx, startPoint, endPoint, collisionComponent):
        ...
    @classmethod
    def convertDynCollisionToParentCtx(cls, collisionRes, compIdx, collisionComponent):
        ...
    @classmethod
    def parseHitPoints(cls, hitPoints, collisionComponent):
        ...
    @classmethod
    def parseHitPoint(cls, hitPoint, collisionComponent):
        ...
    @classmethod
    def getPartIndexByNetworkID(cls, spaceID, networkID):
        ...
    @classmethod
    def parseDamageStickerHitPoint(cls, hitPoint, collisions, segLength=None):
        ...

class RepaintParams(object):
    @staticmethod
    def getRepaintParams(vehicleDescr):
        ...
