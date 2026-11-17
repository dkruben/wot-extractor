# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/battle_pass_award.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import BATTLE_PASS_SELECT_BONUS_NAME as BATTLE_PASS_SELECT_BONUS_NAME
from gui.battle_pass.battle_pass_helpers import extractCompensationMoney as extractCompensationMoney
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from gui.battle_pass.bonuses_layout_controller import BonusesLayoutController as BonusesLayoutController
from shared_utils import findFirst as findFirst
from gui.server_events.bonuses import BattlePassSelectTokensBonus as BattlePassSelectTokensBonus

class BattlePassAwardsManager(object):
    __bonusesLayoutController: Any
    @classmethod
    def init(cls):
        ...
    @classmethod
    def composeBonuses(cls, rewards, ctx=None):
        ...
    @classmethod
    def sortBonuses(cls, bonuses):
        ...
    @classmethod
    def hideInvisible(cls, bonuses, needSplit=False):
        ...
    @classmethod
    def getBigIcon(cls, bonus):
        ...
    @classmethod
    def uniteTokenBonuses(cls, bonuses):
        ...

def awardsFactory(items, ctx=None):
    ...
