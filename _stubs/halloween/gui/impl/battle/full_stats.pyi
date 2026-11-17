# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/battle/full_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from HWArenaInfoBossHealthBarComponent import getArenaInfoBossHealthBarComponent as getArenaInfoBossHealthBarComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from HWTeamInfoStatsComponent import HWTeamInfoStatsComponent as HWTeamInfoStatsComponent
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from halloween.gui.game_control.halloween_anomalies_controller import AnomalyData as AnomalyData
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.impl.gen.view_models.views.battle.full_stats_view_model import FullStatsViewModel as FullStatsViewModel
from halloween.gui.impl.gen.view_models.views.common.anomaly_model import AnomalyModel as AnomalyModel, AnomalyType as AnomalyType
from halloween.gui.impl.lobby.widgets.event_stats import TeamStats as TeamStats
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween_common.halloween_constants import ARENA_BONUS_TYPE_TO_LEVEL as ARENA_BONUS_TYPE_TO_LEVEL
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class TabScreen(ViewImpl):
    _sessionProvider: Any
    _hwAnomaliesCtrl: Any
    _currentGoal: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def vehicleStats(self):
        ...
    @property
    def arenaPhases(self):
        ...
    @property
    def battleGUICtrl(self):
        ...
    @property
    def viewModel(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateHeader(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBuffs(self, model=None):
        ...
    def __onPhaseChanged(self):
        ...
    def __onBattleGoalChanged(self, goalName):
        ...
    def __prepareGoal(self, goalName):
        ...
    def __onBossVulnerableChanged(self, isBossVulnerable):
        ...
    def __onBossHPBarVisibilityChanged(self, isBossHPBarVisible):
        ...

class FullEventStatsWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
