# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/presenters/fort_rush_vehicle_filters_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import copy as copy
import logging as logging
import typing as typing
from account_helpers.AccountSettings import FORT_RUSH_CAROUSEL_FILTER_1 as FORT_RUSH_CAROUSEL_FILTER_1, AccountSettings as AccountSettings
from fort_rush.gui.fort_rush_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.filters.carousel_filter import FILTER_KEYS as FILTER_KEYS, SessionCarouselFilter as SessionCarouselFilter
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider as VehicleFiltersDataProvider
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional
_logger: _Any

class FortRushBattleCarouselFilter(SessionCarouselFilter):
    _sessionProvider: _Any
    _clientSections: _Any
    _filters: _Any
    def __init__(self):
        ...
    def load(self):
        ...
    def save(self):
        ...
    @property
    def __respawnCtrl(self):
        ...
    def __getRetainedFilters(self):
        ...

class FortRushVehicleFiltersPresenter(VehicleFiltersDataProvider):
    def __init__(self):
        ...
    @classmethod
    def _getBaseSpecialSection(cls):
        ...
