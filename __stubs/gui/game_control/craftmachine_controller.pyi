# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/craftmachine_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
from adisp import adisp_process as adisp_process
from constants import EnhancementsConfig as config
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN as BATTLE_MODE_VEH_TAGS_EXCEPT_CLAN
from helpers import dependency as dependency
from gui.wgcg.craftmachine.contexts import CraftmachineModulesInfoCtx as CraftmachineModulesInfoCtx
from gui.wgcg.states import WebControllerStates as WebControllerStates
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import ICraftmachineController as ICraftmachineController
from skeletons.gui.web import IWebController as IWebController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class CraftmachineController(ICraftmachineController):
    __webController: Any
    __lobbyCtx: Any
    __itemsCache: Any
    __modules: Any
    __enabledSync: Any
    __enabled: Any
    def __init__(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def getModuleName(self, module):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    # decorador original: @adisp_process
    def __updateModulesInfo(self):
        ...
    @staticmethod
    def __filterEnabledVehiclesCriteria(criteria):
        ...
    def __vehicleIsAvailableForRestore(self):
        ...
    def __vehicleIsAvailableForBuy(self):
        ...
    def __suitableVehicleIsAvailable(self):
        ...
    def __hasSuitableVehicles(self):
        ...
