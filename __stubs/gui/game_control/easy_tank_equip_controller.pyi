# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/easy_tank_equip_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from typing import Optional as Optional, TYPE_CHECKING as TYPE_CHECKING
from constants import Configs as Configs
from helpers import dependency as dependency
from helpers.server_settings import EasyTankEquipConfig as EasyTankEquipConfig
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.game_control.wotlda.easy_tank_equip_provider import _EasyTankEquipProvider as _EasyTankEquipProvider
from gui.game_control.wotlda.loadout_model import BaseOptDeviceLoadoutModel as BaseOptDeviceLoadoutModel

class EasyTankEquipController(IEasyTankEquipController):
    __lobbyContext: Any
    __em: Any
    onUpdated: Any
    _dataProvider: Any
    def __init__(self):
        ...
    @property
    def config(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def getLoadoutByVehicleID(self, vehicleID):
        ...
    def __removeListeners(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
