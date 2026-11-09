# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchange/vehicle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.battle_control.arena_info import vos_collections as vos_collections
from gui.prestige.prestige_helpers import MAX_GRADE_ID as MAX_GRADE_ID
from gui.shared.badges import buildBadge as buildBadge
from helpers import dependency as dependency
from prestige_system import PrestigeConstants as PrestigeConstants
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class ISortedIDsComposer(object):
    __slots__: tuple
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class VehiclesSortedIDsComposer(broker.SingleSideComposer, ISortedIDsComposer):
    __slots__: tuple
    _items: Any
    def __init__(self, voField='vehiclesIDs', sortKey=...):
        ...
    def addSortIDs(self, isEnemy, arenaDP):
        ...
    def removeObserverIDs(self, arenaDP):
        ...

class AllySortedIDsComposer(VehiclesSortedIDsComposer):
    __slots__: tuple
    _items: Any
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class EnemySortedIDsComposer(VehiclesSortedIDsComposer):
    __slots__: tuple
    _items: Any
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class BiSortedIDsComposer(broker.BiDirectionComposer, ISortedIDsComposer):
    __slots__: tuple
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class TeamsSortedIDsComposer(BiSortedIDsComposer):
    __slots__: tuple
    def __init__(self, sortKey=...):
        ...

class TeamsCorrelationIDsComposer(BiSortedIDsComposer):
    __slots__: tuple
    def __init__(self):
        ...

class TotalStatsComposer(broker.IExchangeComposer):
    __slots__: tuple
    _stats: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def compose(self, data):
        ...
    def addTotalStats(self, stats):
        ...

class VehicleInfoComponent(broker.ExchangeComponent):
    __sessionProvider: Any
    __slots__: tuple
    _data: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def get(self, forced=False):
        ...
    def addVehicleInfo(self, vInfoVO, overrides):
        ...

class VehicleStatusComponent(broker.ExchangeComponent):
    __slots__: tuple
    _vehicleID: Any
    _status: Any
    _idsComposers: Any
    _statsComposers: Any
    _dogTag: Any
    def __init__(self, idsComposers=None, statsComposers=None):
        ...
    def clear(self):
        ...
    def get(self, forced=False):
        ...
    def addVehicleInfo(self, vInfoVO):
        ...
    def addTotalStats(self, stats):
        ...
    def addSortIDs(self, arenaDP):
        ...

class VehicleStatsComponent(broker.VehicleComponent):
    __slots__: tuple
    def addStats(self, vStatsVO):
        ...

class VehiclesExchangeBlock(broker.ExchangeBlock):
    __slots__: tuple
    _idsComposers: Any
    _statsComposers: Any
    def __init__(self, itemComponent, positionComposer=None, idsComposers=None, statsComposers=None):
        ...
    def clear(self):
        ...
    def get(self, forced=False):
        ...
    def addSortIDs(self, arenaDP, *flags):
        ...
    def addTotalStats(self, stats):
        ...
