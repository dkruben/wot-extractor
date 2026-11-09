# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline_personality.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers.AccountSettings import AccountSettings as AccountSettings, KEY_SETTINGS as KEY_SETTINGS
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME, CTRL_TYPE as CTRL_TYPE
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, HAS_DEV_RESOURCES as HAS_DEV_RESOURCES
from constants_utils import AbstractBattleMode as AbstractBattleMode
from fl_kill_cam_mode import FLLookAtKillerMode as FLLookAtKillerMode
from frontline.gui import gui_constants as gui_constants
from frontline.gui.Scaleform import registerFLScaleform as registerFLScaleform
from frontline.gui.Scaleform.daapi.view.lobby.hangar.hangar_quest_flags import registerQuestFlags as registerQuestFlags
from frontline.gui.battle_control.controllers.consumables import registerFLEquipmentController as registerFLEquipmentController
from frontline.gui.battle_control.controllers.equipment_items import registerFLEquipmentsItems as registerFLEquipmentsItems
from frontline.gui.battle_control.controllers.repositories import registerFLBattleRepositories as registerFLBattleRepositories
from frontline.gui.frontline_gui_constants import initFLLimitedUIIDs as initFLLimitedUIIDs
from frontline.gui.gui_constants import ViewAlias as ViewAlias
from frontline.gui.impl.lobby.views.frontline_event_banner import FrontlineEventBanner as FrontlineEventBanner, isEpicBattlesEntryPointAvailable as isEpicBattlesEntryPointAvailable
from frontline.gui.prb_control import registerFLPrebattles as registerFLPrebattles, extendIntroByType as extendIntroByType
from frontline_common.constants import ACCOUNT_DEFAULT_SETTINGS as ACCOUNT_DEFAULT_SETTINGS
from gui.Scaleform.genConsts.EPICBATTLES_ALIASES import EPICBATTLES_ALIASES as EPICBATTLES_ALIASES
from gui.override_scaleform_views_manager import g_overrideScaleFormViewsConfig as g_overrideScaleFormViewsConfig
from gui.prb_control.prb_utils import initHangarGuiConsts as initHangarGuiConsts
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
LOBBY_EXT_PACKAGES: list
BATTLE_EXT_PACKAGES: list

class ClientFrontlineBattleMode(AbstractBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.EPIC
    _QUEUE_TYPE = QUEUE_TYPE.EPIC
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.EPIC_BATTLE
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.EPIC_BATTLE
    _CLIENT_BATTLE_PAGE: tuple
    _CLIENT_PRB_ACTION_NAME = PREBATTLE_ACTION_NAME.EPIC
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = EPICBATTLES_ALIASES.EPIC_BATTLES_ENTRY_POINT
    @property
    def _client_bannerEntryPointValidatorMethod(self):
        ...
    @property
    def _client_bannerEntryPointLUIRule(self):
        ...
    @property
    def _client_providerBattleQueue(self):
        ...
    @property
    def _client_battleRequiredLibraries(self):
        ...
    @property
    def _client_ammunitionPanelViews(self):
        ...
    @property
    def _client_ammunitionSetupViews(self):
        ...
    @property
    def _client_hangarPresetsReader(self):
        ...
    @property
    def _client_hangarDynamicGuiProvider(self):
        ...
    @property
    def _client_hangarEventBannerType(self):
        ...
    @property
    def _client_controlModes(self):
        ...

class ClientFrontlineTrainingBattleMode(ClientFrontlineBattleMode):
    _PREBATTLE_TYPE = PREBATTLE_TYPE.EPIC_TRAINING
    _ARENA_BONUS_TYPE = ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.EPIC_TRAINING
    _CLIENT_PRB_ACTION_NAME = PREBATTLE_ACTION_NAME.EPIC_TRAINING_LIST
    _CLIENT_BANNER_ENTRY_POINT_ALIAS = EPICBATTLES_ALIASES.EPIC_BATTLES_ENTRY_POINT

def preInit():
    ...
def init():
    ...
def start():
    ...
def fini():
    ...
