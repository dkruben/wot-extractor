# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_team_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fun_random_common.fun_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from fun_random.gui.battle_results.packers.fun_packers import FunRandomTeamStats as FunRandomTeamStats
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_team_stats_model import FunTeamStatsModel as FunTeamStatsModel
from gui.battle_results.pbs_helpers.team_stats_helpers import getPlayerContextMenuArgs as getPlayerContextMenuArgs
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen import R as R
from gui.impl.backport import BackportContextMenuWindow as BackportContextMenuWindow, createContextMenuData as createContextMenuData
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FunTeamStatsSubPresenter(BattleResultsSubPresenter):
    __connectionMgr: Any
    _CONTEXT_MENU_TYPE = CONTEXT_MENU_HANDLER_TYPE.BATTLE_RESULTS_USER
    _PACKER_CLS = FunRandomTeamStats
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createContextMenu(self, event):
        ...
    def _getEvents(self):
        ...
    def __getBackportContextMenuData(self, databaseID, vehicleCD):
        ...
    def __getContextMenuArgs(self, databaseID, vehicleCD):
        ...
    def __onTeamStatsSorted(self, event):
        ...
