# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/common/death_zones_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lrange as lrange
import ArenaType as ArenaType
from Math import Vector2 as Vector2
ZONES_SIZE = 10
DEATH_ZONE_IDS: Any

class ZONE_STATE(object):
    SAVE = 0
    WARNING = 1
    CRITICAL = 2

class DEATH_ZONES_STRATEGY(object):
    CENTER_DISTANT_FIRST = 0
    LEFT_RIGHT_RANDOM_CHOICE = 1

def idxFrom(zoneId, zoneSize=...):
    ...
def zoneIdFrom(x, y, zoneSize=...):
    ...
def scale10To(zoneSize, zoneId):
    ...
def getZoneIdFromPosition(arenaTypeID, position):
    ...
def getZoneIdFromPositionFor(zoneSize, boundbox, position):
    ...
def _getZoneIdFromPosition(lowerLeft, upperRight, position, zoneSize):
    ...
def _getZoneBoundsFromId(arenaTypeID, zoneId, zoneSize, boundbox=None):
    ...
def getZoneCenterFromId(arenaTypeID, zoneId, boundbox=None):
    ...
def getZoneCenterFromIdFor(zoneSize, arenaTypeID, zoneId, boundbox=None):
    ...
