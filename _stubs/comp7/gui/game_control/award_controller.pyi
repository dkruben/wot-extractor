# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/game_control/award_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import ArenaType as ArenaType
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isComp7VisibleQuest as isComp7VisibleQuest, getComp7QuestType as getComp7QuestType, parseComp7RanksQuestID as parseComp7RanksQuestID, getRequiredTokensCountToComplete as getRequiredTokensCountToComplete
from comp7.gui.shared import event_dispatcher as comp7_events
from comp7.gui.shared.event_dispatcher import showComp7BanWindow as showComp7BanWindow
from comp7.skeletons.gui.game_control import IComp7ShopController as IComp7ShopController
from comp7_common_const import Comp7QuestType as Comp7QuestType, qualificationQuestIDBySeasonNumber as qualificationQuestIDBySeasonNumber, COMP7_YEARLY_REWARD_TOKEN as COMP7_YEARLY_REWARD_TOKEN
from constants import INVOICE_ASSET as INVOICE_ASSET, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, PENALTY_TYPES as PENALTY_TYPES
from fairplay_violation_types import getFairplayViolationLocale as getFairplayViolationLocale, getPenaltyTypeAndViolationName as getPenaltyTypeAndViolationName, FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES as FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES
from gui.game_control.AwardController import MultiTypeServiceChannelHandler as MultiTypeServiceChannelHandler, ServiceChannelHandler as ServiceChannelHandler, PunishWindowHandler as PunishWindowHandler
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters.time_formatters import getTillTimeByResource as getTillTimeByResource
from helpers import dependency as dependency
from messenger.formatters import TimeFormatter as TimeFormatter
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7_ranks_common import Comp7Division as Comp7Division
from gui.server_events.event_items import TokenQuest as TokenQuest
_logger: Any

class Comp7QuestRewardHandler(MultiTypeServiceChannelHandler):
    __comp7Ctrl: Any
    __comp7ShopCtrl: Any
    __completedQuestIDs: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _showAward(self, ctx):
        ...
    def __showAward(self):
        ...
    def __getComp7CompletedQuests(self):
        ...
    def __onEventCacheSyncCompleted(self, *_):
        ...
    @staticmethod
    def __getRanksQuestSortKey(quest):
        ...
    @staticmethod
    def __getTokensQuestSortKey(quest):
        ...

class Comp7InvoiceRewardHandler(ServiceChannelHandler):
    __comp7Ctrl: Any
    __RETRY_TIMES: list
    __bonuses: Any
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def __onEntitlementsUpdated(self):
        ...
    def __onEntitlementsUpdateFailed(self):
        ...

class Comp7PunishWindowHandler(PunishWindowHandler):
    def _showAward(self, ctx):
        ...
    @property
    def channelType(self):
        ...
