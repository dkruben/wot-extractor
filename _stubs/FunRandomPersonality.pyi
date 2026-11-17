# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/FunRandomPersonality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.battle_control import registerFunRandomBattle as registerFunRandomBattle
from fun_random.gui.feature import registerFunRandomFeature as registerFunRandomFeature
from fun_random.gui.game_control import registerFunRandomAwardControllers as registerFunRandomAwardControllers
from fun_random.gui.impl import registerFunRandomImpl as registerFunRandomImpl
from fun_random.gui.prb_control import registerFunRandomOthersPrbParams as registerFunRandomOthersPrbParams
from fun_random.gui.Scaleform import registerFunRandomScaleform as registerFunRandomScaleform
from fun_random.gui.server_events import registerFunRandomQuests as registerFunRandomQuests
from fun_random.gui.fun_gui_constants import initFunRandomLimitedUIIds as initFunRandomLimitedUIIds, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from fun_random.gui import fun_gui_constants as fun_gui_constants
from fun_random_common import injectConsts as injectConsts, injectSquadConsts as injectSquadConsts
from fun_random_common.fun_battle_mode import FunRandomBattleMode as FunRandomBattleMode
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from chat_shared import SYS_MESSAGE_TYPE as _SM_TYPE
from gui.prb_control.prb_utils import initGuiTypes as initGuiTypes, initRequestType as initRequestType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES as FUNRANDOM_ALIASES
_LOBBY_EXT_PACKAGES: list

class ClientFunRandomBattleMode(FunRandomBattleMode):
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_PRB_ACTION_NAME = PREBATTLE_ACTION_NAME.FUN_RANDOM
    _CLIENT_PRB_ACTION_NAME_SQUAD = PREBATTLE_ACTION_NAME.FUN_RANDOM_SQUAD
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = FUNRANDOM_ALIASES.FUN_RANDOM_ENTRY_POINT
    _CLIENT_REPLAY_MODE_TAG = 'Arcade'
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
    def _client_gameControllers(self):
        ...
    @property
    def _client_battleControllersRepository(self):
        ...
    @property
    def _client_providerBattleQueue(self):
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
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_bannerEntryPointLUIRule(self):
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
    def _client_arenaDescrClass(self):
        ...
    @property
    def _client_squadFinderClass(self):
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
    def _client_tokenQuestsSubFormatters(self):
        ...
    @property
    def _client_lootBoxAutoOpenSubFormatters(self):
        ...
    @property
    def _client_vehicleViewStates(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_modeHiddenVehiclesCriteria(self):
        ...

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
