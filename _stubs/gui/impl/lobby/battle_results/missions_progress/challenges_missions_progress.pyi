# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/challenges_missions_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from challenges_common import isChallengeFailQuest as isChallengeFailQuest
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.challenges.challenges_award_manager import AwardsManager as AwardsManager
from gui.challenges.challenges_bonuses_packers import getChallengesPostBattleBonusPacker as getChallengesPostBattleBonusPacker
from gui.challenges.challenges_decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.progression.challenges_missions_progress_model import ChallengesMissionsProgressModel as ChallengesMissionsProgressModel
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.challenges.views_helpers import parseChallengeQuestId as parseChallengeQuestId
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.events_dispatcher import showChallenges as showChallenges
from gui.shared.missions.packers.events import ChallengeMissionUIDataPacker as ChallengeMissionUIDataPacker
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: ViewComponent[...]
class ChallengesMissionsProgressPresenter(IProgressionCategoryPresenter):
    __eventsCache: Any
    __challenges: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __allCommonQuests: Any
    __progress: Any
    __questID: Any
    __challengeID: Any
    __tooltipData: Any
    __bonusesModel: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, allCommonQuests):
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
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    def __createModel(self, challengeQuestModel, quest):
        ...
    def __setNavigationStatus(self, model, challenge):
        ...
    def __onNavigate(self):
        ...
