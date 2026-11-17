# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_vehicle_selection_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CURRENT_VEHICLE as CURRENT_VEHICLE
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from helpers import dependency as dependency
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared.system_factory import collectIgnoredModeForAutoSelectVehicle as collectIgnoredModeForAutoSelectVehicle
from last_stand.gui import vehicleComparisonKey as vehicleComparisonKey
from last_stand.gui.ls_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys, setSettings as setSettings
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_vehicle_selection_controller import ILSVehicleSelectionController as ILSVehicleSelectionController
from last_stand_common.last_stand_constants import LAST_STAND_ARENA_BONUS_TYPES as LAST_STAND_ARENA_BONUS_TYPES
from skeletons.gui.shared import IItemsCache as IItemsCache

class LSVehicleSelectionController(ILSVehicleSelectionController, IGlobalListener):
    _lsCtrl: Any
    _itemsCache: Any
    __active: Any
    __returnFromLSBattle: Any
    def __init__(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def selectModeVehicle(self, vehInvID=0):
        ...
    def selectVehicle(self, vehInvID):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def __getFavoriteVehInvID(self):
        ...
    def __consumeReturnFromBattle(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
