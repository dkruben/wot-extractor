# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_hidden_vehicles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CURRENT_VEHICLE as CURRENT_VEHICLE
from adisp import adisp_process as adisp_process
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from fun_random.gui.feature.util.fun_helpers import getVehicleComparisonKey as getVehicleComparisonKey
from fun_random.gui.fun_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from fun_random.gui.shared.gui_items.vehicle import isOnlyFunRandomVehicle as isOnlyFunRandomVehicle
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IPrbListener as IPrbListener
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from skeletons.gui.shared import IItemsCache as IItemsCache
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode

class FunHiddenVehicles(IFunRandomController.IFunHiddenVehicles, IPrbListener):
    __itemsCache: Any
    __subModes: Any
    def __init__(self, subModesHolder):
        ...
    def fini(self):
        ...
    def startVehiclesListening(self):
        ...
    def stopVehiclesListening(self):
        ...
    def updateCurrentVehicle(self, desiredSubMode):
        ...
    # decorador original: @adisp_process
    def __onSelectVehicleInHangar(self, event):
        ...
