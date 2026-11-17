# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController as ClassicStatisticsDataController, DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker, vehicle as vehicle, createExchangeBroker as createExchangeBroker
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey as VehicleInfoSortKey
from gui.shared.gui_items.Vehicle import VEHICLE_BATTLE_TYPES_ORDER_INDICES as VEHICLE_BATTLE_TYPES_ORDER_INDICES
from gui.shared.utils import toUpper as toUpper

class HWSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class HWEnemySortedIDsComposer(vehicle.EnemySortedIDsComposer):
    __slots__: tuple
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class HWEnemySingleSideComposer(broker.SingleSideComposer):
    __slots__: tuple
    def compose(self, data):
        ...
    def addItem(self, _, data):
        ...

class HWTeamsSortedIDsComposer(vehicle.TeamsSortedIDsComposer):
    __slots__: tuple
    _right: Any
    def __init__(self, sortKey=...):
        ...

class HWTeamsCorrelationIDsComposer(vehicle.TeamsCorrelationIDsComposer):
    __slots__: tuple
    _right: Any
    def __init__(self):
        ...

class HWBiDirectionComposer(broker.BiDirectionComposer):
    __slots__: tuple
    _right: Any
    def __init__(self):
        ...

class HWStatisticsDataController(ClassicStatisticsDataController):
    __poiStatsController: Any
    __arenaInfoComponent: Any
    def __init__(self):
        ...
    def _createExchangeBroker(self, exchangeCtx):
        ...
