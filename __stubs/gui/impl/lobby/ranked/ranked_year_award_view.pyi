# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/ranked/ranked_year_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.auxiliary.rewards_helper import getRewardTooltipContent as getRewardTooltipContent, getRewardRendererModelPresenter as getRewardRendererModelPresenter, RANKED_MODEL_PRESENTERS as RANKED_MODEL_PRESENTERS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.ranked.ranked_year_award_model import RankedYearAwardModel as RankedYearAwardModel
from gui.ranked_battles.constants import YEAR_AWARDS_ORDER as YEAR_AWARDS_ORDER, YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX as YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX
from gui.ranked_battles.ranked_formatters import getFormattedBonusesForYearAwardsWindow as getFormattedBonusesForYearAwardsWindow
from gui.shared import event_dispatcher as event_dispatcher
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, TooltipData as TooltipData
from gui.ranked_battles.ranked_helpers.sound_manager import RankedSoundManager as RankedSoundManager
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
_logger: Any

class RankedYearAwardView(ViewImpl):
    __rankedController: Any
    __slots__: tuple
    __items: Any
    __bonuses: Any
    __points: Any
    __vehicleCD: Any
    __showRemainedSelection: Any
    def __init__(self, contentResId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, rawAwards, points, showRemainedSelection):
        ...
    def __onDestroy(self, _=None):
        ...
    def __setViewData(self, points):
        ...
    def __setBonuses(self, bonuses):
        ...
    def __onActionButtonClick(self, _=None):
        ...
    def __getBackportTooltipData(self, event):
        ...
    @staticmethod
    def __removeSelectableYearRewards(rawAwards, count):
        ...

class RankedYearAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    __args: Any
    def __init__(self, rawAwards, points, showRemainedSelection):
        ...
    def isParamsEqual(self, *args):
        ...
