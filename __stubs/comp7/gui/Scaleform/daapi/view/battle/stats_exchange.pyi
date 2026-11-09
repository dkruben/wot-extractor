# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/battle/stats_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import VOIP as VOIP
from comp7.gui.Scaleform.daapi.view.meta.Comp7BattleStatisticDataControllerMeta import Comp7BattleStatisticDataControllerMeta as Comp7BattleStatisticDataControllerMeta
from comp7.gui.Scaleform.genConsts.TOOLTIPS_BATTLE_CONSTANTS import TOOLTIPS_BATTLE_CONSTANTS as TOOLTIPS_BATTLE_CONSTANTS
from comp7.gui.battle_control.arena_info import vos_collections as vos_collections
from comp7.gui.battle_control.arena_info.arena_vos import Comp7Keys as Comp7Keys
from comp7.gui.impl.lobby.comp7_helpers.comp7_i18n_helpers import RANK_MAP as RANK_MAP, DIVISION_MAP as DIVISION_MAP
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys as Comp7CoreKeys
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from constants import ROLE_TYPE_TO_LABEL as ROLE_TYPE_TO_LABEL
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import DynamicVehicleStatsComponent as DynamicVehicleStatsComponent
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.stats_exchange import PointsOfInterestStatsController as PointsOfInterestStatsController
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker as broker, createExchangeBroker as createExchangeBroker, vehicle as vehicle
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class Comp7VehicleInfoComponent(vehicle.VehicleInfoComponent):
    __slots__: tuple
    __sessionProvider: Any
    __comp7Controller: Any
    __itemsCache: Any
    def addVehicleInfo(self, vInfoVO, overrides):
        ...
    @classmethod
    def __getVoiceChatConnected(cls, vInfoVO):
        ...
    def __isSuperSquad(self, vInfoVO):
        ...

class Comp7StatisticsDataController(Comp7BattleStatisticDataControllerMeta):
    __poiStatsController: Any
    __arenaInfoComponent: Any
    def __init__(self):
        ...
    def _createExchangeBroker(self, exchangeCtx):
        ...
    def _getArenaWinTextShort(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def __onChannelUpdated(self, *_, **__):
        ...
