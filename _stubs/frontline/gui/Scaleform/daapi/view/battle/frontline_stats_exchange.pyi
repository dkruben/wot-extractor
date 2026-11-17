# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frontline.gui.Scaleform.daapi.view.meta.FrontlineBattleStatisticDataControllerMeta import FrontlineBattleStatisticDataControllerMeta as FrontlineBattleStatisticDataControllerMeta
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker as createExchangeBroker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import vehicle as vehicle
from gui.battle_control.arena_info import vos_collections as vos_collections
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.battle_control.arena_info.arena_vos import EPIC_BATTLE_KEYS as EPIC_BATTLE_KEYS
from gui.battle_control import avatar_getter as avatar_getter
_logger: Any

class EpicStatsComponent(DynamicVehicleStatsComponent):
    __slots__: tuple
    _rank: Any
    _lane: Any
    _hasRespawns: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def get(self, forced=False):
        ...
    def addStats(self, vStatsVO):
        ...

class FrontlineStatisticsDataController(FrontlineBattleStatisticDataControllerMeta):
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def invalidateArenaInfo(self):
        ...
    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        ...
    def _populate(self):
        ...
    def _createExchangeBroker(self, exchangeCtx):
        ...
    def _createExchangeCollector(self):
        ...
    def __getStatsComponentClass(self):
        ...
    def __onPlayerStatsUpdated(self, *args):
        ...
    def as_setFragsS(self, data):
        ...
    def as_updateVehiclesStatsS(self, data):
        ...
