# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/challenges/challenges_award_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.lobby.common.bonuses_layout_config_reader import BonusesLayout as BonusesLayout
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from typing import Any as Any, Dict as Dict, List as List
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_CONFIG_FILENAME = 'gui/challenges_bonuses_layout.xml'

class AwardsManager(object):
    __bonusesLayout: _Any
    @classmethod
    def init(cls):
        ...
    @classmethod
    def finalize(cls):
        ...
    @classmethod
    def composeVisibleBonuses(cls, rewards, ctx=None, reverse=False):
        ...
    @classmethod
    def composeBonuses(cls, rewards, ctx=None, reverse=False):
        ...
    @classmethod
    def sortMergeBonuses(cls, bonuses, reverse=False):
        ...
    @classmethod
    def sortBonuses(cls, bonuses, reverse=False):
        ...
    @classmethod
    def sortVisibleBonuses(cls, bonuses, reverse=False):
        ...
    @classmethod
    def hideInvisible(cls, bonuses):
        ...

def awardsFactory(rewards, ctx=None):
    ...
