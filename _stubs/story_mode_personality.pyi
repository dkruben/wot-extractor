# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode_personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from aih_constants import CTRL_TYPE as CTRL_TYPE, CTRL_MODE_NAME as CTRL_MODE_NAME
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES, ARENA_GUI_TYPE as ARENA_GUI_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.impl.gen import R as R
from gui.battle_hints import battle_hints_overlap_controller as battle_hints_overlap_controller
from gui.battle_hints.battle_hints_overlap_controller import HintScope as HintScope
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes, initScaleformGuiTypes as initScaleformGuiTypes
from gui.shared.system_factory import registerScaleformBattlePackages as registerScaleformBattlePackages, registerScaleformLobbyPackages as registerScaleformLobbyPackages
from schema_manager import getSchemaManager as getSchemaManager
from story_mode import account_settings as account_settings
from story_mode.avatar_input_handler.control_modes import OnboardingArcadeControlMode as OnboardingArcadeControlMode, OnboardingSniperControlMode as OnboardingSniperControlMode, StoryModeArcadeControlMode as StoryModeArcadeControlMode, StoryModeSniperControlMode as StoryModeSniperControlMode, StoryModeArcadeMinefieldControlMode as StoryModeArcadeMinefieldControlMode, SMStrategicMapCaseControlMode as SMStrategicMapCaseControlMode, SMEntityViewMode as SMEntityViewMode
from story_mode.configs import sm_client_settings as sm_client_settings
from story_mode.gui import story_mode_gui_constants as story_mode_gui_constants
from story_mode.gui.app_loader import observers as observers
from story_mode.gui.battle_control.arena_info.arena_vos import getDisplayedClassTag as getDisplayedClassTag
from story_mode.gui.battle_control.controllers import equipments_items as equipments_items, equipment_ctrl as equipment_ctrl
from story_mode.gui.battle_control import battle_constant as battle_constant
from story_mode.gui.battle_control.controllers.repository import OnboardingRepository as OnboardingRepository, StoryModeRepository as StoryModeRepository, StoryModeSharedRepository as StoryModeSharedRepository
from story_mode.gui.game_control.story_mode_fading_controller import StoryModeFadingController as StoryModeFadingController
from story_mode.gui.impl.lobby.story_mode_event_banner import StoryModeNewbieBanner as StoryModeNewbieBanner, StoryModeEventBanner as StoryModeEventBanner
from story_mode.skeletons.story_mode_fading_controller import IStoryModeFadingController as IStoryModeFadingController
from story_mode_common import story_mode_constants as story_mode_constants, battle_mode as battle_mode
from story_mode_common.configs.story_mode_battle_mgr_quotums import quotumsSchema as quotumsSchema
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema

class ClientStoryModeBattleMode(battle_mode.StoryModeBattleMode):
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_PRB_ACTION_NAME = story_mode_gui_constants.PREBATTLE_ACTION_NAME.STORY_MODE
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = StoryModeNewbieBanner.NAME
    @property
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_prbEntityClass(self):
        ...
    @property
    def _client_prbEntryPointClass(self):
        ...
    @property
    def _client_selectorColumn(self):
        ...
    @property
    def _client_selectorItemsCreator(self):
        ...
    @property
    def _client_modeSelectorItemsClass(self):
        ...
    @property
    def _client_battleRequiredLibraries(self):
        ...
    @property
    def _client_lobbyRequiredLibraries(self):
        ...
    @property
    def _client_gameControllers(self):
        ...
    @property
    def _client_arenaDescrClass(self):
        ...
    @property
    def _client_battleResultStatsCtrlClass(self):
        ...
    @property
    def _client_messengerServerFormatters(self):
        ...
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_sharedControllersRepository(self):
        ...
    @property
    def _client_DynamicObjectCacheClass(self):
        ...
    @property
    def _client_controlModes(self):
        ...
    @property
    def _client_dynamicViewsForMonitoring(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_displayedClassTagGetter(self):
        ...

class ClientOnboardingBattleMode(ClientStoryModeBattleMode):
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.STORY_MODE_ONBOARDING
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.STORY_MODE_ONBOARDING
    _CLIENT_BATTLE_PAGE: tuple
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_lobbyRequiredLibraries(self):
        ...
    @property
    def _client_controlModes(self):
        ...

class ClientEventBattleMode(ClientStoryModeBattleMode):
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = StoryModeEventBanner.NAME
    @property
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
