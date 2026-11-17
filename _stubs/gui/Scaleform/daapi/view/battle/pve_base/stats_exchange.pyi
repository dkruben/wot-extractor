# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from past.builtins import cmp as cmp
from TeamInfoLivesComponent import TeamInfoLivesComponent as TeamInfoLivesComponent
from constants import BOT_DISPLAY_STATUS as BOT_DISPLAY_STATUS
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController as ClassicStatisticsDataController, DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker as createExchangeBroker
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import vehicle as vehicle
from gui.Scaleform.daapi.view.battle.shared.stats_exchange.vehicle import BiSortedIDsComposer as BiSortedIDsComposer, AllySortedIDsComposer as AllySortedIDsComposer, EnemySortedIDsComposer as EnemySortedIDsComposer, VehicleInfoComponent as VehicleInfoComponent
from gui.battle_control.arena_info.settings import VehicleSpottedStatus as VehicleSpottedStatus, INVALIDATE_OP as INVALIDATE_OP
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey as VehicleInfoSortKey
from helpers import dependency as dependency
from pve_battle_hud import WidgetType as WidgetType
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO

class PveVehicleInfoSortKey(VehicleInfoSortKey):
    __slots__: tuple
    _sortAlive: Any
    def __init__(self, item):
        ...
    def _cmp(self, other):
        ...

class PveVehicleInfoSortKeyEnemyList(PveVehicleInfoSortKey):
    __slots__: tuple
    _sortAlive: Any
    def __init__(self, item):
        ...

class PveTeamsSortedIDsComposer(BiSortedIDsComposer):
    __slots__: tuple
    def __init__(self):
        ...

class PveVehicleInfoComponent(VehicleInfoComponent):
    _sessionProvider: Any
    _EMPTY_LIVES_COUNTER = -1
    def addVehicleInfo(self, vInfoVO, overrides):
        ...

class PveDynamicVehicleStatsComponent(DynamicVehicleStatsComponent):
    __slots__: tuple
    _sessionProvider: Any
    def get(self, forced=False):
        ...

class PveStatisticsDataController(ClassicStatisticsDataController):
    _sessionProvider: Any
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def _settingsChangeHandler(self, settingsID):
        ...
    def _onTeamLivesUpdated(self):
        ...
    def _createExchangeBroker(self, exchangeCtx):
        ...

def updatedInfoPredicate(isEnemy, settings):
    ...
