# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/personal_mission_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory as MissionCategory
from gui.impl.gen.view_models.views.lobby.personal_missions_30.main_view_reward_model import RewardsType as RewardsType
from gui.impl.gen.view_models.views.lobby.personal_missions_30.rewards_view_model import RewardsViewType as RewardsViewType
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from typing import Optional as Optional, Set as Set
MAX_DETAIL_ID = 15
MAX_DAILY_QUESTS_PM_POINTS = 25
MAX_NEWBIE_DAILY_QUESTS_PM_POINTS = 15
MISSIONS_ROLES_TO_CATEGORIES: dict
REWARDS_VIEW_TYPES: dict
REWARD_CLASSES: dict
PERSONAL_MISSIONS_CAMPAIGN_SELECTOR_SPACE: Any
PERSONAL_MISSIONS_CAMPAIGNS_1_2_SPACE: Any
PERSONAL_MISSIONS_CAMPAIGN_3_SPACE: Any
_STAGES_CONFIG_DATA: dict
STAGES_CONFIG: dict

class IntroKeys(Enum):
    PM3_MAIN_INTRO_VIEW = 'INTRO'
    OPERATION_INTRO_VIEW = 'INTRO_OP_%s'

class OperationIDs(int, Enum):
    OPERATION_FIRST = 8
    OPERATION_SECOND = 9
    OPERATION_THIRD = 10
    OPERATION_FOURTH = 11

class CameraNameTemplates(str, Enum):
    STAGE = 'operation_{}_stage_{}'
    TOP = 'operation_{}_camera_top_{}'
    FREE = 'operation_{}_camera_free'
    FREE_FAR = 'operation_{}_camera_free_far'

class TopCameras(int, Enum):
    FIRST = 1
    SECOND = 2

class StageAdditions(str, Enum):
    CAPE = 'cape'
    SUPPORT = 'support'

class AssemblingType(str, Enum):
    FADE = 'fade'
    VIDEO = 'video'

class SoundsSpaceKeys(CONST_CONTAINER):
    CAMPAIGN_SELECTOR_SPACE = 'pm_campaign_selector'
    CAMPAIGNS_1_2_SPACE = 'pm_campaigns_1_2'
    CAMPAIGN_3_SPACE = 'pm_campaign_3'

class SoundsStateKeys(CONST_CONTAINER):
    HANGAR_PROGRESSION_STATE = 'STATE_hangar_personal_missions_progression'
    HANGAR_PROGRESSION_ON_STATE = 'STATE_hangar_personal_missions_progression_on'
    HANGAR_PROGRESSION_OFF_STATE = 'STATE_hangar_personal_missions_progression_off'
    HANGAR_PLACE_STATE = 'STATE_hangar_place'
    HANGAR_PLACE_PERSONAL_MISSIONS_STATE = 'STATE_hangar_place_personalMissions'
    PERSONAL_MISSIONS_STATE = 'STATE_hangar_personalMissions'
    CAMPAIGN_SELECTOR_STATE = 'STATE_hangar_personalMissions_00'
    CAMPAIGNS_1_2_STATE = 'STATE_hangar_personalMissions_01'
    CAMPAIGN_3_STATE = 'STATE_hangar_personalMissions_03'

class SoundsKeys(CONST_CONTAINER):
    PLAY_ANIMATION_EVENT = 'pm_operation_%s_stage_%s'
    SWITCH_CAMERA_EVENT = 'hangar_pm_whoosh'
    CAMPAIGN_SELECTOR_ENTER = 'pm_lobby_enter'
    CAMPAIGN_SELECTOR_EXIT = 'pm_lobby_exit'
    CAMPAIGNS_1_2_AMBIENT = 'pm_ambient'
    CAMPAIGNS_1_2_MUSIC = 'pm_music'
    CAMPAIGNS_1_2_EXIT = 'pm_exit'
    CAMPAIGN_3_ENTER = 'pm_03_enter'
    CAMPAIGN_3_EXIT = 'pm_03_exit'
    TO_ASSEMBLING = 'pm_03_tank_enter'
    FROM_ASSEMBLING = 'pm_03_tank_exit'
    VEHICLE_CLICK = 'tank_selection'

class StageInfo(object):
    __slots__: tuple
    operationId: Any
    stageId: Any
    stages: Any
    additions: Any
    __assemblingType: Any
    def __init__(self, operationId, stageId, stages=None, additions=None):
        ...
    @property
    def assemblingType(self):
        ...
    def __getAssemblingType(self):
        ...
    def __getVideoPath(self):
        ...
