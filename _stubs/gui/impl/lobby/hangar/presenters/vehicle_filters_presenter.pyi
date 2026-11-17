# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_filters_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as typing
import BigWorld as BigWorld
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.options import CarouselTypeSetting as CarouselTypeSetting
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from gui import GUI_NATIONS as GUI_NATIONS
from gui.filters.carousel_filter import FILTER_KEYS as FILTER_KEYS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass import BattlePassFilterConsts as BattlePassFilterConsts
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_filter_model import VehicleFilterModel as VehicleFilterModel, FilterSection as FilterSection, RoleSection as RoleSection
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.settings import VEHICLE_LEVELS as VEHICLE_LEVELS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER, VEHICLE_ROLES_LABELS_BY_CLASS as VEHICLE_ROLES_LABELS_BY_CLASS, VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from typing import List as List, Dict as Dict
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter
_VEHICLE_LEVEL_FILTERS: list
_CAROUSEL_ROW_COUNT_TYPE: dict

# base nao representavel no stub: ViewComponent[...]
class VehicleFiltersDataProvider:
    __settingsCore: Any
    __filter: Any
    __rowCount: Any
    __mapping: Any
    def __init__(self, carouselFilter):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    @classmethod
    def _getBaseSpecialSection(cls):
        ...
    def _generateMappings(self):
        ...
    def __onResetFilter(self):
        ...
    def __convertSection(self, sectionKey, filters):
        ...
    def __convertToModel(self, filters):
        ...
    def __updateModel(self):
        ...
    def __onSaveFilter(self, args):
        ...
    def __onCarouselSettingsChange(self, diff):
        ...
    def __onCarouselTypeChanged(self, args):
        ...
    def __updateCarousel(self):
        ...
