# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_leagues.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.ranked_battles.ranked_builders import leagues_vos as leagues_vos
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from gui.ranked_battles import ranked_helpers as ranked_helpers
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.meta.RankedBattlesLeaguesViewMeta import RankedBattlesLeaguesViewMeta as RankedBattlesLeaguesViewMeta
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache

class RankedBattlesLeaguesView(RankedBattlesLeaguesViewMeta, IResetablePage):
    rankedController: Any
    itemsCache: Any
    def reset(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __dossierUpdateCallBack(self, *_):
        ...
    def __onWebSeasonInfoUpdate(self):
        ...
    def __onRankedUpdate(self):
        ...
    def __setBonusBattlesCount(self):
        ...
    def __setEfficiencyData(self):
        ...
    def __setEmptyLeagueAndPositionData(self):
        ...
    def __setLeagueAndPositionData(self):
        ...
    def __setStatsData(self):
        ...
