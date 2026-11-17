# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_season_gap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from helpers import dependency as dependency, time_utils as time_utils
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.ranked_battles.ranked_builders import season_gap_vos as season_gap_vos
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from gui.ranked_battles.constants import SeasonResultTokenPatterns as SeasonResultTokenPatterns, RankedDossierKeys as RankedDossierKeys, ZERO_RANK_ID as ZERO_RANK_ID, SeasonGapStates as SeasonGapStates, NOT_IN_LEAGUES_QUEST as NOT_IN_LEAGUES_QUEST
from gui.Scaleform.daapi.view.meta.RankedBattlesSeasonGapViewMeta import RankedBattlesSeasonGapViewMeta as RankedBattlesSeasonGapViewMeta
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.shared.utils.scheduled_notifications import PeriodicNotifier as PeriodicNotifier
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.server_events import IEventsCache as IEventsCache
_STATE_TO_READY_GAP_STATE: dict
_STATE_TO_BANNED_GAP_STATE: dict
_STATE_TO_ROLLED_GAP_STATE: dict

class RankedBattlesSeasonGapView(RankedBattlesSeasonGapViewMeta, IResetablePage):
    __eventsCache: Any
    __itemsCache: Any
    __rankedController: Any
    __TOKENS_ORDER: tuple
    __slots__: tuple
    __periodicNotifier: Any
    __prevSeason: Any
    __dossier: Any
    __resultState: Any
    __resultLeague: Any
    __isSprinter: Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def onBtnClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getResultTokenPattern(self):
        ...
    def __getNotLeagueQuest(self):
        ...
    def __getTillUpdateTime(self):
        ...
    def __hasSprinterToken(self):
        ...
    def __onTokensUpdate(self, _):
        ...
    def __update(self):
        ...
    def __updateData(self):
        ...
    def __updateEfficiency(self):
        ...
    def __updateRating(self):
        ...
    def __updateStateByDossier(self):
        ...
    def __updateStateByTokens(self):
        ...
