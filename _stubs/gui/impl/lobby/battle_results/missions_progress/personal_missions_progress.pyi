# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/personal_missions_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.battle_results.progress.progress_helpers import isPMOperationAndMissionEnabled as isPMOperationAndMissionEnabled
from gui.impl.gen.view_models.views.lobby.battle_results.progression.personal_missions_progress_model import PersonalMissionsProgressModel as PersonalMissionsProgressModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.gen import R as R
from gui.impl.lobby.personal_missions_30.personal_mission_constants import MISSIONS_ROLES_TO_CATEGORIES as MISSIONS_ROLES_TO_CATEGORIES
from gui.impl.lobby.personal_missions_30.views_helpers import getMissionConfigData as getMissionConfigData
from gui.impl.lobby.personal_missions_30.bonus_packers import getBonusPacker as getBonusPacker, packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.server_events.events_dispatcher import showPersonalMissionsChain as showPersonalMissionsChain
from gui.impl.lobby.personal_missions_30.tooltips.mission_progress_tooltip import MissionProgressTooltip as MissionProgressTooltip
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.gen.view_models.views.lobby.battle_results.progression.personal_missions_progress_model import PM3Status as PM3Status
from gui.impl.lobby.personal_missions_30.tooltips.missions_category_tooltip import MissionsCategoryTooltip as MissionsCategoryTooltip
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory as MissionCategory
from gui.server_events.finders import getBranchByOperationId as getBranchByOperationId
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Dict as Dict
from gui.impl.gen.view_models.views.lobby.personal_missions_30.quest_model import QuestModel as QuestModel

# base nao representavel no stub: ViewComponent[...]
class PersonalMissionsProgressPresenter(IProgressionCategoryPresenter):
    __eventsCache: Any
    __lobbyContext: Any
    __personalMissions: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __progress: Any
    __tooltipData: Any
    __bonusesModel: Any
    __currentOperationOfPbs: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, *args, **kwargs):
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
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    @staticmethod
    def __getCampaignStatus(isQuestFullyCompleted, pmOperations, operationFromPBS):
        ...
    def __getTooltipData(self, event):
        ...
    def __onNavigate(self):
        ...
    def __fillRewards(self, eventId, rewardsModel, bonuses, packer):
        ...
    def __onSwitcherUpdated(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
