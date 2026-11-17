# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import deepcopy as deepcopy
from future.utils import viewvalues as viewvalues
from battle_royale.notification.decorators import BRProgressionLockButtonDecorator as BRProgressionLockButtonDecorator
from constants import LOOTBOX_TOKEN_PREFIX as LOOTBOX_TOKEN_PREFIX
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter as ServiceChannelFormatter, QuestAchievesFormatter as QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BRProgressionAchievesFormatter(QuestAchievesFormatter):
    _BULLET = '\u2022 '
    _SEPARATOR: Any
    __LOOTBOX_TEMPLATE = 'SHPLootBoxReceived'
    __STPCOIN_TEMPLATE = 'StPCoinReceived'
    __BATTLE_PASS_TEMPLATE = 'battlePassBR'
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def getFormattedAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...

class BRProgressionSystemMessageFormatter(ServiceChannelFormatter):
    __BATTLE_ROYALE_TEMPLATE = 'battleRoyaleProgressionSystemMessage'
    __ST_PATRICK_TEMPLATE = 'stPatrickProgressionSystemMessage'
    __battleRoyaleController: Any
    _achievesFormatter: Any
    def __init__(self):
        ...
    def format(self, message, *args):
        ...
    def _format(self, message, *_):
        ...
    def _formatSingleStageCompletion(self, message, stageInfo):
        ...
