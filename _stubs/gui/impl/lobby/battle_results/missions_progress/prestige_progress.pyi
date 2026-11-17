# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/prestige_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import Configs as Configs
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.progression.prestige_progress_model import PrestigeProgressModel as PrestigeProgressModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prestige.prestige_helpers import fillPrestigeEmblemModel as fillPrestigeEmblemModel, hasVehiclePrestige as hasVehiclePrestige, showPrestigeVehicleStats as showPrestigeVehicleStats
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

# base nao representavel no stub: ViewComponent[...]
class PrestigeProgressPresenter(IProgressionCategoryPresenter):
    __lobbyContext: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __progress: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, *args, **kwargs):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    # decorador original: @args2params(...)
    def __onNavigate(self, vehCD):
        ...
    def __onServerSettingChanged(self, diff):
        ...
