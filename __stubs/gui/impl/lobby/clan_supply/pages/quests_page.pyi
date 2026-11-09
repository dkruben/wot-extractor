# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/pages/quests_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
import SoundGroups as SoundGroups
from adisp import adisp_process as adisp_process
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui import SystemMessages as SystemMessages
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.clans.data_wrapper.clan_supply import QuestStatus as DataQuestStatus, ConditionRuleType as ConditionRuleType, ConditionSquadState as ConditionSquadState, DataNames as DataNames
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quest_model import QuestModel as QuestModel, QuestStatus as QuestStatus, QuestCondition as QuestCondition, QuestSquadState as QuestSquadState
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quests_model import ScreenStatus as ScreenStatus
from gui.impl.lobby.clan_supply.bonus_packers import composeBonuses as composeBonuses, getCurrencyReward as getCurrencyReward
from gui.impl.lobby.clan_supply.sound_helper import SOUNDS as SOUNDS
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.shared.event_dispatcher import showStrongholds as showStrongholds
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from gui.wgcg.clan_supply.contexts import ClaimRewardsCtx as ClaimRewardsCtx
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import first as first, nextTick as nextTick
from skeletons.gui.game_control import IClanNotificationController as IClanNotificationController
from skeletons.gui.web import IWebController as IWebController
from typing import Optional as Optional, Dict as Dict, List as List, Tuple as Tuple
from gui.clans.data_wrapper import clan_supply as clan_supply
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quests_model import QuestsModel as QuestsModel
_logger: Any
BUBBLES_ALIAS = 'clansupply_hangar_bubble'
_QuestDataStatusToModelStatus: dict
_QuestDataConditionToModelCondition: dict
_QuestDataSquadStateToModelSquadState: dict
_ExistMainSquadStateLocalizationKeys: tuple
_ExistMainConditionLocalizationKeys: tuple
_ExistAlternativeSquadStateLocalizationKeys: tuple
_ExistAlternativeConditionLocalizationKeys: tuple

class QuestsPage(SubModelPresenter):
    __slots__: tuple
    __webController: Any
    __notificationCtrl: Any
    __tooltips: Any
    __cachedQuestData: Any
    __notifier: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __updateState(self):
        ...
    def __updateQuests(self, questsInfo):
        ...
    def __fillQuestModel(self, questData, prevQuestData, screenStatus):
        ...
    def __onDataReceived(self, dataName, data):
        ...
    def __onDataFailed(self, dataName):
        ...
    def __onRefresh(self):
        ...
    def __updateClanInfo(self, *_):
        ...
    # decorador original: @adisp_process
    def __onClaimReward(self):
        ...
    def __onGoToClans(self):
        ...
    def __restartNotifier(self, timeUntilUpdateState):
        ...
    @staticmethod
    def __getQuestSquadState(conditionData):
        ...
    @staticmethod
    def __getConditionParams(rules):
        ...
    @staticmethod
    def __isPreviousRewardsEmpty(rewards):
        ...
