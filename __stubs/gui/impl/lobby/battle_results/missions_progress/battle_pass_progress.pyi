# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/battle_pass_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from battle_pass_common import BattlePassConsts as BattlePassConsts, NON_CHAPTER_ID as NON_CHAPTER_ID, isPostProgressionChapter as isPostProgressionChapter
from gui.battle_pass.battle_pass_bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.progression.battle_pass_progress_model import BattlePassProgressModel as BattlePassProgressModel
from gui.impl.gen.view_models.views.lobby.tooltips.additional_rewards_tooltip_model import AdditionalRewardsTooltipModel as AdditionalRewardsTooltipModel
from gui.impl.lobby.battle_pass.battle_pass_wot_plus import isWotPlusBattlePassAvailableForAnyTier as isWotPlusBattlePassAvailableForAnyTier
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalBattlePassRewardsTooltip as AdditionalBattlePassRewardsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
from gui.shared.event_dispatcher import showBattlePass as showBattlePass
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import WOTP_REQUESTER_NAME as WOTP_REQUESTER_NAME
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IWotPlusController as IWotPlusController
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import BattlePassProgress as BattlePassProgress
from gui.impl.gen.view_models.views.lobby.battle_results.progression.external_points_model import ExternalPointsModel as ExternalPointsModel
EXTERNAL_POINTS_LABELS_MAP: dict

# base nao representavel no stub: ViewComponent[...]
class BattlePassProgressPresenter(IProgressionCategoryPresenter):
    __battlePassController: Any
    __wotPlusController: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __progress: Any
    __tooltipItems: Any
    __chapter: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
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
    def _updateProgress(self):
        ...
    def __packBattlePassProgress(self):
        ...
    def __packExternalPoints(self, model):
        ...
    def __packAwards(self, progress, currentChapter, level, model):
        ...
    def __onNavigate(self):
        ...
    def __onSettingsChange(self, *_):
        ...
    def __onSeasonStateChanged(self):
        ...
