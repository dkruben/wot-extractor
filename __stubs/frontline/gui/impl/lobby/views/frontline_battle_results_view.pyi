# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/frontline_battle_results_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.constants.aliases import FrontlineHangarAliases as FrontlineHangarAliases
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, ViewFlags as ViewFlags
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from helpers import dependency as dependency
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel as PostBattleResultsViewModel
from frontline.gui.impl.lobby.presenters.frontline_battle_result_sub_presenter import FrontlineBattleResultsSubPresenter as FrontlineBattleResultsSubPresenter
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService

class FrontlineBattleResultsView(ViewImpl, IRoutableView):
    __battleResults: Any
    __connectionMgr: Any
    __localStorage = ''
    __arenaUniqueID: Any
    __subPresenter: Any
    __router: Any
    def __init__(self, ctx, *args, **kwargs):
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
    @classmethod
    def getLocalStorage(cls):
        ...
    @classmethod
    def saveLocalStorage(cls, ctx):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onClose(self):
        ...

class FrontlinePostBattleResultsWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
