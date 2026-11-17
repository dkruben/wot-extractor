# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush_personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from chat_shared import SYS_MESSAGE_TYPE as _SM_TYPE
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from constants_utils import initCommonTypes as initCommonTypes, initSquadCommonTypes as initSquadCommonTypes
from debug_utils import LOG_DEBUG as LOG_DEBUG
from fort_rush.account_helpers.account_settings import extendAccountSettings as extendAccountSettings
from fort_rush.gui import fort_rush_gui_constants as fort_rush_gui_constants
from fort_rush.gui.battle_results import registerFortRushBattleResultsStatsSorting as registerFortRushBattleResultsStatsSorting
from fort_rush.gui.register_aditional_params import registerConditionFormatterIcons as registerConditionFormatterIcons
from fort_rush.gui.game_control import registerFortRushAwardControllers as registerFortRushAwardControllers, registerFortRushSMTypes as registerFortRushSMTypes, registerControlModeOverrides as registerControlModeOverrides
from fort_rush_common import fort_rush_constants as fort_rush_constants
from fort_rush_common.configs.fort_rush_battles_config import fortRushBattlesConfigGameParamsSchema as fortRushBattlesConfigGameParamsSchema
from gui.battle_results.reusable import ReusableInfoFactory as ReusableInfoFactory
from gui.impl.gen import R as R
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from fort_rush.gui.fort_rush_gui_constants import FUNCTIONAL_FLAG as FORT_RUSH_FUNCTIONAL_FLAG
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes, initScaleformGuiTypes as initScaleformGuiTypes, initBattleCtrlIDs as initBattleCtrlIDs
from gui.shared.system_factory import registerScaleformLobbyPackages as registerScaleformLobbyPackages, registerIgnoredModeForAutoSelectVehicle as registerIgnoredModeForAutoSelectVehicle
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL
from schema_manager import getSchemaManager as getSchemaManager

class ClientFortRushBattleMode(fort_rush_constants.FortRushBattleMode):
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = fort_rush_gui_constants.FORT_RUSH_HANGAR_ALIASES.FORT_RUSH_ENTRY_POINT
    _CLIENT_PRB_ACTION_NAME = fort_rush_gui_constants.PREBATTLE_ACTION_NAME.FORT_RUSH
    _CLIENT_PRB_ACTION_NAME_SQUAD = fort_rush_gui_constants.PREBATTLE_ACTION_NAME.FORT_RUSH_SQUAD
    _CLIENT_GAME_SEASON_TYPE = fort_rush_constants.GameSeasonType.FORT_RUSH
    @property
    def _client_prbEntityClass(self):
        ...
    @property
    def _client_canSelectPrbEntity(self):
        ...
    @property
    def _client_prbEntryPointClass(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_bannerEntryPointValidatorMethod(self):
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
    def _client_providerBattleQueue(self):
        ...
    @property
    def _client_squadFinderClass(self):
        ...
    @property
    def _client_arenaDescrClass(self):
        ...
    @property
    def _client_battleResultStatsCtrlClass(self):
        ...
    @property
    def _client_seasonControllerHandler(self):
        ...
    @property
    def _client_battleRequiredLibraries(self):
        ...
    @property
    def _client_lobbyRequiredLibraries(self):
        ...
    @property
    def _client_battleEntry(self):
        ...
    @property
    def _client_DynamicObjectCacheClass(self):
        ...
    @property
    def _client_notificationActionHandlers(self):
        ...
    @property
    def _client_messengerClientFormatters(self):
        ...
    @property
    def _client_messengerServerFormatters(self):
        ...
    @property
    def _client_tokenQuestsSubFormatters(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_LobbyContextMenuOptions(self):
        ...
    @property
    def _client_battleChannelController(self):
        ...
    @property
    def _client_customizationHangarDisabled(self):
        ...
    @property
    def _client_attackReasonToCode(self):
        ...
    @property
    def _client_gameControllers(self):
        ...
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_sharedControllersRepository(self):
        ...
    @property
    def _client_battleResultsReusables(self):
        ...

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
