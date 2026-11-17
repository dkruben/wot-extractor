# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/event_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from HWTeamInfoStatsComponent import HWTeamInfoStatsComponent as HWTeamInfoStatsComponent
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.gui_items.Vehicle import VEHICLE_BATTLE_TYPES_ORDER_INDICES as VEHICLE_BATTLE_TYPES_ORDER_INDICES
from gui.shared.utils import toUpper as toUpper
from halloween.gui.impl.gen.view_models.views.battle.event_stats_team_member_model import EventStatsTeamMemberModel as EventStatsTeamMemberModel
from halloween.gui.impl.gen.view_models.views.battle.event_stats_view_model import EventStatsViewModel as EventStatsViewModel
from halloween.gui.impl.gen.view_models.views.common.base_team_member_model import TeamMemberBanType as TeamMemberBanType
from halloween.gui.impl.gen.view_models.views.common.stat_column_settings_model import ColumnEnum as ColumnEnum
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class TeamStats(ViewImpl, IArenaVehiclesController):
    sessionProvider: Any
    __arenaDP: Any
    def __init__(self, flags=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def vehicleStats(self):
        ...
    def invalidateArenaInfo(self):
        ...
    def invalidateVehiclesStats(self, arenaDP):
        ...
    def addVehicleInfo(self, vo, arenaDP):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        ...
    def updateVehiclesStats(self, updated, arenaDP):
        ...
    def _onTeamLivesUpdated(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __createTeamMember(self, index, vInfo):
        ...
    def __updateBuffs(self, vehID, memberStats):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateColumns(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateStats(self, model=None):
        ...
    def __updateStatsOnChangeParams(self, *args, **kwars):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __sortTeammates(self, userVOs):
        ...
