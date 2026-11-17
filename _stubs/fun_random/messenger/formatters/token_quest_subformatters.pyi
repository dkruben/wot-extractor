# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewkeys as viewkeys, viewvalues as viewvalues
from typing import Dict as Dict, List as List
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from constants import LOOTBOX_TOKEN_PREFIX as LOOTBOX_TOKEN_PREFIX
from fun_random.gui.feature.fun_constants import FEP_MODE_ITEMS_QUEST_ID as FEP_MODE_ITEMS_QUEST_ID, FEP_PROGRESSION_EXECUTOR_QUEST_ID as FEP_PROGRESSION_EXECUTOR_QUEST_ID
from fun_random.gui.feature.util.fun_helpers import getProgressionInfoByExecutor as getProgressionInfoByExecutor
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.lobby.common.lootboxes import FEP_CATEGORY as FEP_CATEGORY, FunRandomLootBoxTypes as FunRandomLootBoxTypes
from fun_random.notification.decorators import FunRandomProgressionStageMessageDecorator as FunRandomProgressionStageMessageDecorator
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers.time_utils import ONE_DAY as ONE_DAY
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter, QuestAchievesFormatter as QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData, getRewardsForQuests as getRewardsForQuests
from messenger.formatters.token_quest_subformatters import TokenQuestsSubFormatter as TokenQuestsSubFormatter, AsyncTokenQuestsSubFormatter as AsyncTokenQuestsSubFormatter, SyncTokenQuestsSubFormatter as SyncTokenQuestsSubFormatter

class FunProgressionRewardsBaseFormatter(ServiceChannelFormatter, TokenQuestsSubFormatter, FunAssetPacksMixin, FunProgressionWatcher):
    __INFO_TEMPLATE = 'InformationHeaderSysMessage'
    __PROGRESSION_STAGE_TEMPLATE = 'FunRandomProgressionStage'
    __RES_SHORTCUT = R.strings.fun_random.notification
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def _getAchievesFormatter(self):
        ...
    def _format(self, message, *_):
        ...
    def _formatProgressionCompletion(self, progression, rewardsFmt):
        ...
    # decorador original: @hasActiveProgression(...)
    def _formatSingleQuestCompletion(self, qInfo, rewards):
        ...

class FunProgressionRewardsAsyncFormatter(AsyncTokenQuestsSubFormatter, FunProgressionRewardsBaseFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def _getAchievesFormatter(self):
        ...

class FunProgressionRewardsSyncFormatter(SyncTokenQuestsSubFormatter, FunProgressionRewardsBaseFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...
    def format(self, message, *args):
        ...
    def _getAchievesFormatter(self):
        ...

class FunRandomLootBoxFormatter(QuestAchievesFormatter, FunAssetPacksMixin):
    @classmethod
    def getFormattedAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _sortTokenFunc(cls, tokenId):
        ...

class FunModeItemsQuestAsyncFormatter(AsyncTokenQuestsSubFormatter, FunAssetPacksMixin):
    __INFO_TEMPLATE = 'InformationHeaderSysMessage'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def _format(self, message, *_):
        ...
    def _formatModeItemsSingleQuest(self, rewards):
        ...
