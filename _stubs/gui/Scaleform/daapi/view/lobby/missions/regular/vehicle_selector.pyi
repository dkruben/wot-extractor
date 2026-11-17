# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/vehicle_selector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from account_helpers.AccountSettings import MISSION_SELECTOR_FILTER as MISSION_SELECTOR_FILTER, AccountSettings as AccountSettings
from gui.filters.carousel_filter import CarouselFilter as CarouselFilter, EventCriteriesGroup as EventCriteriesGroup
from gui.Scaleform import getButtonsAssetPath as getButtonsAssetPath
from gui.Scaleform.daapi.view.lobby.missions.vehicle_selector import MissionVehicleSelector as MissionVehicleSelector, MissionVehicleSelectorCarousel as MissionVehicleSelectorCarousel, SelectorCriteriesGroup as SelectorCriteriesGroup
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER as TANK_CAROUSEL_FILTER
from gui.server_events import caches as caches
from gui.shared.formatters import text_styles as text_styles
from helpers.i18n import makeString as ms

class RegularMissionVehicleSelector(MissionVehicleSelector):
    def _getTitle(self):
        ...
    @classmethod
    def _getCarouselAlias(cls):
        ...
    def _getNotAvailableStatusText(self):
        ...

class RegularVehicleSelectorCarousel(MissionVehicleSelectorCarousel):
    _carouselFilterCls: Any
    def __init__(self):
        ...
    def _setCarouselFilters(self):
        ...

class _RegularCarouselFilter(CarouselFilter):
    _serverSections: Any
    _criteriesGroups: Any
    _filters: Any
    def __init__(self):
        ...
    def load(self):
        ...
    def save(self):
        ...
