# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/minimap/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from account_helpers.settings_core.options import MinimapVehModelsSetting as MinimapVehModelsSetting, MinimapHPSettings as MinimapHPSettings
from gui.Scaleform.genConsts.LAYER_NAMES import LAYER_NAMES as LAYER_NAMES
from shared_utils import BitmaskHelper as BitmaskHelper
MINIMAP_COMPONENT_PATH: Any
MINIMAP_MIN_SIZE_INDEX = 0
MINIMAP_MAX_SIZE_INDEX = 5
MINIMAP_WAS_SPOTTED_RESET_DELAY = 5.0
EQ_MARKER_TO_SYMBOL: dict
MINIMAP_ATTENTION_SOUND_ID = 'minimap_attention'

class CONTAINER_NAME(object):
    TEAM_POINTS = 'points'
    ICONS = 'icons'
    EQUIPMENTS = 'equipments'
    DEAD_VEHICLES = 'deadVehicles'
    ALIVE_VEHICLES = 'aliveVehicles'
    PERSONAL = 'personal'
    FLAGS = 'flags'
    ZONES = 'zones'
    PROTECTION_ZONE = 'landingZone'
    HQS = 'hqs'

class ENTRY_SYMBOL_NAME(object):
    ALLY_TEAM_BASE = 'AllyTeamBaseEntry'
    ENEMY_TEAM_BASE = 'EnemyTeamBaseEntry'
    ALLY_TEAM_SPAWN = 'AllyTeamSpawnEntry'
    ENEMY_TEAM_SPAWN = 'EnemyTeamSpawnEntry'
    CONTROL_POINT = 'ControlPointEntry'
    ARTILLERY_ENTRY = 'ArtilleryEntry'
    ARTILLERY_YELLOW_ENTRY = 'ArtilleryYellowEntry'
    AOE_ARTILLERY_ENTRY = 'AOEArtilleryMinimapEntry'
    BOMBER_ENTRY = 'BomberEntry'
    RECON_ENTRY = 'ReconEntry'
    SMOKE_ENTRY = 'SmokeEntry'
    VEHICLE = 'VehicleEntry'
    VIEW_POINT = 'ViewPointEntry'
    DEAD_POINT = 'DeadPointEntry'
    VIDEO_CAMERA = 'VideoCameraEntry'
    ARCADE_CAMERA = 'ArcadeCameraEntry'
    STRATEGIC_CAMERA = 'StrategicCameraEntry'
    VIEW_RANGE_CIRCLES = 'ViewRangeCirclesEntry'
    ANIMATION = 'AnimationEntry'
    MARK_OBJECTIVE_DEF = 'PositionDefendEntry'
    MARK_OBJECTIVE_ATK = 'PositionAttackEntry'
    MARK_OBJECTIVE_REPLY_DEF = 'PositionDefendReplyEntry'
    MARK_OBJECTIVE_REPLY_ATK = 'PositionAttackReplyEntry'
    MARK_POSITION = 'PositionFlashEntry'
    SIGHT_POINTER = 'SightPointerEntry'
    ARTY_MARKER = 'ArtyMarkerMinimapEntry'
    ARTY_HIT_DOT_MARKER = 'ArtyHitDotMarkerUI'
    LOCATION_MARKER = 'MarkGoingToPositionEntryUI'
    ATTENTION_MARKER = 'MarkAttentionEntryUI'
    SHOOTING_POINT_MARKER = 'ShootingPointEntryUI'
    NAVIGATION_POINT_MARKER = 'NavigationPointEntryUI'
    FLAG_POINT_MARKER = 'FlagPointEntryUI'
    UNSPOTTED_MARKER = 'UnspottedMarkerUI'
    EPIC_SECTOR_ENEMY_BASE = 'SectorBaseEnemyEntry'
    EPIC_SECTOR_ALLY_BASE = 'SectorBaseAllyEntry'
    EPIC_HQ_ENEMY = 'HeadquarterEnemyEntry'
    EPIC_HQ_ALLY = 'HeadquarterAllyEntry'
    EPIC_SECTOR = 'SectorEntry'
    EPIC_SECTOR_OVERLAY = 'SectorOverlayEntry'
    EPIC_HQ = 'HeadquarterEntry'
    EPIC_FLP = 'FrontLinePointEntry'
    EPIC_REPAIR = 'ResupplyEntry'
    EPIC_PROTECTION_ZONE = 'LandingZoneEntry'
    EPIC_DEPLOY_SECTOR_BASE_ALLY = 'SectorBaseEntryDeploymentAlly'
    EPIC_DEPLOY_SECTOR_BASE_ENEMY = 'SectorBaseEntryDeploymentEnemy'
    EPIC_DEPLOY_HQ_ALLY = 'HeadquarterEntryDeploymentAlly'
    EPIC_DEPLOY_HQ_ENEMY = 'HeadquarterEntryDeploymentEnemy'
    RADAR_ANIM = 'RadarUI'
    DISCOVERED_ITEM_MARKER: str
    COMP7_RECON = 'Comp7PointReconMinimapEntryUI'

class TRANSFORM_FLAG(object):
    FULL = 4294967295
    NO_POSITION = 1
    NO_ROTATION = 2
    NO_SCALE = 4
    DEFAULT: Any

class CIRCLE_TYPE(object):
    EMPTY = 0
    DRAW_RANGE = 1
    MAX_VIEW_RANGE = 2
    VIEW_RANGE = 4
    MIN_SPOTTING_RANGE = 8

class CIRCLE_STYLE(object):
    ALPHA = 50
    class COLOR(object):
        DRAW_RANGE = 16776960
        MAX_VIEW_RANGE = 16777215
        VIEW_RANGE = 2621223
        MIN_SPOTTING_RANGE = 4499630

class VIEW_RANGE_CIRCLES_AS3_DESCR(object):
    AS_ADD_MAX_DRAW_CIRCLE = 'as_addDrawRange'
    AS_ADD_DYN_CIRCLE = 'as_addDynamicViewRange'
    AS_ADD_MAX_VIEW_CIRCLE = 'as_addMaxViewRage'
    AS_ADD_MIN_SPOTTING_CIRCLE = 'as_addMinSpottingRange'
    AS_UPDATE_DYN_CIRCLE = 'as_updateDynRange'
    AS_DEL_MAX_DRAW_CIRCLE = 'as_delDrawRange'
    AS_DEL_DYN_CIRCLE = 'as_delDynRange'
    AS_DEL_MAX_VIEW_CIRCLE = 'as_delMaxViewRage'
    AS_DEL_MIN_SPOTTING_CIRCLE = 'as_delMinSpottingRange'
    AS_INIT_ARENA_SIZE = 'as_initArenaSize'
    AS_REMOVE_ALL_CIRCLES = 'as_removeAllCircles'

class SIGHT_POINTER_ENTRY_AS3_DESCR(str, Enum):
    AS_SET_VIEW_RANGE = 'as_setViewRange'
    AS_SET_VIEW_ANGLE = 'as_setViewAngle'
    AS_SET_MIN_VIEW_ANGLE = 'as_setMinViewAngle'

class SettingsTypes(Enum):
    MinimapVehicles = 0
    MinimapHitPoint = 1

class ADDITIONAL_FEATURES(BitmaskHelper):
    OFF = 0
    BY_REQUEST = 1
    DO_REQUEST = 2
    ALWAYS = 4
    @classmethod
    def isOn(cls, mask):
        ...
    @classmethod
    def isChanged(cls, mask):
        ...

def convertSettingToFeatures(value, previous, settingsType):
    ...
def clampMinimapSizeIndex(index):
    ...
