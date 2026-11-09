# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/game_mode_emulator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/game_mode_emulator.py
from __future__ import absolute_import
import sys, BigWorld
from SpaceVisibilityFlags import SpaceVisibilityFlagsFactory
from constants import ARENA_GAMEPLAY_IDS
GAME_MODE_ARG = 'gameMode'
DEFAULT_VISIBILITY_MASK = -1
ENVIRONMENT_ARG = 'environment'
DEFAULT_ENVIRONMENT = ''

def gameModeVisibilityMask(spaceName):
    if GAME_MODE_ARG not in sys.argv:
        return DEFAULT_VISIBILITY_MASK
    gameModeArgIndex = sys.argv.index(GAME_MODE_ARG) + 1
    if gameModeArgIndex >= len(sys.argv):
        return DEFAULT_VISIBILITY_MASK
    gameMode = sys.argv[gameModeArgIndex].lower()
    if gameMode not in ARENA_GAMEPLAY_IDS:
        return DEFAULT_VISIBILITY_MASK
    spaceVisibilityFlags = SpaceVisibilityFlagsFactory.create(spaceName)
    return spaceVisibilityFlags.getMaskForGameplayID(gameMode)


def environment():
    if ENVIRONMENT_ARG not in sys.argv:
        return DEFAULT_ENVIRONMENT
    environmentArgIndex = sys.argv.index(ENVIRONMENT_ARG) + 1
    if environmentArgIndex >= len(sys.argv):
        return DEFAULT_ENVIRONMENT
    return sys.argv[environmentArgIndex]


def createFakeAvatar():
    entityID = BigWorld.createEntity('OfflineEntity', BigWorld.camera().spaceID, 0, (0,
                                                                                     0,
                                                                                     0), (0,
                                                                                          0,
                                                                                          0), {})
    entity = BigWorld.entity(entityID)
    BigWorld.player = lambda : entity
