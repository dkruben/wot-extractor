# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/team_statistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.pbs_helpers.team_stats_helpers import getPlayerContextMenuArgs as getPlayerContextMenuArgs
from gui.impl.backport import createContextMenuData as createContextMenuData, BackportContextMenuWindow as BackportContextMenuWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_team_stats_model import RandomTeamStatsModel as RandomTeamStatsModel
from gui.impl.lobby.battle_results.random_packers import RandomTeamEfficiency as RandomTeamEfficiency
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from frameworks.wulf import ViewModel as ViewModel

class TeamStatisticsSubPresenter(BattleResultsSubPresenter):
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
