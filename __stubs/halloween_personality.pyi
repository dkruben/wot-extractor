# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween_personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers.AccountSettings import AccountSettings as AccountSettings, KEY_SETTINGS as KEY_SETTINGS
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from constants_utils import initCommonTypes as initCommonTypes, initSquadCommonTypes as initSquadCommonTypes, addBattleEventTypesFromExtension as addBattleEventTypesFromExtension, addAttackReasonTypesFromExtension as addAttackReasonTypesFromExtension, addDamageInfoCodes as addDamageInfoCodes, addDamageResistanceReasonsFromExtension as addDamageResistanceReasonsFromExtension
from debug_utils import LOG_DEBUG as LOG_DEBUG
from aih_constants import CTRL_TYPE as CTRL_TYPE, CTRL_MODE_NAME as CTRL_MODE_NAME
from halloween.gui.battle_control.controllers.equipment_items import registerHWEquipmentsItems as registerHWEquipmentsItems
from halloween.gui.halloween_account_settings import ACCOUNT_DEFAULT_SETTINGS as ACCOUNT_DEFAULT_SETTINGS
from halloween.gui.halloween_gui_constants import HALLOWEEN_TOOLTIP_SET as HALLOWEEN_TOOLTIP_SET
from halloween.gui.register_additional_params import registerAdditionalParams as registerAdditionalParams, initAdditionalGuiTypes as initAdditionalGuiTypes
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from halloween.gui.shared.tooltips.hw_advanced import registerHWEquipmentTooltipMovies as registerHWEquipmentTooltipMovies
from halloween.gui.shared.utils import checkAbilities as checkAbilities
from halloween.messenger.formatters.service_channel import HWInvoiceReceivedLowPriorityFormatter as HWInvoiceReceivedLowPriorityFormatter
from halloween_common import halloween_constants as halloween_constants
from halloween.gui import halloween_gui_constants as halloween_gui_constants
from halloween.gui.battle_control import halloween_battle_constants as halloween_battle_constants
from halloween.control_modes import HWArcadeControlMode as HWArcadeControlMode, HWPostMortemControlMode as HWPostMortemControlMode, HWSniperControlMode as HWSniperControlMode
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes, initScaleformGuiTypes as initScaleformGuiTypes, initBattleCtrlIDs as initBattleCtrlIDs
from gui.shared.system_factory import registerScaleformBattlePackages as registerScaleformBattlePackages, registerLobbyTooltipsBuilders as registerLobbyTooltipsBuilders, registerLifecycleHandledSubViews as registerLifecycleHandledSubViews
from halloween_common.configs.halloween_anomalies import anomaliesConfigSchema as anomaliesConfigSchema
from halloween_common.configs.halloween_bestiary import bestiarySchema as bestiarySchema
from halloween_common.configs.halloween_gsw import GSWSchema as GSWSchema
from halloween_common.configs.halloween_loot import lootConfigSchema as lootConfigSchema
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
from chat_shared import SYS_MESSAGE_TYPE as _SM_TYPE
from schema_manager import getSchemaManager as getSchemaManager
from halloween.configs import hw_upgrades_config as hw_upgrades_config

class ClientHalloweenBattleMode(halloween_constants.HalloweenBattleMode):
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_PRB_ACTION_NAME = halloween_gui_constants.PREBATTLE_ACTION_NAME.HALLOWEEN
    _CLIENT_PRB_ACTION_NAME_SQUAD = halloween_gui_constants.PREBATTLE_ACTION_NAME.HALLOWEEN_SQUAD
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_ENTRY_POINT
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
    def _client_platoonLayouts(self):
        ...
    @property
    def _client_readyVehicleCheckers(self):
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
    def _client_awardControllerHandlers(self):
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
    def _client_gfNotifications(self):
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
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_lowPriorityWulfWindows(self):
        ...

class ClientHalloweenMediumBattleMode(ClientHalloweenBattleMode):
    _ARENA_BONUS_TYPE = halloween_constants.ARENA_BONUS_TYPE.HALLOWEEN_MEDIUM
    _QUEUE_TYPE = halloween_constants.QUEUE_TYPE.HALLOWEEN_MEDIUM
    @property
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...

class ClientHalloweenHardBattleMode(ClientHalloweenBattleMode):
    _ARENA_BONUS_TYPE = halloween_constants.ARENA_BONUS_TYPE.HALLOWEEN_HARD
    _QUEUE_TYPE = halloween_constants.QUEUE_TYPE.HALLOWEEN_HARD
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
