# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/game_control/AwardController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from dossiers2.ui.achievements import BADGES_BLOCK as BADGES_BLOCK
from fort_rush.gui.shared.event_dispatcher import showAwardWindow as showAwardWindow
from fort_rush.helpers.utils import isFREventProgressionQuest as isFREventProgressionQuest
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from gui import SystemMessages as SystemMessages
from gui.game_control import AwardController as AwardController
from gui.game_control.AwardController import MultiTypeServiceChannelHandler as MultiTypeServiceChannelHandler
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.dossier.factories import getAchievementFactory as getAchievementFactory
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from messenger.formatters.service_channel import QuestAchievesFormatter as QuestAchievesFormatter, _processTankmanToken as _processTankmanToken
from optional_bonuses import BONUS_MERGERS as BONUS_MERGERS
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any

class _FortRushQuestAchievesFormatter(QuestAchievesFormatter):
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _extractAchievements(cls, data):
        ...

class FortRushPunishWindowHandler(AwardController.PunishWindowHandler):
    @property
    def channelType(self):
        ...

class FortRushAwardsController(MultiTypeServiceChannelHandler):
    __ctrl: Any
    __systemMessages: Any
    __STR_RES = R.strings.fort_rush.notifications.progression
    __completedQuestIds: Any
    def __init__(self, awardCtrl):
        ...
    def _needToShowAward(self, ctx):
        ...
    def _showAward(self, ctx):
        ...
    def __updateReward(self, rewardData, bonuses):
        ...
    @staticmethod
    def __getRewardDataKey(bonus):
        ...
    def __showStageCompletedMessage(self, stageIdx, rewards):
        ...
    def __getRewards(self, rewardData, rewards):
        ...
    def __getStageIdx(self, questID):
        ...
