# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/veh_post_progression_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import map as map
from future.utils import viewvalues as viewvalues
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior as GuiSettingsBehavior
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.vehicle_equipment import SUPPORT_EXT_DATA_FEATURES as SUPPORT_EXT_DATA_FEATURES
from gui.shared.utils.requesters import getDiffID as getDiffID, REQ_CRITERIA as REQ_CRITERIA
from gui.veh_post_progression.messages import showWelcomeUnlockMsg as showWelcomeUnlockMsg
from helpers import dependency as dependency
from helpers.server_settings import VehiclePostProgressionConfig as VehiclePostProgressionConfig
from items import vehicles as vehicles
from post_progression_common import VehiclesPostProgression as VehiclesPostProgression, SERVER_SETTINGS_KEY as SERVER_SETTINGS_KEY, EXT_DATA_SLOT_KEY as EXT_DATA_SLOT_KEY, EXT_DATA_PROGRESSION_KEY as EXT_DATA_PROGRESSION_KEY, FEATURE_BY_GROUP_ID as FEATURE_BY_GROUP_ID
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IVehiclePostProgressionController as IVehiclePostProgressionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from shared_utils import makeTupleByDict as makeTupleByDict, findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers.server_settings import ServerSettings as ServerSettings
from items.vehicles import VehicleType as VehicleType
_INVENTORY_ROOT = 'inventory'
_INVENTORY_KEYS: tuple
_SETTIGS_ROOT = 'serverSettings'

class VehiclePostProgressionController(IVehiclePostProgressionController):
    __itemsCache: Any
    __lobbyContext: Any
    __settingsCore: Any
    __serverSettings: Any
    __postProgressionSettings: Any
    def __init__(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, _):
        ...
    def isDisabledFor(self, vehicle, settings=None, skipRentalIsOver=False):
        ...
    def isEnabled(self):
        ...
    def isExistsFor(self, vehType, settings=None):
        ...
    def isSwitchSetupFeatureEnabled(self):
        ...
    def getSettings(self):
        ...
    def getInvalidProgressions(self, diff, existingIDs):
        ...
    def processVehExtData(self, vehType, extData):
        ...
    def __onProgressionSettingsUpdate(self, diff):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __getPostProgressionSettings(self):
        ...
    def __getInvalidBySettings(self, settingsDiff, existingIDs):
        ...
    def __tryShowWelcomeUnlockMsg(self):
        ...
