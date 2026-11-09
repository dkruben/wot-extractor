# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
from fun_random_common.fun_constants import BATTLE_MODE_VEH_TAGS_EXCEPT_FUN as BATTLE_MODE_VEH_TAGS_EXCEPT_FUN
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import LimitedLevelVehiclesWatcher as LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher as RestrictedVehiclesWatcher
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class FunRandomVehiclesWatcher(LimitedLevelVehiclesWatcher, RestrictedVehiclesWatcher, FunSubModesWatcher):
    __itemsCache: Any
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_FUN
    def start(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getAllowedVehicleTypes(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getForbiddenVehicleTypes(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getForbiddenVehicleClasses(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _getValidLevels(self):
        ...
