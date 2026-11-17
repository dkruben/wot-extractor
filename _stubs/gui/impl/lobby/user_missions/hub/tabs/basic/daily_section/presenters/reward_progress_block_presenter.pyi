# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/reward_progress_block_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import OFFERS_ENABLED_KEY as OFFERS_ENABLED_KEY, DAILY_QUESTS_CONFIG as DAILY_QUESTS_CONFIG
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.reward_progress_block_model import RewardProgressTypes as RewardProgressTypes, RewardProgressBlockModel as RewardProgressBlockModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_progress import WinBackProgress as WinBackProgress, OffersState as OffersState
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_quest_model import WinBackQuestModel as WinBackQuestModel
from gui.impl.lobby.missions.missions_helpers import getDailyEpicQuestToken as getDailyEpicQuestToken, getRewardProgressType as getRewardProgressType
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.base_block_presenter import BaseBlockPresenter as BaseBlockPresenter
from gui.impl.lobby.winback.tooltips.main_reward_tooltip import MainRewardTooltip as MainRewardTooltip
from gui.impl.lobby.winback.tooltips.selectable_reward_tooltip import SelectableRewardTooltip as SelectableRewardTooltip
from gui.impl.lobby.winback.winback_bonus_packer import getWinbackBonusPacker as getWinbackBonusPacker, packWinbackBonusModelAndTooltipData as packWinbackBonusModelAndTooltipData
from gui.impl.lobby.winback.winback_bonuses import getWinbackRewardsTimeLeft as getWinbackRewardsTimeLeft
from gui.impl.lobby.winback.winback_helpers import getWinbackCompletedQuestsCount as getWinbackCompletedQuestsCount, getSortedWinbackQuests as getSortedWinbackQuests, getWinbackQuestsData as getWinbackQuestsData, getLastWinbackQuestData as getLastWinbackQuestData
from gui.server_events.settings import visitEventsGUI as visitEventsGUI
from gui.shared.event_dispatcher import showWinbackSelectRewardView as showWinbackSelectRewardView
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker as getDailyMissionsBonusPacker
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController, IWinbackController as IWinbackController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
from typing import Dict as Dict
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.epic_quest_progress import EpicQuestProgress as EpicQuestProgress

# base nao representavel no stub: BaseBlockPresenter[...]
class RewardProgressBlockPresenter:
    eventsCache: Any
    itemsCache: Any
    lobbyContext: Any
    battlePassController: Any
    winbackController: Any
    _winbackData: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def progressType(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _markQuestsAsVisited(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _updateModel(self, model):
        ...
    def _updateCommonData(self, vm):
        ...
    def _updateWinbackData(self):
        ...
    def _updateWinbackQuestProgress(self, vm):
        ...
    def _createWinbackQuestModel(self, questNumber, questData, packer):
        ...
    def _updateEpicQuestProgress(self, model, fullUpdate=False):
        ...
    def _updateBattlePassData(self, vm):
        ...
    def _updateOffersData(self, vm):
        ...
    def _getWinbackOffersState(self):
        ...
    def _onServerSettingsChanged(self, diff=None):
        ...
    def _onWinbackConfigUpdated(self, *_):
        ...
    def _onUpdateBattlePassData(self, *args, **kwargs):
        ...
    def _onTakeAllReward(self):
        ...
    def _onTakeReward(self, args):
        ...
