# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import resource_helper as resource_helper
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from frameworks.wulf.gui_constants import WindowStatus as WindowStatus
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BattleMattersViewMeta import BattleMattersViewMeta as BattleMattersViewMeta
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_main_view_model import BattleMattersMainViewModel as BattleMattersMainViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.intermediate_quest_model import IntermediateQuestModel as IntermediateQuestModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel as QuestViewModel, State as State
from gui.impl.lobby.battle_matters.battle_matters_bonus_packer import getBattleMattersBonusPacker as getBattleMattersBonusPacker, bonusesSortKey as bonusesSortKey, battleMattersSortKey as battleMattersSortKey
from gui.impl.lobby.battle_matters.battle_matters_constants import QuestCardSections as QuestCardSections, CARDS_CONFIG_XML_PATH as CARDS_CONFIG_XML_PATH
from gui.impl.lobby.battle_matters.battle_matters_main_reward_view import BattleMattersMainRewardView as BattleMattersMainRewardView
from gui.impl.lobby.battle_matters.battle_matters_vehicle_selection_view import BattleMattersVehicleSelectionView as BattleMattersVehicleSelectionView
from gui.impl.lobby.battle_matters.battle_matters_paused_view import BattleMattersPausedView as BattleMattersPausedView
from gui.impl.lobby.battle_matters.tooltips.battle_matters_token_tooltip_view import BattleMattersTokenTooltipView as BattleMattersTokenTooltipView
from gui.impl.lobby.battle_matters.battle_matters_rewards_view import BattleMattersRewardsViewWindow as BattleMattersRewardsViewWindow
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.events_dispatcher import showBattleMattersMainReward as showBattleMattersMainReward
from gui.shared.event_dispatcher import showDelayedReward as showDelayedReward, showHangar as showHangar
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.shared.missions.packers.bonus import packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from shared_utils import nextTick as nextTick
from gui.clans.clan_cache import g_clanCache as g_clanCache
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.game_control import IManualController as IManualController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.Scaleform.locale.MENU import MENU as MENU
from typing import List as List, Union as Union
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_progress_model import QuestProgressModel as QuestProgressModel
from gui.server_events.event_items import BattleMattersQuest as BattleMattersQuest, BattleMattersTokenQuest as BattleMattersTokenQuest
_logger: Any

class BattleMattersMissionComponent(InjectComponentAdaptor, BattleMattersViewMeta):
    __slots__: tuple
    __battleMattersController: Any
    __settingsCore: Any
    # decorador original: @nextTick
    def updateState(self, openMainRewardView=False, openVehicleSelection=False, openMainView=False, **_):
        ...
    def markVisited(self):
        ...
    def _addInjectContentListeners(self):
        ...
    def _removeInjectContentListeners(self):
        ...
    def _makeInjectView(self, componentClass):
        ...
    def _onPopulate(self):
        ...
    def _destroy(self):
        ...
    def _onViewReady(self, *args):
        ...
    def _getComponentClass(self, openMainRewardView=False, openVehicleSelection=False, openMainView=False):
        ...
    def __onStateChanged(self):
        ...
    def __checkHint(self):
        ...

class BattleMattersMainView(ViewImpl):
    __slots__: tuple
    __appLoader: Any
    __battleMattersController: Any
    __eventsCache: Any
    __manualController: Any
    __lobbyContext: Any
    __settingsCore: Any
    __tooltips: Any
    __questCardsDescriptions: Any
    __currentQuestIdx: Any
    __compensationQuestsStatus: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    @classmethod
    def __getMissionPage(cls):
        ...
    def __getCurrentQuestIdx(self):
        ...
    @staticmethod
    def __onSelectDelayedReward():
        ...
    @staticmethod
    def __onShowMainReward():
        ...
    def __onWindowStatusChanged(self, uniqueID, newStatus):
        ...
    def __readXML(self):
        ...
    def __onAnimForQuest(self, args):
        ...
    def __getBattleMattersData(self):
        ...
    def __update(self):
        ...
    def __updateCompensationQuestStatus(self):
        ...
    def __updateQuestProgress(self, questProgressModel, regularQuests):
        ...
    def __createQuestProgressModel(self, quest):
        ...
    def __updateQuests(self, model, quests):
        ...
    def __updateLastSeenProgressForQuest(self, questsModel, lastSeenQuestInProgressIdx):
        ...
    def __saveLastSeenProgress(self, currentQuest):
        ...
    def __createQuestModel(self, quest, currentQuest, lastSeenQuestInProgressIdx):
        ...
    def __isRegularQuestCompleted(self, quest):
        ...
    def __onShowManual(self):
        ...
    def __onShowManualForQuest(self, args):
        ...
    def __onSyncCompleted(self):
        ...
