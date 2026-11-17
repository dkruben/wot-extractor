# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher as BaseVehiclesWatcher
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import FORBIDDEN_VEHICLE_TAGS as FORBIDDEN_VEHICLE_TAGS

class VehiclesWatcher(BaseVehiclesWatcher):
    itemsCache: Any
    lsCtrl: Any
    def _getUnsuitableVehicles(self, onClear=False):
        ...
