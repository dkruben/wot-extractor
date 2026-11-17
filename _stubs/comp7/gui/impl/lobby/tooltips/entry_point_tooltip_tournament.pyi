# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/entry_point_tooltip_tournament.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.enums import TournamentName as TournamentName
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.tournament_entry_point_tooltip_model import TournamentEntryPointTooltipModel as TournamentEntryPointTooltipModel, TournamentState as TournamentState
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from helpers.ingame_tournament_helper import IngameTournamentState as IngameTournamentState
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from math_common import round_py2_style_int as round_py2_style_int
from skeletons.gui.game_control import IIngameTournamentController as IIngameTournamentController
from helpers.ingame_tournament_helper import IngameTournamentType as IngameTournamentType

class Comp7TournamentEntryPointTooltip(ViewImpl):
    __ingameTournamentController: Any
    __tournamentStateTooltipStateMap: dict
    __tournamentType: Any
    def __init__(self, tounamentType):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onStatusUpdated(self, _):
        ...
    def _onStatusTick(self):
        ...
    def _updateState(self):
        ...
