# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/ranked/year_leaderboard_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import CURRENT_REALM as CURRENT_REALM
from dossiers2.ui.achievements import BADGES_BLOCK as BADGES_BLOCK
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.ranked.year_leaderboard_view_model import YearLeaderboardViewModel as YearLeaderboardViewModel
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.utils import getPlayerName as getPlayerName
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class YearLeaderboardView(ViewImpl):
    __slots__: tuple
    __rankedController: Any
    __itemsCache: Any
    __lobbyContext: Any
    def __init__(self, contentResID, *args):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, _, __, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, playerPosition, rewardsData, *args, **kwargs):
        ...
    def __getClanAbbrev(self):
        ...
    def __onLeaderboardBtnClick(self):
        ...

class YearLeaderboardAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    __args: Any
    def __init__(self, *args):
        ...
    def isParamsEqual(self, *args):
        ...

def _extractReward(rewardsData):
    ...
