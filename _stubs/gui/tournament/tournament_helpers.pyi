# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/tournament/tournament_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import TOURNAMENT_CONFIG as TOURNAMENT_CONFIG
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.functions import getUniqueViewName as getUniqueViewName
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import Optional as Optional, Dict as Dict
from helpers.server_settings import _TournamentSettings as _TournamentSettings
from gui.Scaleform.daapi.view.lobby import BrowserView as BrowserView

# decorador original: @dependency.replace_none_kwargs(...)
def getTournamentsConfig(lobbyCtx=None):
    ...
def isTournamentEnabled():
    ...
def showTournaments(url=None):
    ...
def _serverSettingChanged(browser, diff):
    ...
def getIgbHost():
    ...
