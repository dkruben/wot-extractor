# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_how_to_earn_points_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.moves import itertools as itertools
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_how_to_earn_points_view_model import BattlePassHowToEarnPointsViewModel as BattlePassHowToEarnPointsViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_cell_model import GameModeCellModel as GameModeCellModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_model import ArenaBonusType as ArenaBonusType, GameModeModel as GameModeModel, PointsCardType as PointsCardType
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel as GameModeRowsModel
from gui.impl.lobby.user_missions.hub.hub_view import DailyTabs as DailyTabs
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.shared.event_dispatcher import showHangar as showHangar, showWotPlusInfoPage as showWotPlusInfoPage
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.battle_pass.battle_pass_wot_plus import getWotPlusPerBattlePoints as getWotPlusPerBattlePoints, getWotPlusBattlePassTier as getWotPlusBattlePassTier, isWotPlusBattlePassAvailableForAnyTier as isWotPlusBattlePassAvailableForAnyTier, getMergedWotPlusPointsList as getMergedWotPlusPointsList, extractMinValueFromRange as extractMinValueFromRange
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource
REVERSE_GAME_MODE_ORDER: tuple
REVERSE_GAME_MODE_ORDER_MAP: dict
_rBattlePass = R.strings.battle_pass
_logger: Any

class BattlePassHowToEarnPointsView(ViewImpl):
    __itemsCache: Any
    __battlePass: Any
    __chapterID: Any
    def __init__(self, chapterID=0):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __getGameMode(self, arenaType):
        ...
    def __createGeneralModel(self):
        ...
    def __createGameModel(self, gameType):
        ...
    def __createBattleRoyalGameModel(self):
        ...
    def __createBattleRoyalConditionsTable(self, gameType, viewModel):
        ...
    def __createBattleRoyaleConditionRow(self, points, previousLevel, wpWinMergedPoints):
        ...
    def __createConditionsTable(self, gameType, viewModel):
        ...
    @staticmethod
    def __createBattleRoyalTableHeader(gameType, viewModel):
        ...
    @staticmethod
    def __createTableHeader(gameType, viewModel):
        ...
    def __createCardsModel(self, gameType, viewModel):
        ...
    @staticmethod
    def __createVehiclesHeader(gameType, viewModel):
        ...
    def __createVehiclesTable(self, gameType, viewModel):
        ...
    def __goToMissions(self):
        ...
    def __goToWotPlusInfoPage(self):
        ...
    def __onBattlePassSettingsChange(self, *_):
        ...

class BattlePassHowToEarnPointsWindow(LobbyWindow):
    def __init__(self, chapterID=0):
        ...
