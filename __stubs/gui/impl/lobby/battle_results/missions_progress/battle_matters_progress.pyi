# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/battle_matters_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.progression.battle_matters_progress_model import BattleMattersProgressModel as BattleMattersProgressModel
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import getBattleMattersBonusPacker as getBattleMattersBonusPacker, bonusesSortKey as bonusesSortKey, battleMattersSortKey as battleMattersSortKey
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel as QuestViewModel, State as State
from gui.server_events.events_dispatcher import showBattleMatters as showBattleMatters
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Union as Union
from gui.server_events.event_items import BattleMattersQuest as BattleMattersQuest, BattleMattersTokenQuest as BattleMattersTokenQuest

# base nao representavel no stub: ViewComponent[...]
class BattleMattersProgressPresenter(IProgressionCategoryPresenter):
    __battleMattersController: Any
    __eventsCache: Any
    __settingsCore: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __allCommonQuests: Any
    __progress: Any
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
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateProgress(self):
        ...
    def _updateModel(self):
        ...
    def _finalize(self):
        ...
    def __createQuestModel(self, quest, pCur, pPrev, isCompleted):
        ...
    def __onNavigate(self):
        ...
