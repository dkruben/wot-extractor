# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/ServerSettingsManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
from itertools import chain as chain
from future.utils import viewitems as viewitems
from account_helpers.settings_core import longToInt32 as longToInt32, settings_constants as settings_constants
from account_helpers.settings_core.migrations import migrateToVersion as migrateToVersion
from account_helpers.settings_core.settings_constants import VERSION as VERSION, GuiSettingsBehavior as GuiSettingsBehavior, OnceOnlyHints as OnceOnlyHints, SPGAim as SPGAim, CONTOUR as CONTOUR, ReferralProgram as ReferralProgram, PersonalMission3 as PersonalMission3, NewYearStorageKeys as NewYearStorageKeys, PersonalMission4 as PersonalMission4
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui.battle_pass.battle_pass_helpers import updateBattlePassSettings as updateBattlePassSettings
from gui.limited_ui.lui_rules_storage import LuiRuleTypes as LuiRuleTypes
from gui.server_events.pm_constants import PM_TUTOR_FIELDS as PM_TUTOR_FIELDS
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCache as ISettingsCache
GUI_START_BEHAVIOR = 'guiStartBehavior'
GAME_EXTENDED_2 = 'gameExtData2'
HINT_STORAGE_KEY_MAPPING: dict
LIMITED_UI_STORAGES: tuple
LIMITED_UI_STORAGES_BY_TYPE: dict
LIMITED_UI_STORAGES_ALL: Any
LIMITED_UI_KEY = 'LIMITED_UI'

class SETTINGS_SECTIONS(CONST_CONTAINER):
    GAME = 'GAME'
    GAME_EXTENDED = 'GAME_EXTENDED'
    GAME_EXTENDED_2 = 'GAME_EXTENDED_2'
    GAMEPLAY = 'GAMEPLAY'
    GRAPHICS = 'GRAPHICS'
    SOUND = 'SOUND'
    CONTROLS = 'CONTROLS'
    AIM_1 = 'AIM_1'
    AIM_2 = 'AIM_2'
    AIM_3 = 'AIM_3'
    AIM_4 = 'AIM_4'
    MARKERS = 'MARKERS'
    CAROUSEL_FILTER_1 = 'CAROUSEL_FILTER_1'
    CAROUSEL_FILTER_2 = 'CAROUSEL_FILTER_2'
    CAROUSEL_FILTER_3 = 'CAROUSEL_FILTER_3'
    RANKED_CAROUSEL_FILTER_1 = 'RANKED_CAROUSEL_FILTER_1'
    RANKED_CAROUSEL_FILTER_2 = 'RANKED_CAROUSEL_FILTER_2'
    RANKED_CAROUSEL_FILTER_3 = 'RANKED_CAROUSEL_FILTER_3'
    ROYALE_CAROUSEL_FILTER_1 = 'ROYALE_CAROUSEL_FILTER_1'
    ROYALE_CAROUSEL_FILTER_2 = 'ROYALE_CAROUSEL_FILTER_2'
    EPICBATTLE_CAROUSEL_FILTER_1 = 'EPICBATTLE_CAROUSEL_FILTER_1'
    EPICBATTLE_CAROUSEL_FILTER_2 = 'EPICBATTLE_CAROUSEL_FILTER_2'
    EPICBATTLE_CAROUSEL_FILTER_3 = 'EPICBATTLE_CAROUSEL_FILTER_3'
    BATTLEPASS_CAROUSEL_FILTER_1 = 'BATTLEPASS_CAROUSEL_FILTER_1'
    MAPBOX_CAROUSEL_FILTER_1 = 'MAPBOX_CAROUSEL_FILTER_1'
    MAPBOX_CAROUSEL_FILTER_2 = 'MAPBOX_CAROUSEL_FILTER_2'
    MAPBOX_CAROUSEL_FILTER_3 = 'MAPBOX_CAROUSEL_FILTER_3'
    FUN_RANDOM_CAROUSEL_FILTER_1 = 'FUN_RANDOM_CAROUSEL_FILTER_1'
    FUN_RANDOM_CAROUSEL_FILTER_2 = 'FUN_RANDOM_CAROUSEL_FILTER_2'
    FUN_RANDOM_CAROUSEL_FILTER_3 = 'FUN_RANDOM_CAROUSEL_FILTER_3'
    COMP7_CAROUSEL_FILTER_1 = 'COMP7_CAROUSEL_FILTER_1'
    COMP7_CAROUSEL_FILTER_2 = 'COMP7_CAROUSEL_FILTER_2'
    COMP7_CAROUSEL_FILTER_3 = 'COMP7_CAROUSEL_FILTER_3'
    COMP7_LIGHT_CAROUSEL_FILTER_1 = 'COMP7_LIGHT_CAROUSEL_FILTER_1'
    COMP7_LIGHT_CAROUSEL_FILTER_2 = 'COMP7_LIGHT_CAROUSEL_FILTER_2'
    COMP7_LIGHT_CAROUSEL_FILTER_3 = 'COMP7_LIGHT_CAROUSEL_FILTER_3'
    GUI_START_BEHAVIOR = 'GUI_START_BEHAVIOR'
    EULA_VERSION = 'EULA_VERSION'
    MARKS_ON_GUN = 'MARKS_ON_GUN'
    CONTACTS = 'CONTACTS'
    FALLOUT = 'FALLOUT'
    ONCE_ONLY_HINTS = 'ONCE_ONLY_HINTS'
    ONCE_ONLY_HINTS_2 = 'ONCE_ONLY_HINTS_2'
    ONCE_ONLY_HINTS_3 = 'ONCE_ONLY_HINTS_3'
    FEEDBACK = 'FEEDBACK'
    DAMAGE_INDICATOR = 'FEEDBACK_DAMAGE_INDICATOR'
    DAMAGE_LOG = 'FEEDBACK_DAMAGE_LOG'
    BATTLE_EVENTS = 'FEEDBACK_BATTLE_EVENTS'
    BATTLE_BORDER_MAP = 'FEEDBACK_BORDER_MAP'
    QUESTS_PROGRESS = 'QUESTS_PROGRESS'
    SITUATIONAL_PERKS = 'FEEDBACK_SITUATIONAL_PERKS'
    UI_STORAGE = 'UI_STORAGE'
    UI_STORAGE_2 = 'UI_STORAGE_2'
    BATTLE_MATTERS_QUESTS = 'BATTLE_MATTERS_QUESTS'
    SESSION_STATS = 'SESSION_STATS'
    BATTLE_PASS_STORAGE = 'BATTLE_PASS_STORAGE'
    BATTLE_COMM = 'BATTLE_COMM'
    DOG_TAGS = 'DOG_TAGS'
    HOLIDAY_OPS = 'HOLIDAY_OPS'
    UNIT_FILTER = 'UNIT_FILTER'
    BATTLE_HUD = 'BATTLE_HUD'
    SPG_AIM = 'SPG_AIM'
    CONTOUR = 'CONTOUR'
    LIMITED_UI_1 = 'LIMITED_UI_1'
    LIMITED_UI_2 = 'LIMITED_UI_2'
    SENIORITY_AWARDS_STORAGE = 'SENIORITY_AWARDS_STORAGE'
    LIMITED_UI_PERMANENT_1 = 'LIMITED_UI_PERMANENT_1'
    LIMITED_UI_PERMANENT_2 = 'LIMITED_UI_PERMANENT_2'
    REFERRAL_PROGRAM = 'REFERRAL_PROGRAM'
    ADVANCED_ACHIEVEMENTS_STORAGE = 'ADVANCED_ACHIEVEMENTS_STORAGE'
    PERSONAL_MISSION_3 = 'PERSONAL_MISSION_3'
    PERSONAL_MISSION_4 = 'PERSONAL_MISSION_4'
    ONCE_ONLY_HINTS_GROUP: tuple
    CAROUSEL_FILTER_3_GROUP: tuple
    UI_STORAGE_GROUP: tuple

class UI_STORAGE_KEYS(CONST_CONTAINER):
    AUTO_RELOAD_HIGHLIGHTS_COUNTER = 'auto_reload_highlights_count'
    DISABLE_ANIMATED_TOOLTIP = 'disable_animated_tooltip'
    FIELD_POST_HINT_IS_SHOWN = 'field_post_hint'
    REFERRAL_BUTTON_CIRCLES_SHOWN = 'referral_button_circles_shown'
    DUAL_GUN_HIGHLIGHTS_COUNTER = 'dual_gun_highlights_count'
    OPTIONAL_DEVICE_SETUP_INTRO_SHOWN = 'optional_device_setup_intro_shown'
    TURBOSHAFT_HIGHLIGHTS_COUNTER = 'turboshaft_highlights_count'
    ROCKET_ACCELERATION_HIGHLIGHTS_COUNTER = 'rocket_acceleration_highlights_count'
    POST_PROGRESSION_INTRO_SHOWN = 'post_progression_intro_shown'
    VEH_PREVIEW_POST_PROGRESSION_BULLET_SHOWN = 'veh_preview_post_progression_bullet_shown'
    ACHIEVEMENT_EDIT_VIEW_VISITED = 'achievement_edit_view_visited'
    DUAL_ACCURACY_HIGHLIGHTS_COUNTER = 'dual_accuracy_highlights_count'
    STEAM_ADD_EMAIL_OVERLAY_SHOWN = 'steam_add_email_overlay_shown'
    IS_CONFIRM_EMAIL_OVERLAY_ALLOWED = 'is_confirm_email_overlay_allowed'
    LIMITED_UI_ALL_NOVICE_RULES_COMPLETED = 'limited_ui_all_novice_rules_completed'
    MUTABLE_DAMAGE_SHELL_MARK_IS_SHOWN = 'mutable_damage_shell_mark_is_shown'
    AUTO_SHOOT_HIGHLIGHTS_COUNTER = 'auto_shoot_highlights_count'
    AUTO_SHOT_NPD_SHELLS_MARK_IS_SHOWN = 'auto_shot_npd_shells_mark_is_shown'
    TWIN_GUN_HIGHLIGHTS_COUNTER = 'twin_gun_highlights_count'
    NEW_C11N_SECTION_HINT_ACTION_TAKEN = 'new_c11n_section_hint_action_taken'
    C11N_VEHICLE_LIST_HINT_ACTION_TAKEN = 'c11n_vehicle_list_hint_action_taken'
    VEHICLE_C11N_FILTER_HINT_ACTION_TAKEN = 'vehicle_c11n_filter_hint_action_taken'

class ADVANCED_ACHIEVEMENTS_STORAGE_KEYS(CONST_CONTAINER):
    EARNING_TIMESTAMP = 'ACHIEVEMENTS_EARNING_TIMESTAMP'

class BATTLE_MATTERS_KEYS(CONST_CONTAINER):
    QUESTS_SHOWN = 'shown'
    QUEST_PROGRESS = 'questProgress'

class LIMITED_UI_SPAM_OFF(CONST_CONTAINER):
    LOBBY_HEADER_COUNTERS_STORE = 'store'
    LOBBY_HEADER_COUNTERS_PROFILE = 'profile'
    PROFILE_HOF = 'profileHof'
    PROFILE_TECHNIQUE_PAGE = 'profileTechniquePage'
    SESSION_STATS = 'sessionStats'
    BLUEPRINTS_BUTTON = 'blueprintsButton'
    LOBBY_HEADER_COUNTERS_MISSIONS = 'missions'
    MISSIONS_MARATHON_VIEW = 'MissionsMarathonView'
    LOBBY_HEADER_COUNTERS_PM_OPERATIONS = 'PersonalMissionOperations'
    REFERRAL_BTN_COUNTER = 'referralButtonCounter'
    AP_ZONE_HINT = 'AmmunitionPanelHintZoneHint'
    C11N_PROGRESSION_HINT = 'CustomizationProgressionViewHint'
    TECH_TREE_EVENTS = 'TechTreeEvent'
    DOG_TAG_HINT = 'DogTagHangarHint'
    MODE_SELECTOR_WIDGET_BTN_HINT = 'ModeSelectorWidgetsBtnHint'
    PR_HANGAR_HINT = 'PersonalReservesHangarHint'
    MODERNIZE_SETUP_HINT = 'ModernizedSetupTabHint'
    OFFER_BANNER_WINDOW = 'OfferBannerWindow'
    ORDER: tuple

class ServerSettingsManager(object):
    settingsCache: Any
    GAME = settings_constants.GAME
    GRAPHICS = settings_constants.GRAPHICS
    SOUND = settings_constants.SOUND
    CONTROLS = settings_constants.CONTROLS
    Section: Any
    Offset: Any
    CONTACTS = settings_constants.CONTACTS
    DAMAGE_INDICATOR = settings_constants.DAMAGE_INDICATOR
    DAMAGE_LOG = settings_constants.DAMAGE_LOG
    BATTLE_EVENTS = settings_constants.BATTLE_EVENTS
    BATTLE_BORDER_MAP = settings_constants.BATTLE_BORDER_MAP
    QUESTS_PROGRESS = settings_constants.QUESTS_PROGRESS
    SITUATIONAL_PERKS = settings_constants.SITUATIONAL_PERKS
    SESSION_STATS = settings_constants.SESSION_STATS
    BATTLE_COMM = settings_constants.BattleCommStorageKeys
    BATTLE_PASS = settings_constants.BattlePassStorageKeys
    SCORE_PANEL = settings_constants.ScorePanelStorageKeys
    SENIORITY_AWARDS = settings_constants.SeniorityAwardsStorageKeys
    SECTIONS: dict
    AIM_MAPPING: dict
    _MAX_AUTO_RELOAD_HIGHLIGHTS_COUNT = 5
    _MAX_AUTO_SHOOT_HIGHLIGHTS_COUNT = 5
    _MAX_DUAL_GUN_HIGHLIGHTS_COUNT = 5
    _MAX_TURBOSHAFT_HIGHLIGHTS_COUNT = 5
    _MAX_ROCKET_ACCELERATION_HIGHLIGHTS_COUNT = 5
    _MAX_DUAL_ACCURACY_HIGHLIGHTS_COUNT = 5
    _MAX_TWIN_GUN_HIGHLIGHTS_COUNTER = 5
    _core: Any
    def __init__(self, core):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def applySettings(self, callback=None):
        ...
    def getAimSetting(self, section, key, default=None):
        ...
    def getOnceOnlyHintsSetting(self, key, default=None):
        ...
    def getOnceOnlyHintsSettings(self):
        ...
    def setOnceOnlyHintsSettings(self, settings):
        ...
    def getUIStorage(self, defaults=None):
        ...
    def saveInUIStorage(self, fields):
        ...
    def getUIStorage2(self, defaults=None):
        ...
    def saveInUIStorage2(self, fields):
        ...
    def getBPStorage(self, defaults=None):
        ...
    def updateBPStorageData(self, data, defaults=None):
        ...
    def saveInBPStorage(self, settings):
        ...
    def getNewYearStorage(self, defaults=None):
        ...
    def saveInNewYearStorage(self, settings):
        ...
    def checkAutoReloadHighlights(self, increase=False):
        ...
    def checkAutoShootHighlights(self, increase=False):
        ...
    def checkDualGunHighlights(self, increase=False):
        ...
    def checkTurboshaftHighlights(self, increase=False):
        ...
    def checkRocketAccelerationHighlights(self, increase=False):
        ...
    def checkDualAccuracyHighlights(self, increase=False):
        ...
    def checkTwinGunHighlights(self, increase=False):
        ...
    def updateUIStorageCounter(self, key, step=1):
        ...
    def setDisableAnimTooltipFlag(self):
        ...
    def getDisableAnimTooltipFlag(self):
        ...
    def getBattleMattersQuestWasShowed(self):
        ...
    def setBattleMattersQuestWasShowed(self, count):
        ...
    def getBattleMattersQuestProgress(self):
        ...
    def setBattleMattersQuestProgress(self, lastSeenProgress):
        ...
    def getLimitedUIProgress(self, storageIdx, offset, ruleType):
        ...
    def setLimitedUIGroupProgress(self, data):
        ...
    def isLimitedUICompleted(self, defaults=False):
        ...
    def setLimitedUICompleted(self):
        ...
    def getPM3InstalledVehDetails(self):
        ...
    def getPM4InstalledVehDetails(self):
        ...
    def getLastFullCompletedPM3OperationID(self):
        ...
    def setPM3VehDetailInstalled(self, vehDetailNumber=0):
        ...
    def setPM4OperationFirstEntrance(self):
        ...
    def setPM4VehDetailInstalled(self, vehDetailNumber=0):
        ...
    def setViewedReferralProgramSeason(self, season):
        ...
    def getViewedReferralProgramSeason(self):
        ...
    def setQuestProgressSettings(self, settings):
        ...
    def getAdvancedAchievementsEarningTimestamp(self):
        ...
    def setAdvancedAchievementsEarningTimestamp(self, timestamp):
        ...
    def updateIsHintTutorial(self, hint):
        ...
    def setHintTutorialState(self, hint, hintSeen, tutorialSeen):
        ...
    def _buildAimSettings(self, settings):
        ...
    def setAimSettings(self, settings):
        ...
    def getMarkersSetting(self, section, key, default=None):
        ...
    def _buildMarkersSettings(self, settings):
        ...
    def setMarkersSettings(self, settings):
        ...
    def setSessionStatsSettings(self, settings):
        ...
    def getSessionStatsSettings(self):
        ...
    def getPersonalMission3Data(self, defaults=None):
        ...
    def setPersonalMission3Data(self, data):
        ...
    def getPersonalMission4Data(self, defaults=None):
        ...
    def setPersonalMission4Data(self, data):
        ...
    def getVersion(self):
        ...
    def setSettings(self, settings):
        ...
    def getSetting(self, key, default=None):
        ...
    def getSection(self, section, defaults=None):
        ...
    def getSections(self, sections, defaults=None):
        ...
    def setSections(self, sections, settings):
        ...
    def getSectionSettings(self, section, key, default=None):
        ...
    def setSectionSettings(self, section, settings):
        ...
    def _buildSectionSettings(self, section, settings):
        ...
    def _extractValue(self, key, storedValue, default, masks, offsets):
        ...
    def _mapValues(self, settings, storingValue, masks, offsets):
        ...
    def _hasKeyInSection(self, section, key):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _updateToVersion(self, callback=None):
        ...
    def _setSettingsSections(self, data):
        ...
    def __checkUIHighlights(self, key, maxVal, increase):
        ...
