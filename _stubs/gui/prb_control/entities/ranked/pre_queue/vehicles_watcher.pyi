# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/ranked/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from itertools import chain as chain
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import RestrictedVehiclesWatcher as RestrictedVehiclesWatcher
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency, server_settings as server_settings
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class RankedVehiclesWatcher(RestrictedVehiclesWatcher):
    __itemsCache: Any
    __lobbyContext: Any
    def start(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getForbiddenVehicleClasses(self):
        ...
    def _getForbiddenVehicleTypes(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
