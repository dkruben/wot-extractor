# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_in_progress_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from battle_pass_common import BattlePassConsts as BattlePassConsts, isPostProgressionChapter as isPostProgressionChapter
import constants as constants
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, Array as Array
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_in_progress_tooltip_view_model import BattlePassInProgressTooltipViewModel as BattlePassInProgressTooltipViewModel, ChapterType as ChapterType
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_by_place_model import RewardPointsByPlaceModel as RewardPointsByPlaceModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel as RewardPointsModel
from gui.impl.lobby.battle_pass.battle_pass_wot_plus import getWotPlusPerBattlePoints as getWotPlusPerBattlePoints, getWotPlusBattlePassTier as getWotPlusBattlePassTier, isValidWotPlusTier as isValidWotPlusTier, getMergedWotPlusPointsList as getMergedWotPlusPointsList, extractMinValueFromRange as extractMinValueFromRange
from gui.impl.pub import ViewImpl as ViewImpl
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_helpers import getChapterType as getChapterType, isSeasonEndingSoon as isSeasonEndingSoon, getFormattedTimeLeft as getFormattedTimeLeft, getSupportedCurrentArenaBonusType as getSupportedCurrentArenaBonusType
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.formatters.invites import getPreQueueName as getPreQueueName
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IBattleRoyaleController as IBattleRoyaleController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class BattlePassInProgressTooltipView(ViewImpl):
    __battlePass: Any
    __battleRoyaleController: Any
    __lobbyContext: Any
    __slots__: tuple
    LAYOUT_ID: Any
    __battleType: Any
    def __init__(self, battleType=None, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _customBattleTypeIcon(self):
        ...
    def _hasRewardPoints(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __getAwards(self, chapterID, rewardsList, level, bonusType):
        ...
    def __updateBattleRoyalePoints(self, model, availableBPTier):
        ...
    def __createBattleRoyalePointsBlock(self, pointsByMode):
        ...
    def __getBattleRoyalePoints(self, gameMode, externapPoints):
        ...
