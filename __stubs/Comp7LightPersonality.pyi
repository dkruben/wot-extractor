# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/Comp7LightPersonality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import comp7_light.gui.comp7_light_constants as gui_constants
from comp7_core.gui import initCoreGuiTypes as initCoreGuiTypes
from comp7_light.gui.Scaleform import registerComp7LightScaleform as registerComp7LightScaleform
from comp7_light.gui.comp7_light_constants import COMP7_LIGHT_ENTRY_POINT_ALIAS as COMP7_LIGHT_ENTRY_POINT_ALIAS
from comp7_light.gui.impl.battle import registerComp7LightBattle as registerComp7LightBattle
from comp7_light.gui.impl.lobby import registerComp7LightLobby as registerComp7LightLobby
from comp7_light.gui.prb_control import registerComp7LightOthersPrbParams as registerComp7LightOthersPrbParams
from comp7_light_battle_mode import Comp7LightBattleMode as Comp7LightBattleMode
from comp7_light_common import injectConsts as injectConsts, injectSquadConsts as injectSquadConsts
from comp7_light_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, GameSeasonType as GameSeasonType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes
from gui.shared.system_factory import registerTeamVoipSupport as registerTeamVoipSupport
_LOBBY_EXT_PACKAGES: list
_BATTLE_EXT_PACKAGES: list

class ClientComp7LightBattleMode(Comp7LightBattleMode):
    _CLIENT_PRB_ACTION_NAME = gui_constants.PREBATTLE_ACTION_NAME.COMP7_LIGHT
    _CLIENT_PRB_ACTION_NAME_SQUAD = gui_constants.PREBATTLE_ACTION_NAME.COMP7_LIGHT_SQUAD
    _CLIENT_REPLAY_MODE_TAG = 'OnslaughtLight'
    _CLIENT_GAME_SEASON_TYPE = GameSeasonType.COMP7_LIGHT
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = COMP7_LIGHT_ENTRY_POINT_ALIAS
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
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_prbEntryPointClass(self):
        ...
    @property
    def _client_prbEntityClass(self):
        ...
    @property
    def _client_canSelectPrbEntity(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_providerBattleQueue(self):
        ...
    @property
    def _client_viewsForMonitoring(self):
        ...
    @property
    def _client_prbSquadEntryPointClass(self):
        ...
    @property
    def _client_prbSquadEntityClass(self):
        ...
    @property
    def _client_selectorSquadItemsCreator(self):
        ...
    @property
    def _client_squadFinderClass(self):
        ...
    @property
    def _client_platoonWelcomeViewClass(self):
        ...
    @property
    def _client_platoonLayouts(self):
        ...
    @property
    def _client_platoonViewClass(self):
        ...
    @property
    def _client_unitMembersOrderKey(self):
        ...
    @property
    def _client_LobbyContextMenuOptions(self):
        ...
    @property
    def _client_arenaDescrClass(self):
        ...
    @property
    def _client_notificationActionHandlers(self):
        ...
    @property
    def _client_messengerServerFormatters(self):
        ...
    @property
    def _client_messengerClientFormatters(self):
        ...
    @property
    def _client_DynamicObjectCacheClass(self):
        ...
    @property
    def _client_battleResultStatsCtrlClass(self):
        ...
    @property
    def _client_battleResultsEntryState(self):
        ...
    @property
    def _client_battleResultsReusables(self):
        ...
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_prebattleCtrlMode(self):
        ...
    @property
    def _client_battleRequiredLibraries(self):
        ...

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
