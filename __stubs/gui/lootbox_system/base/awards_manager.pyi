# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/awards_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.lootbox_system.base.bonuses_layout import BonusesLayout as BonusesLayout
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from typing import Any as Any, Dict as Dict, List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus

class AwardsManager(object):
    __bonusesLayout: _Any
    @classmethod
    def init(cls):
        ...
    @classmethod
    def finalize(cls):
        ...
    @classmethod
    def bonusesLayoutUpdate(cls):
        ...
    @classmethod
    def composeBonuses(cls, eventName, rewards, ctx=None):
        ...
    @classmethod
    def sortMergeBonuses(cls, eventName, bonuses, reverse=False):
        ...
    @classmethod
    def sortBonuses(cls, eventName, bonuses, reverse=False):
        ...
    @classmethod
    def getRarity(cls, eventName, bonus):
        ...
    @classmethod
    def getIsVisible(cls, eventName, bonus):
        ...

def awardsFactory(items, ctx=None):
    ...
