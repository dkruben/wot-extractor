# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pve_battle_hud.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pve_battle_hud.py
from __future__ import absolute_import
import logging
from logging import Logger
import enum
PVE_HUD_LOGGER_NAME = 'PVEBattleHUD'

def getPveHudLogger():
    return logging.getLogger(PVE_HUD_LOGGER_NAME)


@enum.unique
class WidgetType(enum.IntEnum):
    ENEMY_LIST = 1
    ALLY_LIST = 2
    MINIMAP = 3
    PROGRESS_COUNTER = 4
    PRIMARY_OBJECTIVE = 5
    SECONDARY_OBJECTIVE = 6
    COUNTDOWN = 7
    CHAT = 8
    BATTLE_COMMUNICATION = 9
    RESPAWN_HUD = 10


@enum.unique
class ProgressCounterState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    REGULAR = 3
    HIDDEN = 4


@enum.unique
class PrimaryObjectiveState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    REGULAR = 3
    HIDDEN = 4
    REMIND = 5
    LAST_REMIND = 6
    LARGE_TIMER = 7
    COUNTDOWN = 8
    SUCCESS = 9
    FAILURE = 10

    def isCompleted(self):
        return self in [PrimaryObjectiveState.HIDDEN,
         PrimaryObjectiveState.SUCCESS,
         PrimaryObjectiveState.FAILURE]


@enum.unique
class SecondaryObjectiveState(enum.IntEnum):
    INITIAL = 1
    APPEARANCE = 2
    RESTORED = 3
    REGULAR = 4
    COUNTDOWN = 5
    SUCCESS = 6
    FAILURE = 7
    DISAPPEARANCE = 8
    HIDDEN = 9
