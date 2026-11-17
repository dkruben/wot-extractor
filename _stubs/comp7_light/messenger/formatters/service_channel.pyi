# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.notification.decorators import Comp7LightProgressionLockButtonDecorator as Comp7LightProgressionLockButtonDecorator
from constants import SCENARIO_RESULT as SCENARIO_RESULT
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import BattleResultsFormatter as BattleResultsFormatter, QuestAchievesFormatter as QuestAchievesFormatter, ServiceChannelFormatter as ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData, parseTokenBonusCount as parseTokenBonusCount
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from skeletons.gui.server_events import IEventsCache as IEventsCache

class Comp7LightBattleResultsFormatter(BattleResultsFormatter):
    __comp7LightController: Any
    __eventsCache: Any
    _battleResultKeys: dict
    def _prepareFormatData(self, message):
        ...
    def __makeProgressionPointsString(self, message):
        ...
    def __getProgressionTokenBonus(self, battleResults):
        ...

class Comp7LightProgressionAchievesFormatter(QuestAchievesFormatter):
    _BULLET = '\u2022 '
    _SEPARATOR: Any
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...

class Comp7LightProgressionSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = 'comp7LightProgressionSystemMessage'
    _achievesFormatter: Any
    def __init__(self):
        ...
    def format(self, message, *args):
        ...
    def _format(self, message, *_):
        ...
    def _formatSingleStageCompletion(self, message, stageInfo):
        ...
