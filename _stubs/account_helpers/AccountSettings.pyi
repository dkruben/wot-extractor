# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/AccountSettings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import Event as Event
import Keys as Keys
import Settings as Settings
import WWISE as WWISE
import constants as constants
import nations as nations
from account_helpers import gameplay_ctx as gameplay_ctx
from account_helpers.settings_core.settings_constants import AIM as AIM, BATTLE_EVENTS as BATTLE_EVENTS, CONTOUR as CONTOUR, CONTROLS as CONTROLS, GAME as GAME, SITUATIONAL_PERKS as SITUATIONAL_PERKS, SOUND as SOUND, ArmorFlashlight as ArmorFlashlight, ArmorInspector as ArmorInspector, BattleCommStorageKeys as BattleCommStorageKeys, GuiSettingsBehavior as GuiSettingsBehavior, PersonalMission3 as PersonalMission3, PersonalMission4 as PersonalMission4, ScorePanelStorageKeys as ScorePanelStorageKeys, SPGAim as SPGAim, GRAPHICS as GRAPHICS
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, VEHICLE_CLASSES as VEHICLE_CLASSES
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.genConsts.MISSIONS_CONSTANTS import MISSIONS_CONSTANTS as MISSIONS_CONSTANTS
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS as PROFILE_CONSTANTS
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.collection.collections_constants import COLLECTION_RENEW_SEEN as COLLECTION_RENEW_SEEN, COLLECTION_START_SEEN as COLLECTION_START_SEEN, COLLECTIONS_UPDATED_ENTRY_SEEN as COLLECTIONS_UPDATED_ENTRY_SEEN
from gui.integrated_auction.constants import AUCTION_FINISH_STAGE_SEEN as AUCTION_FINISH_STAGE_SEEN, AUCTION_STAGE_START_SEEN as AUCTION_STAGE_START_SEEN
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from helpers import dependency as dependency, getClientVersion as getClientVersion
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from py2to3.compat import base64compat as base64compat
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
from typing import List as List, Optional as Optional, Iterable as Iterable
_logger: Any
KEY_FILTERS = 'filters'
KEY_SESSION_SETTINGS = 'session_settings'
KEY_SETTINGS = 'settings'
KEY_FAVORITES = 'favorites'
KEY_COUNTERS = 'counters'
KEY_NOTIFICATIONS = 'notifications'
KEY_UI_FLAGS = 'ui_flags'
KEY_MANUAL = 'manual'
KEY_BATTLE_HINTS = 'battle_hints'
KEY_NEWBIE_HINTS = 'newbie_hints'
CAROUSEL_FILTER_1 = 'CAROUSEL_FILTER_1'
CAROUSEL_FILTER_2 = 'CAROUSEL_FILTER_2'
CAROUSEL_FILTER_3 = 'CAROUSEL_FILTER_3'
CAROUSEL_FILTER_CLIENT_1 = 'CAROUSEL_FILTER_CLIENT_1'
MISSION_SELECTOR_FILTER = 'MISSION_SELECTOR_FILTER'
PM_SELECTOR_FILTER = 'PM_SELECTOR_FILTER'
RANKED_CAROUSEL_FILTER_1 = 'RANKED_CAROUSEL_FILTER_1'
RANKED_CAROUSEL_FILTER_2 = 'RANKED_CAROUSEL_FILTER_2'
RANKED_CAROUSEL_FILTER_3 = 'RANKED_CAROUSEL_FILTER_3'
RANKED_CAROUSEL_FILTER_CLIENT_1 = 'RANKED_CAROUSEL_FILTER_CLIENT_1'
EPICBATTLE_CAROUSEL_FILTER_1 = 'EPICBATTLE_CAROUSEL_FILTER_1'
EPICBATTLE_CAROUSEL_FILTER_2 = 'EPICBATTLE_CAROUSEL_FILTER_2'
EPICBATTLE_CAROUSEL_FILTER_3 = 'EPICBATTLE_CAROUSEL_FILTER_3'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_1 = 'EPICBATTLE_CAROUSEL_FILTER_CLIENT_1'
EPICBATTLE_CAROUSEL_FILTER_CLIENT_2 = 'EPICBATTLE_CAROUSEL_FILTER_CLIENT_2'
STORAGE_VEHICLES_CAROUSEL_FILTER_1 = 'STORAGE_CAROUSEL_FILTER_1'
STORAGE_BLUEPRINTS_CAROUSEL_FILTER = 'STORAGE_BLUEPRINTS_CAROUSEL_FILTER'
BATTLEPASS_CAROUSEL_FILTER_1 = 'BATTLEPASS_CAROUSEL_FILTER_1'
BATTLEPASS_CAROUSEL_FILTER_CLIENT_1 = 'BATTLEPASS_CAROUSEL_FILTER_CLIENT_1'
SELECT_VEHICLES_CAROUSEL_FILTER_1 = 'SELECT_VEHICLES_CAROUSEL_FILTER_1'
ROYALE_CAROUSEL_FILTER_1 = 'ROYALE_CAROUSEL_FILTER_1'
ROYALE_CAROUSEL_FILTER_2 = 'ROYALE_CAROUSEL_FILTER_2'
ROYALE_CAROUSEL_FILTER_CLIENT_1 = 'ROYALE_CAROUSEL_FILTER_CLIENT_1'
ROYALE_INTRO_VIDEO_SHOWN = 'ROYALE_INTRO_VIDEO_SHOWN'
ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON = 'ROYALE_INTRO_VIDEO_SHOWN_FOR_SEASON'
ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON = 'ROYALE_SQUAD_TIP_SHOWN_FOR_SEASON'
MAPBOX_CAROUSEL_FILTER_1 = 'MAPBOX_CAROUSEL_FILTER_1'
MAPBOX_CAROUSEL_FILTER_2 = 'MAPBOX_CAROUSEL_FILTER_2'
MAPBOX_CAROUSEL_FILTER_3 = 'MAPBOX_CAROUSEL_FILTER_3'
MAPBOX_CAROUSEL_FILTER_CLIENT_1 = 'MAPBOX_CAROUSEL_FILTER_CLIENT_1'
HOLIDAY_OPS = 'HOLIDAY_OPS'
FUN_RANDOM_CAROUSEL_FILTER_1 = 'FUN_RANDOM_CAROUSEL_FILTER_1'
FUN_RANDOM_CAROUSEL_FILTER_2 = 'FUN_RANDOM_CAROUSEL_FILTER_2'
FUN_RANDOM_CAROUSEL_FILTER_3 = 'FUN_RANDOM_CAROUSEL_FILTER_3'
FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1 = 'FUN_RANDOM_CAROUSEL_FILTER_CLIENT_1'
COMP7_CAROUSEL_FILTER_1 = 'COMP7_CAROUSEL_FILTER_1'
COMP7_CAROUSEL_FILTER_2 = 'COMP7_CAROUSEL_FILTER_2'
COMP7_CAROUSEL_FILTER_3 = 'COMP7_CAROUSEL_FILTER_3'
COMP7_CAROUSEL_FILTER_CLIENT_1 = 'COMP7_CAROUSEL_FILTER_CLIENT_1'
COMP7_PREBATTLE_CAROUSEL_ROW_VALUE = 'comp7PrebattleCarouselRowValue'
COMP7_IS_VOIP_IN_BATTLE_ACTIVATED = 'comp7IsVoipInBattleActivated'
COMP7_ENTITLEMENTS = 'comp7Entitlements'
COMP7_ENTITLEMENTS_TIMESTAMP = 'timestamp'
COMP7_ENTITLEMENTS_BALANCE = 'balance'
COMP7_LIGHT_CAROUSEL_FILTER_1 = 'COMP7_LIGHT_CAROUSEL_FILTER_1'
COMP7_LIGHT_CAROUSEL_FILTER_2 = 'COMP7_LIGHT_CAROUSEL_FILTER_2'
COMP7_LIGHT_CAROUSEL_FILTER_3 = 'COMP7_LIGHT_CAROUSEL_FILTER_3'
COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1 = 'COMP7_LIGHT_CAROUSEL_FILTER_CLIENT_1'
FORT_RUSH_CAROUSEL_FILTER_1 = 'FORT_RUSH_CAROUSEL_FILTER_1'
ORDERS_FILTER = 'ORDERS_FILTER'
CURRENT_VEHICLE = 'current'
ROYALE_VEHICLE = 'ROYALE_VEHICLE'
LOBBY_MENU_MANUAL_TRIGGER_SHOWN = 'lobby_menu_manual_trigger_shown'
MANUAL_NEW_CONTENT = 'manual_new_content'
GUI_START_BEHAVIOR = 'GUI_START_BEHAVIOR'
EULA_VERSION = 'EULA_VERSION'
FORT_MEMBER_TUTORIAL = 'FORT_MEMBER_TUTORIAL'
IGR_PROMO = 'IGR_PROMO'
PROMO = 'PROMO'
CONTACTS = 'CONTACTS'
FALLOUT_VEHICLES = 'FALLOUT_VEHICLES'
BOOSTERS_FILTER = 'boostersFilter'
LAST_PROMO_PATCH_VERSION = 'lastPromoPatchVersion'
LAST_STORAGE_VISITED_TIMESTAMP = 'lastStorageVisitedTimestamp'
LAST_LOGGED_SERVER_DAY = 'lastLoggedServerDay'
LAST_RESTORE_NOTIFICATION = 'lastRestoreNotification'
PREVIEW_INFO_PANEL_IDX = 'previewInfoPanelIdx'
NEW_SETTINGS_COUNTER = 'newSettingsCounter'
NEW_HOF_COUNTER = 'newHofCounter'
NEW_LOBBY_TAB_COUNTER = 'newLobbyTabCounter'
REFERRAL_COUNTER = 'referralButtonCounter'
CLAN_NOTIFICATION_COUNTERS = 'ClanButtonNewsCounters'
PROGRESSIVE_REWARD_VISITED = 'progressiveRewardVisited'
RANKED_AWARDS_COUNTER = 'rankedAwardsCounter'
RANKED_INFO_COUNTER = 'rankedInfoCounter'
RANKED_YEAR_RATING_COUNTER = 'rankedYearRatingCounter'
RANKED_SHOP_COUNTER = 'rankedShopCounter'
BOOSTERS_FOR_CREDITS_SLOT_COUNTER = 'boostersForCreditsSlotCounter'
SENIORITY_AWARDS_COUNTER = 'seniorityAwardsCounter'
SENIORITY_AWARDS_COINS_REMINDER_SHOWN_TIMESTAMP = 'saReminderShown'
DEMOUNT_KIT_SEEN = 'demountKitSeen'
RECERTIFICATION_FORM_SEEN = 'recertificationFormSeen'
VIEWED_OFFERS = 'viewedOffers'
OFFERS_DISABLED_MSG_SEEN = 'offersDisabledMsgSeen'
PROFILE_TECHNIQUE = 'profileTechnique'
PROFILE_TECHNIQUE_MEMBER = 'profileTechniqueMember'
SHOW_CRYSTAL_HEADER_BAND = 'showCrystalHeaderBand'
ELEN_NOTIFICATIONS = 'elenNotifications'
RECRUITS_NOTIFICATIONS = 'recruitsNotifications'
SPEAKERS_DEVICE = 'speakersDevice'
SESSION_STATS_PREV_BATTLE_COUNT = 'sessionStatsPrevBattleCnt'
UNIT_FILTER = 'UNIT_FILTER'
BLUEPRINTS_CONVERT_SALE_STARTED_SEEN = 'bcsStartedSeen'
IS_SHOP_VISITED = 'isShopVisited'
LAST_SHOP_ACTION_COUNTER_MODIFICATION = 'lastShopActionCounterModification'
OVERRIDEN_HEADER_COUNTER_ACTION_ALIASES = 'overridenHeaderCounterActionAliases'
LIVE_OPS_WEB_EVENTS_COUNTERS = 'liveOpsWebEventsCounters'
LIVE_OPS_WEB_EVENTS_UI_FLAGS = 'liveOpsWebEventsUIFlags'
COMP7_BOND_EQUIPMENT_REMINDER_SHOWN_TIMESTAMP = 'comp7BondEquipmentReminderShown'
COMP7_LAST_SEASON_WITH_SEEN_REWARD = 'comp7LastSeasonWithSeenReward'
COMP7_LAST_MASKOT_WITH_SEEN_REWARD = 'comp7LastMaskotWithSeenReward'
VEHICLE_CAROUSEL_COUNTERS_SEEN = 'vehicleCarouselCountersSeen'
SELECT_VEHICLES_PLAYLIST = 'selectVehiclesPlaylist'
SELECT_VEHICLES_IS_ALL_VEHICLES = 'selectVehiclesIsAllVehicles'
STORE_TAB = 'store_tab'
STATS_REGULAR_SORTING = 'statsSorting'
STATS_SORTIE_SORTING = 'statsSortingSortie'
STATS_COMP7_SORTING = 'statsSortingComp7'
STATS_COMP7_LIGHT_SORTING = 'statsSortingComp7Light'
STATS_COMP7_SPECIAL_SORTING = 'statsSortingComp7Special'
STATS_FUN_RANDOM_SORTING = 'statsSortingFunRandom'
MISSIONS_PAGE = 'missions_page'
DEFAULT_VEHICLE_TYPES_FILTER: Any
DEFAULT_LEVELS_FILTERS: Any
SHOW_OPT_DEVICE_HINT = 'showOptDeviceHint'
SHOW_OPT_DEVICE_HINT_TROPHY = 'showOptDeviceHintTrophy'
SHOW_OPT_MODERNIZED_DEVICE_HINT = 'showOptModernizedDeviceHint'
LAST_BADGES_VISIT = 'lastBadgesVisit'
LAST_SELECTED_SUFFIX_BADGE_ID = 'lastSelectedSuffixBadgeID'
ENABLE_RANKED_ANIMATIONS = 'enableRankedAnimations'
COLOR_SETTINGS_TAB_IDX = 'colorSettingsTabIdx'
COLOR_SETTINGS_SHOWS_COUNT = 'colorSettingsShowsCount'
APPLIED_COLOR_SETTINGS = 'appliedColorSettings'
SELECTED_QUEST_IN_REPLAY = 'SELECTED_QUEST_IN_REPLAY'
LAST_SELECTED_PM_BRANCH = 'lastSelectedPMBranch'
WHEELED_DEATH_DELAY_COUNT = 'wheeledDeathCounter'
FREE_CAM_USES_COUNT = 'killCamBattlesCount'
LAST_BATTLE_PASS_POINTS_SEEN = 'lastBattlePassPointsSeen'
LAST_BATTLE_PASS_CYCLES_SEEN = 'lastBattlePassCyclesSeen'
IS_BATTLE_PASS_EXTRA_START_NOTIFICATION_SEEN = 'isBattlePassExtraStarted'
IS_BATTLE_PASS_COLLECTION_SEEN = 'isCollectionSeen'
IS_BATTLE_PASS_START_NOTIFICATION_SEEN = 'isBattlePassStarted'
EXTRA_CHAPTERS_VIDEO_SHOWN = 'extraChaptersVideoShown'
BUY_ANIMATIONS_WAS_SHOWN = 'buyAnimationsWasShown'
IS_BATTLE_PASS_START_ANIMATION_SEEN = 'isBattlePassStartAnimationSeen'
LAST_BATTLE_PASS_EXTRA_CHAPTER_SEEN = 'lastBattlePassExtraChapterSeen'
UMG_BATTLE_PASS_EXTRA_CHAPTER_SEEN = 'umgBattlePassExtraChapterSeen'
LAST_BATTLE_PASS_HOLIDAY_CHAPTER_SEEN = 'lastBattlePassHolidayChapterSeen'
BR_UI_SECTION = 'battleRoyale'
BR_PROGRESSION_SEEN_QUESTS = 'battleRoyaleSeenQuests'
BR_PROGRESSION_POINTS_SEEN = 'brProgressionPointsSeen'
CRYSTALS_INFO_SHOWN = 'crystalsInfoShown'
IS_CUSTOMIZATION_INTRO_VIEWED = 'isCustomizationIntroViewed'
NPS_STORAGE = 'nps_storage'
CUSTOMIZATION_STYLE_ITEMS_VISITED = 'CustomizationStyleItemsVisited'
CUSTOMIZATION_TABS_VISITED = 'CustomizationTabsVisited'
OPT_DEVICE_TAB_VISITED = 'optDeviceTabVisited'
ANONYMIZER = GAME.ANONYMIZER
CUSTOMIZATION_SECTION = 'customization'
CAROUSEL_ARROWS_HINT_SHOWN_FIELD = 'isCarouselsArrowsHintShown'
PROJECTION_DECAL_HINT_SHOWN_FIELD = 'isProjectionDecalHintShown'
SESSION_STATS_SECTION = 'sessionStats'
BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD = 'battleEfficiencySectionExpanded'
SIEGE_HINT_SECTION = 'siegeModeHint'
WHEELED_MODE_HINT_SECTION = 'wheeledModeScreenHint'
TRAJECTORY_VIEW_HINT_SECTION = 'trajectoryViewHint'
TURBO_SHAFT_ENGINE_MODE_HINT_SECTION = 'turboShaftEngineModeHint'
ROCKET_ACCELERATION_MODE_HINT_SECTION = 'rocketAccelerationModeHint'
RECHARGEABLE_NITRO_MODE_HINT_SECTION = 'rechargeableNitroModeHint'
STAGED_JET_BOOSTERS_MODE_HINT_SECTION = 'stagedJetBoostersModeHint'
TARGET_DESIGNATOR_MODE_HINT_SECTION = 'targetDesignatorModeHint'
DYN_SQUAD_HINT_SECTION = 'dynSquadHint'
PILLBOX_HINT_SECTION = 'pillboxModeHint'
WHEELED_DASH_MODE_HINT_SECTION = 'wheeledDashModeHint'
BUSTLE_FEED_HINT_SECTION = 'bustleFeedHint'
RADAR_HINT_SECTION = 'radarHint'
PRE_BATTLE_HINT_SECTION = 'preBattleHintSection'
PRE_BATTLE_ROLE_HINT_SECTION = 'preBattleRoleHintSection'
FUN_RANDOM_HINT_SECTION = 'funRandomHintSection'
MAPBOX_HINT_SECTION = 'mapboxHintSection'
QUEST_PROGRESS_HINT_SECTION = 'questProgressHint'
HELP_SCREEN_HINT_SECTION = 'helpScreenHint'
IBC_HINT_SECTION = 'battleCommunicationHint'
RESERVES_HINT_SECTION = 'reservesHintSection'
TWIN_GUN_HINT_SECTION = 'twinGunHintSection'
SHELL_PARAMS_SWITCHER_HINT_SECTION = 'shellParamsSwitcherHintSection'
COMMANDER_CAM_HINT_SECTION = 'commanderCamHintSection'
MINIMAP_IBC_HINT_SECTION = 'minimapHintSection'
DEV_MAPS_HINT_SECTION = 'devMapsHintSection'
WATCHED_PRE_BATTLE_TIPS_SECTION = 'watchedPreBattleTipsSection'
LAST_DISPLAY_DAY = 'lastDisplayDay'
HINTS_LEFT = 'hintsLeft'
NUM_BATTLES = 'numBattles'
SELECTED_INTRO_VEHICLES_FIELD = 'selectedIntroVehicles'
NATION_CHANGE_VIEWED = 'nation_change_viewed'
CREW_SKINS_VIEWED = 'crew_skins_viewed'
CREW_BOOKS_VIEWED = 'crew_books_viewed'
CREW_SKINS_HISTORICAL_VISIBLE = 'crew_skins_historical_visible'
VEHICLES_WITH_BLUEPRINT_CONFIRM = 'showedBlueprintConfirm'
IS_FIRST_ENTRY_BY_DIVISION_ID = 'isFirstEntryByDivisionId'
RANKED_STYLED_VEHICLES_POOL = 'rankedStyledVehiclesPool'
STYLE_PREVIEW_VEHICLES_POOL = 'stylePreviewVehiclesPool'
RANKED_WEB_INFO = 'rankedWebLeague'
RANKED_WEB_INFO_UPDATE = 'rankedWebLeagueUpdate'
RANKED_AWARDS_BUBBLE_YEAR_REACHED = 'rankedAwardsBubbleYearReached'
RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED = 'rankedCurrentAwardsBubbleYearReached'
RANKED_ENTITLEMENT_EVENTS_AMOUNT = 'rankedEntitlementEventsAmount'
RANKED_YEAR_POSITION = 'rankedYearPosition'
MARATHON_REWARD_WAS_SHOWN_PREFIX = 'marathonRewardScreenWasShown'
MARATHON_VIDEO_WAS_SHOWN_PREFIX = 'marathonRewardVideoWasShown'
SUBTITLES = 'subtitles'
MODULES_ANIMATION_SHOWN = 'collectibleVehiclesAnimWasShown'
NEW_SHOP_TABS = 'newShopTabs'
IS_COMP7_BONS_BANNER_VISITED = 'isComp7BonsBannerVisited'
LAST_SHOP_TAB_COUNTER = 'lastShopTabCounter'
CUSTOM_SHOP_SETTINGS = 'customShopSettings'
QUESTS = 'quests'
QUEST_DELTAS = 'questDeltas'
QUEST_DELTAS_COMPLETION = 'questCompletion'
QUEST_DELTAS_PROGRESS = 'questProgress'
QUEST_DELTAS_TOKENS_PROGRESS = 'tokensProgress'
TOP_OF_TREE_CONFIG = 'topOfTree'
DOG_TAGS = 'dogTags'
DOG_TAGS_SELECTED_ANIMATED = 'selectedAnimated'
DOG_TAGS_SELECTED_CUSTOMIZABLE = 'selectedCustomizable'
WOT_PLUS = 'wotPlus'
TELECOM_RENTALS = 'telecomRentals'
COMMENDATIONS = 'commendations'
PERSONAL_RESERVES = 'personalReserves'
LAST_ARTY_CTRL_MODE = 'lastArtyCtrlMode'
ACTIVE_TEST_PARTICIPATION_CONFIRMED = 'activeTestParticipateConfirmed'
MAPBOX_PROGRESSION = 'mapbox_progression'
UNLOCK_VEHICLES_IN_BATTLE_HINTS = 'unlockVehiclesInBattleHints'
BECOME_ELITE_VEHICLES_WATCHED = 'becomeEliteWatched'
VPP_ENTRY_POINT_LAST_SEEN_STEP = 'vehiclePostProgressionLastSeenStep'
CLAN_PREBATTLE_SORTING_KEY = 'ClanPrebattleSortingKey'
SHOW_DEMO_ACC_REGISTRATION = 'showDemoAccRegistration'
MAPBOX_SURVEYS = 'mapbox_surveys'
CLAN_NEWS_SEEN = 'clanNewsSeen'
INTEGRATED_AUCTION_NOTIFICATIONS = 'integratedAuctionNotifications'
INTEGRATED_AUCTION_FIRST_APPEARANCE_TIMESTAMP = 'integratedAuctionBannerFirstAppearanceTimestamp'
INTEGRATED_AUCTION_INTRO_CLICK_TIMESTAMP = 'integratedAuctionBannerIntroClickTimestamp'
MINIMAP_SIZE = 'minimapSize'
COMP7_UI_SECTION = 'comp7'
COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT = 'comp7WeeklyQuestsPageTokensCount'
COMP7_SHOP_SEEN_PRODUCTS = 'comp7ShopSeenProducts'
COMP7_LAST_SEASON = 'comp7LastSeason'
COMP7_WEEKLY_WIDGET_SHOWN_QUEST = 'comp7WeeklyWidgetShownQuest'
COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN = 'comp7LastSeasonWhereStatisticsShown'
COMP7_UMG_PROGRESSION_POINTS_SEEN = 'comp7UMGProgressionPointsSeen'
COMP7_UMG_ENTRY_POINT_SEEN = 'comp7UmgEntryPointSeen'
COMP7_PROGRESSION_PAGE_C11N_PROGRESS = 'comp7ProgressionPageC11nProgress'
COMP7_LIGHT_UI_SECTION = 'comp7Light'
COMP7_LIGHT_LAST_SEASON = 'comp7LightLastSeason'
COMP7_LIGHT_PROGRESSION_POINTS_SEEN = 'comp7LightProgressionPointsSeen'
COMP7_LIGHT_UMG_PROGRESSION_POINTS_SEEN = 'comp7LightUMGProgressionPointsSeen'
COMP7_LIGHT_UMG_SEEN_QUESTS = 'comp7LightUmgSeenQuests'
COMP7_LIGHT_UMG_ENTRY_POINT_SEEN = 'comp7LightUmgEntryPointSeen'
INGAME_TOURNAMENT_SECTION = 'ingameTournament'
INGAME_TOURNAMENT_WCI_INTRO_SEEN = 'WCIIntroSeen'
INGAME_TOURNAMENT_OLS_INTRO_SEEN = 'OLSIntroSeen'
FUN_RANDOM_NOTIFICATIONS = 'funRandomNotifications'
FUN_RANDOM_NOTIFICATIONS_FROZEN = 'funRandomNotificationsFrozen'
FUN_RANDOM_NOTIFICATIONS_PROGRESSIONS = 'funRandomNotificationsProgressions'
FUN_RANDOM_NOTIFICATIONS_SUB_MODES = 'funRandomNotificationsSubModes'
LOOTBOX_SYSTEM = 'lootBoxSystem'
LOOT_BOXES_WAS_STARTED = 'lootBoxesWasStarted'
LOOT_BOXES_WAS_FINISHED = 'lootBoxesWasFinished'
LOOT_BOXES_OPEN_ANIMATION_ENABLED = 'lootBoxesOpenAnimationEnabled'
LOOT_BOXES_HAS_NEW = 'lootBoxesHasNew'
LOOT_BOXES_SELECTED_BOX = 'lootBoxesSelectedBox'
LOOT_BOXES_UNIQUE_ID = 'lootBoxesUniqueID'
LOOT_BOXES_INTRO_VIDEO_SHOWN = 'lootBoxesIntroVideoShown'
OPEN_BUNDLE_NOTIFICATIONS = 'openBundle'
OPEN_BUNDLE_START_SHOWN = 'openBundleStartShown'
OPEN_BUNDLE_REMINDER_SHOWN = 'openBundleEndSoonShown'
OPEN_BUNDLE_ENTRY_POINT_SHOWN = 'openBundleEntryIntroShown'
OPEN_BUNDLE_ENTRY_POINT_ANIMATION_SHOWN = 'openBundleEntryAnimationShown'
OPEN_BUNDLE_INTRO_SHOWN = 'openBundleIntroShown'
COLLECTIONS_SECTION = 'collections'
COLLECTIONS_INTRO_SHOWN = 'collectionsIntroShown'
COLLECTION_SHOWN_NEW_REWARDS = 'collectionsNewRewards'
COLLECTION_SHOWN_NEW_ITEMS = 'collectionNewItems'
COLLECTION_SHOWN_NEW_ITEMS_COUNT = 'collectionNewItemsCount'
COLLECTION_TUTORIAL_COMPLETED = 'collectionTutorialCompleted'
COLLECTION_WAS_ENABLED = 'collectionsWasEnabled'
COLLECTIONS_TAB_SHOWN_IDS = 'collectionsTabShownIds'
COLLECTIONS_TAB_SHOWN_NEW_ITEMS = 'collectionsTabShownNewItems'
SHOWN_COMPLETED_COLLECTIONS = 'shownCompletedCollections'
LAST_SHOWN_NEW_COLLECTION = 'lastShownNewColLection'
LAST_SHOWN_COLLECTION_BALANCE = 'lastShownCollectionBalance'
COLLECTIONS_NOTIFICATIONS = 'collectionsNotifications'
ACHIEVEMENTS_INFO = 'achievements20_info'
ACHIEVEMENTS_INITIAL_BATTLE_COUNT = 'achievements20InitialBattleCount'
ACHIEVEMENTS_MAX_WTR_POINTS = 'achievements20MaxWtrPoints'
ACHIEVEMENTS_WTR_RANKS = 'achievementsWtrRanks'
ACHIEVEMENTS_WTR_PREV_POINTS_NOTIFICATION = 'achievementWtrPointsNotification'
ACHIEVEMENTS_WTR_INFO = 'achievementWtr'
ACHIEVEMENTS_WTR_PREV_POINTS = 'achievementWtrPoints'
ACHIEVEMENTS_WTR_PREV_RANK = 'achievementWtrPrevRank'
ACHIEVEMENTS_WTR_PREV_SUB_RANK = 'achievementWtrPrevSubRank'
PREV_ACHIEVEMENTS_NAME_LIST = 'prevAchievementNameList'
ACHIEVEMENTS_VISITED = 'achievementsVisited'
ACHIEVEMENTS_FIRST_ENTRY_STATUS = 'achievementsFirstEntryStatus'
ACHIEVEMENTS_RATING_CALCULATED_STATUS = 'achievementsRatingCalculatedStatus'
ACHIEVEMENTS_EDITING_ENABLED_STATUS = 'achievementsEditingEnabledStatus'
ACHIEVEMENTS_MEDAL_ADDED_STATUS = 'achievementsMedalAddedStatus'
ACHIEVEMENTS_RATING_CHANGED_STATUS = 'achievementsRatingChangedStatus'
ACHIEVEMENTS_MEDAL_COUNT_INFO = 'achievementsMedalCountInfo'
ADVANCED_ACHIEVEMENTS = 'AdvancedAchievements'
PREV_CATEGORY_LIST_DATA = 'prevCategoryListData'
PREV_ACHIEVEMENT_SCORE = 'prevAchievementScore'
PREV_PLAYER_COLLECTION_PROGRESS = 'prevPlayerCollectionProgress'
PREV_TROPHY_COUNT = 'prevTrophyCount'
IS_NEEDED_SHOW_HINT_ACHIEVEMENT_CATALOG = 'isNeededShowHintAchievementCatalog'
UNSEEN_ADVANCED_ACHIEVEMENTS = 'unseenAdvancedAchievements'
SEEN_TROPHIES_ADVANCED_ACHIEVEMENTS = 'seenTrophiesAdvancedAchievements'
MAIN_ADVANCED_ACHIEVEMENTS_PAGE_VISITED = 'mainAdvancedAchievementsPageVisited'
EXCHANGE_GOLD_RATE_DISCOUNT_ANIMATION_SHOWED = 'ExchangeGoldRateDiscountAnimationShowed'
EXCHANGE_XP_RATE_DISCOUNT_ANIMATION_SHOWED = 'ExchangeXpRateDiscountAnimationShowed'
VIEWED_MODULES_SECTION = 'mua'
LIMITED_UI_VERSIONED_RULES = 'luiVersioned'
TANKMEN_LIST = 'tankmenList'
NATIONS_VISITED = 'nationsVisited'
VEH_SKILL_TREE_HINT_SHOWN = 'vehSkillTreeHintShown'
VEH_SKILL_TREE_POPUP_SHOWN = 'vehSkillTreePopupShown'
VEH_SKILL_TREE_RECORDED_NOFITICATION_NODE = 'vehSkillTreeRecordedNotificationNode'
VEH_SKILL_TREE_PRESTIGE_GLARE_SHOWN = 'vehSkillTreePrestigeGlareShown'
VEH_SKILL_TREE_INTRO_SHOWN = 'vehSkillTreeIntroShown'
PERSONAL_MISSION_3 = 'PERSONAL_MISSION_3'
PERSONAL_MISSION_4 = 'PERSONAL_MISSION_4'
CHALLENGES_START_SEEN_NOTIFICATION = 'challengesStartSeenNotification'
CHALLENGES_REMINDER_SEEN_NOTIFICATION = 'challengesReminderSeenNotification'
HANGAR_VIEW_SETTINGS = 'hangarView'
HANGAR_KEY_BINDINGS = 'hangarKeyBindings'
AttackerVehicleConfiguration: Any
KNOWN_SELECTOR_BATTLES = 'knownSelectorBattles'
MODE_SELECTOR_BATTLE_PASS_SHOWN = 'modeSelectorBattlePassShown'
RANKED_LAST_CYCLE_ID = 'rankedLastCycleID'
EPIC_LAST_CYCLE_ID = 'epicLastCycleID'
FRONTLINE_BANNER_FIRST_APPEARANCE_TIMESTAMP = 'frontlineBannerFirstAppearanceTimestamp'
FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP = 'frontlineBannerIntroClickTimestamp'
COMP7_BANNER_FIRST_APPEARANCE_TIMESTAMP = 'comp7BannerFirstAppearanceTimestamp'
COMP7_LIGHT_BANNER_FIRST_APPEARANCE_TIMESTAMP = 'comp7LightBannerFirstAppearanceTimestamp'
BATTLE_ROYALE_BANNER_FIRST_APPEARANCE_TIMESTAMP = 'battleRoyaleBannerFirstAppearanceTimestamp'
FUN_RANDOM_BANNER_LAST_VISITED_SEASON_BORDER = 'funRandomBannerLastVisitedSeasonBorder'
FUN_RANDOM_BANNER_LAST_VISIBLE_PROGRESSION_NAME = 'funRandomBannerLastVisibleProgressionName'
FUN_RANDOM_LAST_PRESET = 'funRandomLastPreset'
FUN_RANDOM_PROGRESSION_OPENED = 'funRandomProgressionOpened'
FUN_RANDOM_INF_PROGRESSION_OPENED = 'funRandomInfProgressionOpened'
FUN_RANDOM_PROGRESSION = 'funRandomProgression'
FUN_RANDOM_PROGR_PREV_COUNTER = 'funRandomProgressionPrevCounter'
FUN_RANDOM_INF_PROGR_PREV_COUNTER = 'funRandomInfProgressionPrevCounter'
FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT = 'funRandomInfProgressionPrevCompleteCount'
DEFAULT_VALUES: dict
MOUSE_SENSITIVITY_CONTROL_MODE_PATHS: dict

class BattleMatters(object):
    BATTLE_MATTERS_SETTINGS = 'battleMattersSettings'
    BATTLES_COUNT_WITHOUT_PROGRESS = 'battlesCountWithoutProgress'
    QUEST_IDX_FOR_LAST_UPDATED_PROGRESS = 'progressForQuest'
    LAST_QUEST_PROGRESS = 'lastQuestProgress'
    REMINDER_LAST_DISPLAY_TIME = 'reminderLastDisplayTime'
    LAST_BATTLE_TIME = 'lastBattleTime'

class Winback(object):
    WINBACK_SETTINGS = 'winbackSettings'
    COMPLETED_STARTING_QUEST_COUNT = 'completedStartingQuestCount'
    INTRO_SHOWN = 'introShown'
    BATTLE_SELECTOR_SETTINGS_BULLET_SHOWN = 'battleSelectorSettingsBulletShown'

class EasyTankEquip(object):
    EASY_TANK_EQUIP_SETTINGS = 'easyTankEquipSettings'
    SHELLS_CARD_SELECTED_PRESET_INDEX = 'shellsCardSelectedPresetIndex'
    CONSUMABLES_CARD_SELECTED_PRESET_INDEX = 'consumablesCardSelectedPresetIndex'
    CONSUMABLES_CARD_PRESET_SLOTS_ORDER = 'consumablesCardPresetSlotsOrder'

class AdventCalendar(object):
    SETTINGS = 'adventCalendarSettings'
    INTRO_SHOWN = 'adventCalendarIntroShown'
    LAST_HIGHLIGHTED_DOOR = 'adventCalendarLastHighlightedDoor'
    FIRST_ENTRY_NOTIFICATION_SHOWING_DAY = 'adventCalendarFirstEntryNotificationShowingDay'
    LAST_DAY_POPUP_SEEN = 'adventCalendarLastDayPopupSeen'

class HolidayOps(object):
    SETTINGS = 'holidayOpsSettings'
    HO_DAILY_QUESTS_VISITED = 'HODailyQuestsVisited'
    HO_GIFT_MACHINE_BUY_TOKEN_VISITED = 'HOGiftMachineBuyTokenVisited'
    HO_SACK_INFO_VISITED = 'HOSackInfoVisited'
    HO_SACK_INFO_LAST_SELECTED = 'HOSackInfoLastSelected'
    HO_RESOURCE_COLLECTING_AVAILABLE = 'HOResourceCollectingAvailable'
    HO_RESOURCE_FRIENDS_COLLECTING_AVAILABLE = 'HOResourceFriendsCollectingAvailable'
    HO_CELEBRITY_ADV_QUESTS_VISITED_MASK = 'HOCelebrityAdvQuestsVisitedMask'
    HO_CELEBRITY_DAY_QUESTS_VISITED_MASK = 'HOCelebrityDayQuestsVisitedMask'
    HO_CELEBRITY_DAY_QUESTS_COMPLETED_MASK = 'HOCelebrityDayQuestsCompletedMask'
    HO_GUEST_ACTIVITY_SHOWN = 'HOGuestActivityShown'
    HO_MAX_LEVEL_MESSAGE_CLOSE = 'HOMaxLevelMessageClose'
    HO_DOG_PAGE_VISITED = 'HODogPageVisited'
    HO_MARKET_PLACE_PAGE_VISITED = 'HOMarketPlaceVisited'
    HO_CAT_PAGE_VISITED = 'HOCatPageVisited'
    HO_FRIENDS_BANNER_SHOWN = 'HOFriendsBannerShown'
    HO_NO_FRIENDS_PAGE_RESET_TIME = 'HONoFriendsPageResetTime'
    HO_REWARD_KIT_OPEN = 'HORewardKitOpen'
    HO_GIFT_MACHINE_HINT_VISIBLE = 'HOGiftMachineHintVisible'
    HO_CHALLENGE_LAST_QUEST_COMPLETION_COUNT = 'HOChallengeLastQuestCompletionCount'
    HO_LAST_SEEN_COLLECTING_NOTIFY_TIME = 'lastSeenCollectingNotifyTime'
    HO_LAST_SEEN_FRIENDS_NOTIFY_TIME = 'lastSeenFriendsNotifyTime'
    HO_LAST_SEEN_NO_FRIENDS_NOTIFY_TIME = 'lastSeenNoFriendsNotifyTime'
    HO_BANNER_FIRST_APPEARANCE_TIMESTAMP = 'bannerFirstAppearanceTimestamp'
    HO_SOMETHING_VISITED_TIMESTAMP = 'somethingVisitedTimestamp'

class StrongholdEvent(object):
    SETTINGS = 'strongholdEventSettings'
    IS_BANNER_FIRST_APPEARANCE_SEEN = 'isBannerFirstAppearanceSeen'
    FIRST_BANNER_ENTERING_MADE = 'firstBannerEnteringMade'

class ResourceWell(object):
    SETTINGS = 'resourceWellSettings'
    START_SHOWN = 'resourceWellStartShown'
    END_SHOWN = 'resourceWellEndShown'
    NOTIFICATIONS = 'resourceWellNotifications'
    IS_BANNER_FIRST_APPEARANCE_SEEN = 'isBannerFirstAppearanceSeen'
    FIRST_BANNER_ENTERING_MADE = 'firstBannerEnteringMade'

class OptionalDevicesAssistant(object):
    SELECTED_PRESET = 'optionalDevicesAssistantSelectedPreset'

class PetSystem(object):
    SETTINGS = 'petSystemSettings'
    SEEN_PET_NAME_IDS = 'petSystemSeenPetNameIDs'
    SEEN_PET_LEVELS = 'petSystemSeenPetLevels'
    SEEN_IN_STORAGE_PET_IDS = 'petSystemSeenInStoragePetIDs'
    SEEN_PROMO_PET_IDS = 'petSystemSeenPromoPetIDs'

class ChallengesMissions(object):
    SETTINGS = 'challengesSettings'
    CHALLENGES_BUNDLE_SHOWN = 'challengesBundleIntroShown'
    CHALLENGES_BUNDLE_ANIMATION_SHOWN = 'challengesBundleAnimationShown'
    VISITED_CHALLENGES = 'visitedChallenges'
    CHALLENGES_INFO_SHOWN = 'challengesInfoShown'

class AccountSettings(object):
    onSettingsChanging: Any
    version = 107
    settingsCore: Any
    __cache: dict
    __sessionSettings: dict
    __isFirstRun = True
    __isCleanPC = False
    @staticmethod
    def clearCache():
        ...
    @staticmethod
    def _readSection(ds, name):
        ...
    @staticmethod
    def _readUserSection():
        ...
    @staticmethod
    def isCleanPC():
        ...
    @staticmethod
    def overrideDefaultSettings(name, value):
        ...
    @staticmethod
    def convert():
        ...
    @staticmethod
    def getFilterDefault(name):
        ...
    @staticmethod
    def getNotificationDefault(name):
        ...
    @staticmethod
    def invalidateNewSettingsCounter():
        ...
    @staticmethod
    def rebindKey(key, newCommand):
        ...
    @staticmethod
    def checkAndResetFireKeyIfInUse(expectedCommand, expectedKey):
        ...
    @staticmethod
    def clearKeyAndSetNewCommand(newCommand, commandKey):
        ...
    @staticmethod
    def removeOldCommandAndReuseFireKey(oldCommand, newCommand):
        ...
    @staticmethod
    def getFilterDefaults(names):
        ...
    @staticmethod
    def getFilter(name):
        ...
    @staticmethod
    def setFilter(name, value):
        ...
    @staticmethod
    def getSettingsDefault(name):
        ...
    @classmethod
    def getSettings(cls, name):
        ...
    @classmethod
    def setSettings(cls, name, value):
        ...
    @staticmethod
    def getManualData(name):
        ...
    @staticmethod
    def setManualData(name, value):
        ...
    @staticmethod
    def setManualUnreadPages(content):
        ...
    @staticmethod
    def getManualUnreadPages():
        ...
    @staticmethod
    def getFavorites(name):
        ...
    @staticmethod
    def setFavorites(name, value):
        ...
    @staticmethod
    def getCounters(name):
        ...
    @staticmethod
    def setCounters(name, value):
        ...
    @staticmethod
    def getNotifications(name, default=None):
        ...
    @staticmethod
    def setNotifications(name, value, force=False):
        ...
    @staticmethod
    def getSessionSettings(name):
        ...
    @staticmethod
    def setSessionSettings(name, value):
        ...
    @staticmethod
    def getSessionSettingsDefault(name):
        ...
    @staticmethod
    def updateNewSettingsCounter(defaultDict, savedDict):
        ...
    @classmethod
    def getUIFlag(cls, name):
        ...
    @classmethod
    def setUIFlag(cls, name, value):
        ...
    @classmethod
    def getBattleMattersSetting(cls, name):
        ...
    @classmethod
    def setBattleMattersSetting(cls, name, value):
        ...
    @classmethod
    def getNewbieHints(cls, name, default=None):
        ...
    @classmethod
    def setNewbieHints(cls, name, value, default=None):
        ...
    @classmethod
    def getBattleHints(cls, name, default=None):
        ...
    @classmethod
    def setBattleHints(cls, name, value, default=None):
        ...
    @classmethod
    def getVehicleViewedModules(cls, vehIntCD):
        ...
    @classmethod
    def setVehicleViewedModules(cls, vehIntCD, modules):
        ...
    @classmethod
    def clearVehicleViewedModules(cls, vehIntCD):
        ...
    @classmethod
    def isVersionedRuleCompleted(cls, ruleID):
        ...
    @classmethod
    def getCompletedVersionedRules(cls):
        ...
    @classmethod
    def completeVersionedRules(cls, ruleIDs):
        ...
    @classmethod
    def clearVersionedRules(cls, ruleIDs):
        ...
    @staticmethod
    def _getValue(name, setting, force=False, default=None):
        ...
    @staticmethod
    def _setValue(name, value, setting, force=False, default=None):
        ...
    @staticmethod
    def __getSessionSettings(name):
        ...
    @staticmethod
    def __setSessionSettings(name, value):
        ...
    @staticmethod
    def __getUserSessionSettings():
        ...
    @staticmethod
    def __checkUserKeyBinding(key=None, command=None, commandSectionItems=None):
        ...
    @classmethod
    def __getPlayerName(cls):
        ...

def _filterAccountSection(dataSec):
    ...
def _pack(value):
    ...
def _unpack(value):
    ...
def _recursiveStep(defaultDict, savedDict, finalDict):
    ...
