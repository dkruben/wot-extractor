# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand_personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers.AccountSettings import AccountSettings as AccountSettings, KEY_SETTINGS as KEY_SETTINGS
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from constants_utils import initCommonTypes as initCommonTypes, initSquadCommonTypes as initSquadCommonTypes, addBattleEventTypesFromExtension as addBattleEventTypesFromExtension, addAttackReasonTypesFromExtension as addAttackReasonTypesFromExtension, addDamageInfoCodes as addDamageInfoCodes, addDamageResistanceReasonsFromExtension as addDamageResistanceReasonsFromExtension, addBattleChatCommands as addBattleChatCommands, initSquadAssemblerCommonTypes as initSquadAssemblerCommonTypes
from debug_utils import LOG_DEBUG as LOG_DEBUG
from aih_constants import CTRL_TYPE as CTRL_TYPE, CTRL_MODE_NAME as CTRL_MODE_NAME
from last_stand.gui.game_control.ls_quests_ui_cache import LSQuestsUICache as LSQuestsUICache
from last_stand.gui.ls_account_settings import ACCOUNT_DEFAULT_SETTINGS as ACCOUNT_DEFAULT_SETTINGS
from last_stand.gui.register_additional_params import registerAdditionalParams as registerAdditionalParams, initAdditionalGuiTypes as initAdditionalGuiTypes
from last_stand.gui.scaleform.genConsts.LAST_STAND_HANGAR_ALIASES import LAST_STAND_HANGAR_ALIASES as LAST_STAND_HANGAR_ALIASES
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from last_stand.gui.shared.utils import checkAbilities as checkAbilities
from last_stand_common import last_stand_constants as last_stand_constants
from last_stand.gui import ls_gui_constants as ls_gui_constants
from last_stand.gui.battle_control import ls_battle_constants as ls_battle_constants
from last_stand.control_modes import LSArcadeControlMode as LSArcadeControlMode, LSSniperControlMode as LSSniperControlMode
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes, initScaleformGuiTypes as initScaleformGuiTypes, initBattleCtrlIDs as initBattleCtrlIDs
from gui.shared.system_factory import registerScaleformBattlePackages as registerScaleformBattlePackages
from last_stand_common.last_stand_constants import LS_BATTLE_CHAT_COMMAND_SETTINGS as LS_BATTLE_CHAT_COMMAND_SETTINGS
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
from chat_shared import SYS_MESSAGE_TYPE as _SM_TYPE

class ClientLastStandBattleMode(last_stand_constants.LastStandBattleMode):
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_PRB_ACTION_NAME = ls_gui_constants.PREBATTLE_ACTION_NAME.LAST_STAND
    _CLIENT_PRB_ACTION_NAME_SQUAD = ls_gui_constants.PREBATTLE_ACTION_NAME.LAST_STAND_SQUAD
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = LAST_STAND_HANGAR_ALIASES.LS_ENTRY_POINT
    @property
    def _client_prbEntityClass(self):
        ...
    @property
    def _client_canSelectPrbEntity(self):
        ...
    @property
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_prbEntryPointClass(self):
        ...
    @property
    def _client_gameControllers(self):
        ...
    @property
    def _client_awardControllerHandlers(self):
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
    def _client_prbSquadEntityClass(self):
        ...
    @property
    def _client_prbSquadEntryPointClass(self):
        ...
    @property
    def _client_selectorSquadItemsCreator(self):
        ...
    @property
    def _client_platoonViewClass(self):
        ...
    @property
    def _client_platoonWelcomeViewClass(self):
        ...
    @property
    def _client_platoonSearchViewClass(self):
        ...
    @property
    def _client_platoonLayouts(self):
        ...
    @property
    def _client_readyVehicleCheckers(self):
        ...
    @property
    def _client_unitMembersOrderKey(self):
        ...
    @property
    def _client_arenaDescrClass(self):
        ...
    @property
    def _client_squadFinderClass(self):
        ...
    @property
    def _client_lobbyRequiredLibraries(self):
        ...
    @property
    def _client_battleEntry(self):
        ...
    @property
    def _client_LobbyContextMenuOptions(self):
        ...
    @property
    def _client_DynamicObjectCacheClass(self):
        ...
    @property
    def _client_tokenQuestsSubFormatters(self):
        ...
    @property
    def _client_bonusTokens(self):
        ...
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_sharedControllersRepository(self):
        ...
    @property
    def _client_battleChannelController(self):
        ...
    @property
    def _client_battleResultStatsCtrlClass(self):
        ...
    @property
    def _client_battleResultsReusables(self):
        ...
    @property
    def _client_messengerServerFormatters(self):
        ...
    @property
    def _client_customizationHangarDisabled(self):
        ...
    @property
    def _client_advancedChatComponent(self):
        ...
    @property
    def _client_controlModes(self):
        ...
    @property
    def _client_equipmentTriggers(self):
        ...
    @property
    def _client_equipmentItems(self):
        ...
    @property
    def _client_equipmentItemsTooltipMovies(self):
        ...
    @property
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_guiItemsCacheInvalidators(self):
        ...
    @property
    def _client_lowPriorityWulfWindows(self):
        ...
    @property
    def _client_viewsForMonitoring(self):
        ...

class ClientLastStandMediumBattleMode(ClientLastStandBattleMode):
    _ARENA_BONUS_TYPE = last_stand_constants.ARENA_BONUS_TYPE.LAST_STAND_MEDIUM
    _QUEUE_TYPE = last_stand_constants.QUEUE_TYPE.LAST_STAND_MEDIUM
    @property
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...

class ClientLastStandHardBattleMode(ClientLastStandBattleMode):
    _ARENA_BONUS_TYPE = last_stand_constants.ARENA_BONUS_TYPE.LAST_STAND_HARD
    _QUEUE_TYPE = last_stand_constants.QUEUE_TYPE.LAST_STAND_HARD
    @property
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
