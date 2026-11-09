# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
import logging as logging
import typing as typing
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class BaseVehiclesWatcher(object):
    __itemsCache: Any
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEHICLE_TAGS
    _VEH_STATE_PRIORITIES: dict
    _isWatching: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getUnsuitableVehiclesBase(self):
        ...
    def _update(self, *_):
        ...
    def _getVehiclesCustomStates(self, onClear=False):
        ...
    def _clearCustomsStates(self):
        ...
    def __setCustomStates(self):
        ...
    def __compareVehStateByPriority(self, oldState, newState):
        ...

class LimitedLevelVehiclesWatcher(BaseVehiclesWatcher):
    __itemsCache: Any
    __validLevels: Any
    def __init__(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getValidLevels(self):
        ...

class RestrictedVehiclesWatcher(BaseVehiclesWatcher):
    __itemsCache: Any
    __allowedVehicleTypes: Any
    __forbiddenVehicleTypes: Any
    __forbiddenVehicleClasses: Any
    def __init__(self):
        ...
    def stop(self):
        ...
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getAllowedVehicleTypes(self):
        ...
    def _getForbiddenVehicleTypes(self):
        ...
    def _getForbiddenVehicleClasses(self):
        ...
