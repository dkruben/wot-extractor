# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/vos_collections.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lmap as lmap
from past.builtins import cmp as cmp
from gui.shared.sort_key import SortKey as SortKey
from gui.battle_control.arena_info.arena_vos import EPIC_RANDOM_KEYS as EPIC_RANDOM_KEYS, EPIC_BATTLE_KEYS as EPIC_BATTLE_KEYS

class VehicleInfoSortKey(SortKey):
    __slots__: tuple
    vInfoVO: Any
    vStatsVO: Any
    def __init__(self, item):
        ...
    def _cmp(self, other):
        ...

class SquadmanVehicleInfoSortKey(VehicleInfoSortKey):
    __slots__: tuple
    prebattleID: Any
    def __init__(self, prebattleID, item):
        ...
    def _cmp(self, other):
        ...

class SpawnGroupVehicleInfoSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class RankedVehicleInfoSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class SquadmanSpawnGroupVehicleInfoSortKey(SpawnGroupVehicleInfoSortKey):
    __slots__: tuple
    prebattleID: Any
    def __init__(self, prebattleID, item):
        ...
    def _cmp(self, other):
        ...

class FragCorrelationSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class RespawnSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class RankSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class EpicRankSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class _Collection(object):
    __slots__: tuple
    _sortKey: Any
    def __init__(self, sortKey=None):
        ...
    def count(self, arenaDP):
        ...
    def iterator(self, arenaDP):
        ...
    def ids(self, arenaDP):
        ...
    def _buildSeq(self, arenaDP):
        ...
    def _sortIfNeed(self, seq):
        ...
    def _getID(self, item):
        ...

class VehiclesInfoCollection(_Collection):
    __slots__: tuple
    def _buildSeq(self, arenaDP):
        ...

class TeamVehiclesInfoCollection(_Collection):
    __slots__: tuple
    _team: Any
    def __init__(self, team, sortKey=None):
        ...
    def _buildSeq(self, arenaDP):
        ...

class VehiclesItemsCollection(_Collection):
    __slots__: tuple
    def _buildSeq(self, arenaDP):
        ...
    def _getID(self, item):
        ...

class ActiveVehiclesItemsCollection(VehiclesItemsCollection):
    def _buildSeq(self, arenaDP):
        ...

class AllyItemsCollection(VehiclesItemsCollection):
    __slots__: tuple
    def _buildSeq(self, arenaDP):
        ...

class EnemyItemsCollection(VehiclesItemsCollection):
    __slots__: tuple
    def _buildSeq(self, arenaDP):
        ...

class AliveItemsCollection(VehiclesItemsCollection):
    __slots__: tuple
    _collection: Any
    def __init__(self, collection):
        ...
    def _buildSeq(self, arenaDP):
        ...
