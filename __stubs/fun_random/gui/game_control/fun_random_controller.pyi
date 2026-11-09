# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/game_control/fun_random_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import FUN_RANDOM_LAST_PRESET as FUN_RANDOM_LAST_PRESET
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from fun_random_common.fun_constants import FUN_EVENT_ID_KEY as FUN_EVENT_ID_KEY, FUN_GAME_PARAMS_KEY as FUN_GAME_PARAMS_KEY, DEFAULT_SETTINGS_KEY as DEFAULT_SETTINGS_KEY
from fun_random.gui.feature.configs.providers.fun_mode_configuration import FunModeConfigurationProvider as FunModeConfigurationProvider
from fun_random.gui.feature.sub_systems.fun_hidden_vehicles import FunHiddenVehicles as FunHiddenVehicles
from fun_random.gui.feature.sub_systems.fun_notifications import FunNotifications as FunNotifications
from fun_random.gui.feature.sub_systems.fun_progressions import FunProgressions as FunProgressions
from fun_random.gui.feature.sub_systems.fun_sub_modes_holder import FunSubModesHolder as FunSubModesHolder
from fun_random.gui.feature.sub_systems.fun_subscription import FunSubscription as FunSubscription
from fun_random.gui.feature.sub_systems.fun_sub_modes_info import FunSubModesInfo as FunSubModesInfo
from fun_random.gui.feature.util.fun_helpers import notifyCaller as notifyCaller
from fun_random.gui.fun_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from fun_random.gui.shared.gui_items.vehicle import isOnlyFunRandomVehicle as isOnlyFunRandomVehicle
from fun_random.helpers.server_settings import FunRandomConfig as FunRandomConfig
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.utils.SelectorBattleTypesUtils import setBattleTypeAsUnknown as setBattleTypeAsUnknown
from helpers import dependency as dependency
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.shared import events as events
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers.server_settings import ServerSettings as ServerSettings
from fun_random.gui.feature.configs.modes.mode import FunModeCompositeConfigurationModel as FunModeCompositeConfigurationModel

class FunRandomController(IFunRandomController, IGlobalListener):
    __lobbyContext: Any
    __serverSettings: Any
    __funRandomSettings: Any
    __configurationProvider: Any
    __subscription: Any
    __subModesHolder: Any
    __subModesInfo: Any
    __progressions: Any
    __hiddenVehicles: Any
    __notifications: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event=None):
        ...
    def onLobbyStarted(self, ctx):
        ...
    @property
    def hiddenVehicles(self):
        ...
    @property
    def notifications(self):
        ...
    @property
    def progressions(self):
        ...
    @property
    def subscription(self):
        ...
    @property
    def subModesHolder(self):
        ...
    @property
    def subModesInfo(self):
        ...
    def isEnabled(self):
        ...
    def isFunRandomPrbActive(self):
        ...
    def isOnlyFunRandomVehicle(self, vehicle):
        ...
    def getAssetsPointer(self):
        ...
    def getConfigurationModel(self):
        ...
    def getSettings(self):
        ...
    def setDesiredSubModeID(self, subModeID, trustedSource=False):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def selectFunRandomBattle(self, desiredSubModeID, callback=None):
        ...
    def __getSubSystems(self):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onServerSettingsUpdate(self, diff):
        ...
    def __clearListening(self):
        ...
    def __createFunConfigurationProvider(self, settings):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __doSelectPrbAction(self, prbActionName, accountsToInvite=None, extData=None, callback=None):
        ...
    def __updateFunRandomSettings(self, prevSettings, newSettings):
        ...
    def __storeFunRandomPreset(self):
        ...
