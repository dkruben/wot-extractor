# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_selector_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lrange as lrange, viewvalues as viewvalues
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui.Scaleform.genConsts.VEHICLE_SELECTOR_CONSTANTS import VEHICLE_SELECTOR_CONSTANTS as VEHICLE_SELECTOR_CONSTANTS
from gui.shared.formatters.vehicle_filters import packVehicleTypesFilter as packVehicleTypesFilter, packVehicleLevelsFilter as packVehicleLevelsFilter, packNationsFilter as packNationsFilter
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA

class VehicleSelectorBase(object):
    __filters: Any
    _levelsRange: Any
    showNotReadyVehicles: Any
    _filterVisibility: Any
    _compatibleOnlyLabel: Any
    def __init__(self):
        ...
    def getFilters(self):
        ...
    def _updateFilter(self, nation=-1, vehicleType='none', isMain=False, level=-1, compatibleOnly=False):
        ...
    def _updateData(self, allVehicles, compatiblePredicate=...):
        ...
    def _parseFilters(self):
        ...
    def _initFilter(self, nation=-1, vehicleType='none', isMain=False, level=-1, compatibleOnly=False):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
