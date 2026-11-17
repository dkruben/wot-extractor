# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import BattleStatisticsDataController as BattleStatisticsDataController
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker as createExchangeBroker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import vehicle as vehicle
from gui.battle_control.arena_info.arena_vos import ChatCommandVO as ChatCommandVO
from gui.battle_control.arena_info.settings import VehicleSpottedStatus as VehicleSpottedStatus
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from helpers import dependency as dependency

class FragsCollectableStats(broker.CollectableStats):
    __slots__: tuple
    __teamsDeaths: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def addVehicleStatsUpdate(self, vInfoVO, vStatsVO):
        ...
    def addVehicleStatusUpdate(self, vInfoVO):
        ...
    def getTotalStats(self, arenaVisitor, sessionProvider):
        ...

class DynamicVehicleStatsComponent(vehicle.VehicleStatsComponent):
    settingsCore: Any
    __slots__: tuple
    _frags: Any
    _chatCommand: Any
    _chatCommandFlags: Any
    _spottedStatus: Any
    _vehicleID: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def get(self, forced=False):
        ...
    def addStats(self, vStatsVO):
        ...

class ClassicStatisticsDataController(BattleStatisticsDataController):
    def _createExchangeBroker(self, exchangeCtx):
        ...
    def _createExchangeCollector(self):
        ...
