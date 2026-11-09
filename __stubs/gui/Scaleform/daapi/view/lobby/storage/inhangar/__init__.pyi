# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import constants as constants
import nations as nations
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.AccountSettings import STORAGE_VEHICLES_CAROUSEL_FILTER_1 as STORAGE_VEHICLES_CAROUSEL_FILTER_1
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.filters.carousel_filter import SessionCarouselFilter as SessionCarouselFilter, EventCriteriesGroup as EventCriteriesGroup, CriteriesGroup as CriteriesGroup
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_data_provider import CarouselDataProvider as CarouselDataProvider
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageVehicleVo as getStorageVehicleVo, isStorageSessionTimeout as isStorageSessionTimeout
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils import makeSearchableString as makeSearchableString
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA

class _ShortNameVehiclesCriteriesGroup(CriteriesGroup):
    _criteria: Any
    @staticmethod
    def isApplicableFor(vehicle):
        ...
    def update(self, filters):
        ...

class StorageCarouselFilter(SessionCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    _filters: Any
    def __init__(self, criteries=None):
        ...
    def load(self):
        ...

class StorageCarouselDataProvider(CarouselDataProvider):
    _baseCriteria: Any
    def _setBaseCriteria(self):
        ...
    def _buildVehicle(self, vehicle):
        ...
    def _getVehicleStats(self, vehicle):
        ...
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        ...
