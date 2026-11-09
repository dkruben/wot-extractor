# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tournaments/tournament_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import random as random
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.match_model import MatchModel as MatchModel, MatchState as MatchState, MatchStage as MatchStage
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_model import TeamModel as TeamModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.tournament_view_model import TournamentViewModel as TournamentViewModel, OverviewState as OverviewState, Streaming as Streaming, PageState as PageState
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.ingame_tournament_helper import IngameTournamentMatchState as IngameTournamentMatchState, IngameTournamentUrlType as IngameTournamentUrlType, IngameTournamentLogoSize as IngameTournamentLogoSize, IngameTournamentBracketType as IngameTournamentBracketType
from helpers.ingame_tournament_helper import IngameTournamentType as IngameTournamentType
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE, getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController
from skeletons.gui.game_control import IIngameTournamentController as IIngameTournamentController
from typing import Optional as Optional
from gui.game_control.ingame_tournament_controller import _MatchData as _MatchData, _TeamData as _TeamData, _LeaderboardData as _LeaderboardData, _RewardData as _RewardData
_logger: Any

class TournamentView(ViewImpl):
    _TOURNAMENT_TYPE = None
    _TOURNAMENT_VIEW = None
    _MATCH_ROUND_TO_MATCH_STAGE: dict
    __BRACKET_TYPE_TO_MATCH_STAGE: dict
    __tournamentController: Any
    __externalLinksCtrl: Any
    _INGAME_TOURNAMENT_MATCH_STATE_TO_UI_STATE: dict
    _TIMER_UPDATE_RANDOM_DELTA = ONE_MINUTE
    _callbackDelayer: Any
    _data: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onGoToTokenStore(self):
        ...
    def _getMatchStage(self, matchData):
        ...
    def __updateTournamentData(self):
        ...
    def __onTournamentWGCGDataUpdated(self, data):
        ...
    def __fillModelData(self):
        ...
    def __getOverviewState(self):
        ...
    def __fillStreamingTypes(self):
        ...
    def __fillMatchData(self, matchModel, matchData):
        ...
    def __fillTeamData(self, teamModel, teamID, matchState=None, teamMatchScore=0):
        ...
    def __setUpdateCallback(self):
        ...
    def __onWatchStreamOne(self):
        ...
    def __onWatchStreamTwo(self):
        ...
    def __onGoToShop(self):
        ...
    def __onClose(self):
        ...
    def __onRefresh(self):
        ...
    def __pollServerTime(self):
        ...
