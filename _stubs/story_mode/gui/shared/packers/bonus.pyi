# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/shared/packers/bonus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.server_events.awards_formatters import getDefaultFormattersMap as getDefaultFormattersMap, ItemsBonusFormatter as ItemsBonusFormatter
from gui.shared.missions.packers.bonus import ItemBonusUIPacker as ItemBonusUIPacker, BonusUIPacker as BonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from typing import Dict as Dict

class SMItemBonusUIPacker(ItemBonusUIPacker):
    @staticmethod
    def _itemsSortFunction(item):
        ...

class SMItemsBonusFormatter(ItemsBonusFormatter):
    def _getItems(self, bonus):
        ...

def getSMFormattersMap():
    ...
def getSMBonusPackersMap():
    ...
def getSMBonusPacker():
    ...
