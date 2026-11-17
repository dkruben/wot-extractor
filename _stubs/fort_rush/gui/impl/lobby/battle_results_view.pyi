# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/battle_results_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel as PostBattleResultsViewModel
from fort_rush.gui.impl.lobby.presenters.fort_rush_battle_result_sub_presenter import FortRushBattleResultsSubPresenter as FortRushBattleResultsSubPresenter
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_HANGAR_ALIASES import FORT_RUSH_HANGAR_ALIASES as FORT_RUSH_HANGAR_ALIASES
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewFlags as ViewFlags
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.sounds.ambients import BattleResultsEnv as BattleResultsEnv
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService

class FortRushBattleResultsView(ViewImpl, IRoutableView):
    __battleResults: Any
    __sound_env__ = BattleResultsEnv
    __arenaUniqueID: Any
    __subPresenter: Any
    __router: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def arenaUniqueID(self):
        ...
    @property
    def viewModel(self):
        ...
    def getRouterModel(self):
        ...
    def createContextMenu(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...

class FortRushPostBattleResultsWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
