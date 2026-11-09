# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/epic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frontline.gui.frontline_helpers import FLBattleTypeDescription as FLBattleTypeDescription
from gui.battle_results.components import base as base
from gui.impl import backport as backport
from gui.impl.gen import R as R

class BattleModificationItem(base.StatsItem):
    __slots__: tuple
    arenaBonusTypes: list
    def _convert(self, record, reusable):
        ...

class StrBattleModificationItem(BattleModificationItem):
    def _convert(self, record, reusable):
        ...
