# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/battle_session_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from constants import TOURNAMENT_CONFIG as TOURNAMENT_CONFIG
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.battle_session_model import BattleSessionModel as BattleSessionModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.impl.lobby.hangar.presenters.utils import fillMenuSharedItems as fillMenuSharedItems, navigateTo as navigateTo
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.shared.events import LoadViewEvent as LoadViewEvent
from gui.shared.view_helpers.emblems import getClanEmblemURL as getClanEmblemURL, EmblemSize as EmblemSize
from gui.tournament.tournament_helpers import isTournamentEnabled as isTournamentEnabled, showTournaments as showTournaments
from helpers import dependency as dependency
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_TOURNAMENTS_URL = 'tournamentsURL'
_GLOBAL_MAP_URL = 'globalMapURL'

class BattleSessionView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    __externalLinks: Any
    __lobbyContext: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self):
        ...
    def __updateModel(self):
        ...
    def __tournamentsClickedHandler(self):
        ...
    def __globalMapClickedHandler(self):
        ...
    def __clanClickedHandler(self):
        ...
    # decorador original: @adisp_process
    def __openUrl(self, name):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __updateMenuItems(self):
        ...
