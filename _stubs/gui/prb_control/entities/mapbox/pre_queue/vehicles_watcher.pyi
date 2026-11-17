# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/mapbox/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
from constants import Configs as Configs
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher as LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher as RestrictedVehiclesWatcher
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class MapboxVehiclesWatcher(LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher):
    __mapboxCtrl: Any
    __lobbyContext: Any
    __itemsCache: Any
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
    def _getValidLevels(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
