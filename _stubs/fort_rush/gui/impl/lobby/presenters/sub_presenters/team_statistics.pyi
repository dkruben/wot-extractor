# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/sub_presenters/team_statistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fort_rush_common.fort_rush_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from fort_rush.gui.fort_rush_presenters_packers import FortRushTeamEfficiency as FortRushTeamEfficiency
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_team_stats_model import BattleTeamStatsModel as BattleTeamStatsModel
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.battle_results.pbs_helpers.team_stats_helpers import getPlayerContextMenuArgs as getPlayerContextMenuArgs
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.backport import createContextMenuData as createContextMenuData, BackportContextMenuWindow as BackportContextMenuWindow
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from frameworks.wulf import ViewModel as ViewModel

class FortRushTeamStatisticsSubPresenter(BattleResultsSubPresenter):
    __connectionMgr: Any
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createContextMenu(self, event):
        ...
    def _getEvents(self):
        ...
    def __getContextMenuArgs(self, databaseID, vehicleCD):
        ...
    def __onTeamStatsSorted(self, event):
        ...
