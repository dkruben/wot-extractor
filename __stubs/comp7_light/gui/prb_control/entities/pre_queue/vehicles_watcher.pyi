# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
import typing as typing
from comp7_light_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT as BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT, Configs as Configs
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher as LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher as RestrictedVehiclesWatcher
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class Comp7LightVehiclesWatcher(LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher):
    __comp7LightController: Any
    __lobbyContext: Any
    __itemsCache: Any
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT
    def start(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getAllowedVehicleTypes(self):
        ...
    def _getValidLevels(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
