# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from messenger import g_settings as g_settings
from messenger.formatters.service_channel import QuestAchievesFormatter as QuestAchievesFormatter

class OpenBundleAchievesFormatter(QuestAchievesFormatter):
    _BULLET = '\u2022'
    @classmethod
    def formatData(cls, data):
        ...
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter=False, processCustomizations=True, processTokens=True):
        ...
    @classmethod
    def _processTokens(cls, data):
        ...
    @classmethod
    def _processTankmanToken(cls, tokenName, tokenData):
        ...
