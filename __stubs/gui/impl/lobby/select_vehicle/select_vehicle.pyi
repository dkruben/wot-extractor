# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/select_vehicle/select_vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
import typing as typing
from account_helpers.AccountSettings import AccountSettings as AccountSettings, SELECT_VEHICLES_PLAYLIST as SELECT_VEHICLES_PLAYLIST, SELECT_VEHICLES_IS_ALL_VEHICLES as SELECT_VEHICLES_IS_ALL_VEHICLES
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.select_vehicle.select_vehicle_model import SelectVehicleModel as SelectVehicleModel
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider as VehicleFiltersDataProvider
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter as VehicleInventoryPresenter
from gui.impl.lobby.hangar.presenters.vehicle_playlists_presenter import VehiclePlaylistsPresenter as VehiclePlaylistsPresenter
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter as VehiclesStatisticsPresenter
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter as VehiclesInfoPresenter
from gui.impl.lobby.select_vehicle.filter import SelectVehiclesCarouselFilter as SelectVehiclesCarouselFilter
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
ALL_VEHICLES_CRITERIA: Any

class SelectVehicleTitles(Enum):
    SELECT_ATTACKER = 'selectAttackerTitle'

class VehiclePlaylistsPresenterSession(VehiclePlaylistsPresenter):
    def _getSelectedID(self):
        ...
    def _setSelectedID(self, plID):
        ...

# base nao representavel no stub: ViewComponent[...]
class SelectVehicleView:
    _onSelectCallback: Any
    _randomVehicleFilter: Any
    _randomInvVehicleFilter: Any
    _carouselFilter: Any
    _accountStyles: Any
    _title: Any
    _currentVehicleCD: Any
    def __init__(self, title, onSelectCallback, currentVehicleCD=0):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getChildComponents(self):
        ...
    def _getEvents(self):
        ...
    def _onIsAllVehiclesChange(self, args):
        ...
    def _onSelect(self, args):
        ...

class SelectVehicleWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, title, onSelectCallback, currentVehicleCD=0):
        ...
