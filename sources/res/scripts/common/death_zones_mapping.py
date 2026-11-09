# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/death_zones_mapping.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/death_zones_mapping.py
from __future__ import absolute_import, division
from future.utils import lrange
from past.utils import old_div
import Math
from Math import Vector2
import ArenaType
ZONES_X = 10
ZONES_Y = 10
DEATH_ZONE_IDS = lrange(0, ZONES_X * ZONES_Y)

def getZoneIdFromPosition(arenaTypeID, position):
    return Math.getZoneIdFromPosition(*(ArenaType.g_cache[arenaTypeID].boundingBox + (position,)))


def getZoneBoundsFromId(arenaTypeID, zoneId):
    lowerLeft, upperRight = ArenaType.g_cache[arenaTypeID].boundingBox
    lowerLeft = Vector2(*lowerLeft)
    upperRight = Vector2(*upperRight)
    x = zoneId % ZONES_X
    y = zoneId // ZONES_X
    stepX, stepY = (upperRight - lowerLeft).tuple()
    stepX = old_div(stepX, ZONES_X)
    stepY = old_div(stepY, ZONES_Y)
    return (lowerLeft + Vector2(x * stepX, y * stepY), lowerLeft + Vector2((x + 1) * stepX, (y + 1) * stepY))


def getZoneCenterFromId(arenaTypeID, zoneId):
    lowerLeft, upperRight = getZoneBoundsFromId(arenaTypeID, zoneId)
    return lowerLeft + (upperRight - lowerLeft) / 2.0
