# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker, vehicle as vehicle, createExchangeBroker as createExchangeBroker
from gui.battle_control.arena_info.vos_collections import VehicleInfoSortKey as VehicleInfoSortKey
from gui.shared.gui_items.Vehicle import VEHICLE_BATTLE_TYPES_ORDER_INDICES as VEHICLE_BATTLE_TYPES_ORDER_INDICES
from gui.shared.utils import toUpper as toUpper
from last_stand.gui.scaleform.daapi.view.meta.LSBattleStatisticDataControllerMeta import LSBattleStatisticDataControllerMeta as LSBattleStatisticDataControllerMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from last_stand.gui.battle_control.arena_info.arena_vos import LSKeys as LSKeys

class LSVehicleInfoComponent(vehicle.VehicleInfoComponent):
    __slots__: tuple
    __sessionProvider: Any
    def addVehicleInfo(self, vInfoVO, overrides):
        ...
    @classmethod
    def __getVoiceChatConnected(cls, vInfoVO):
        ...

class LSSortKey(VehicleInfoSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...

class LSEnemySortedIDsComposer(vehicle.EnemySortedIDsComposer):
    __slots__: tuple
    def addSortIDs(self, isEnemy, arenaDP):
        ...

class LSEnemySingleSideComposer(broker.SingleSideComposer):
    __slots__: tuple
    def compose(self, data):
        ...
    def addItem(self, _, data):
        ...

class LSTeamsSortedIDsComposer(vehicle.TeamsSortedIDsComposer):
    __slots__: tuple
    _right: Any
    def __init__(self, sortKey=...):
        ...

class LSTeamsCorrelationIDsComposer(vehicle.TeamsCorrelationIDsComposer):
    __slots__: tuple
    _right: Any
    def __init__(self):
        ...

class LSBiDirectionComposer(broker.BiDirectionComposer):
    __slots__: tuple
    _right: Any
    def __init__(self):
        ...

class LSStatisticsDataController(LSBattleStatisticDataControllerMeta):
    __poiStatsController: Any
    __arenaInfoComponent: Any
    def __init__(self):
        ...
    def _createExchangeBroker(self, exchangeCtx):
        ...
