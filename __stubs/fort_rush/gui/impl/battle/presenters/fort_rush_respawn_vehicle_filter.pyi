# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/battle/presenters/fort_rush_respawn_vehicle_filter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING, Dict as Dict
import BigWorld as BigWorld
import Event as Event
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from fort_rush_common.component_helpers import getVehicleRespawnComponent as getVehicleRespawnComponent
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.fitting_item import RentalInfoProvider as RentalInfoProvider
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from event_platform.gui.shared.events import RespawnFrameworkEvent as RespawnFrameworkEvent
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria

class FortRushRespawnVehicleFilter(IVehicleFilter):
    __slots__: tuple
    _itemsFactory: Any
    _fortRushCtrl: Any
    onDiff: Any
    _vehicles: Any
    __criteria: Any
    def __init__(self):
        ...
    @property
    def criteria(self):
        ...
    @property
    def vehicles(self):
        ...
    def initialize(self):
        ...
    def _buildCriteria(self):
        ...
    def destroy(self):
        ...
    def _onVehiclesLoaded(self, _):
        ...
