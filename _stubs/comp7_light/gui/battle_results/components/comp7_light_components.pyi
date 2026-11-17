# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/battle_results/components/comp7_light_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7_core.gui.battle_results.components.comp7_core_components import checkIfDeserter as checkIfDeserter
from account_helpers.AccountSettings import STATS_COMP7_LIGHT_SORTING as STATS_COMP7_LIGHT_SORTING
from fairplay_violation_types import FairplayViolations as FairplayViolations
from gui.battle_results.components import base as base
from gui.battle_results.components.shared import SortingBlock as SortingBlock
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo

class IsDeserterFlag(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class Comp7LightSortingBlock(SortingBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...
