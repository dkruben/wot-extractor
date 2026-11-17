# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/aih_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import Math as Math
from VehicleGunRotator import GunMarkerInfo as GunMarkerInfo
CTRL_MODES: tuple
GUN_MARKER_MIN_SIZE = 32.0
SPG_GUN_MARKER_ELEMENTS_COUNT = 37
SPG_GUN_MARKER_ELEMENTS_RATE = 10
SPG_GUN_MARKER_MIN_SIZE = 50.0
SPG_GUN_MARKER_MAX_SIZE = 100.0
SPG_GUN_MARKER_SCALE_RATE = 10.0
MAP_CASE_MODES: tuple
DEFAULT_GUN_MARKER_STATE: Any

class CTRL_TYPE(object):
    USUAL = 0
    OPTIONAL = 1
    DEVELOPMENT = 2

class ShakeReason(object):
    OWN_SHOT = 0
    OWN_SHOT_DELAYED = 1
    HIT = 2
    HIT_NO_DAMAGE = 3
    SPLASH = 4

class CTRL_MODE_NAME(object):
    ARCADE = 'arcade'
    STRATEGIC = 'strategic'
    ARTY = 'arty'
    SNIPER = 'sniper'
    POSTMORTEM = 'postmortem'
    DEBUG = 'debug'
    VIDEO = 'video'
    MAP_CASE = 'mapcase'
    MAP_CASE_ARCADE = 'arcadeMapcase'
    MAP_CASE_EPIC = 'epicMapcase'
    RESPAWN_DEATH = 'respawn'
    DEATH_FREE_CAM = 'deathfreecam'
    DUAL_GUN = 'dualgun'
    MAP_CASE_ARCADE_EPIC_MINEFIELD = 'arcadeEpicMinefieldMapcase'
    KILL_CAM = 'killcam'
    VEHICLES_SELECTION = 'vehiclesSelection'
    TWIN_GUN = 'twinGun'
    LOOK_AT_KILLER = 'lookAtKiller'
    SM_STRATEGIC = 'smStrategic'
    SM_ENTITY_VIEW = 'smEntityView'
    PREBATTLE_HIGHLIGHTS = 'prebattleHighlights'
    DEFAULT = ARCADE
    POSTMORTEM_CONTROL_MODES: tuple
    KILL_CAM_MODES: tuple

class GUN_MARKER_TYPE(int):
    UNDEFINED = 0
    CLIENT = 1
    SERVER = 2
    DUAL_ACC = 3

class GUN_MARKER_FLAG(int):
    UNDEFINED = 0
    CONTROL_ENABLED = 1
    CLIENT_MODE_ENABLED = 2
    SERVER_MODE_ENABLED = 4
    VIDEO_MODE_ENABLED = 8
    ARTY_HIT_ENABLED = 16

class SHOT_RESULT(int):
    EMPTY = 0
    UNDEFINED = 1
    NOT_PIERCED = 2
    LITTLE_PIERCED = 3
    GREAT_PIERCED = 4

class STRATEGIC_CAMERA(int):
    AERIAL = 0
    TRAJECTORY = 1
    DEFAULT = AERIAL

class CHARGE_MARKER_STATE(int):
    DIMMED = 0
    LEFT_ACTIVE = 1
    RIGHT_ACTIVE = 2
    VISIBLE = 3
    DEFAULT = DIMMED

# base nao representavel no stub: namedtuple(...)
class GunMarkerState:
    @classmethod
    def fromGunMarkerInfo(cls, gunMarkerInfo, size=None):
        ...
