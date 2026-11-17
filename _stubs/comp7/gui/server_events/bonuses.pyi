# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/server_events/bonuses.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from comp7_common_const import COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_REGEXP as COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_REGEXP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events.bonuses import TokensBonus as TokensBonus
from gui.shared.utils.functions import makeTooltip as makeTooltip
COMP7_TOKEN_WEEKLY_REWARD_NAME = 'comp7TokenWeeklyReward'
_logger: Any

class Comp7TokenWeeklyRewardBonus(TokensBonus):
    _name: Any
    def __init__(self, name, value, isCompensation=False, ctx=None):
        ...
    def isShowInGUI(self):
        ...
    def getTooltip(self):
        ...

def isComp7WeeklyQuestToken(tID):
    ...
