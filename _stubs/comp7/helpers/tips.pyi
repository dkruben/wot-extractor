# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/helpers/tips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7_common.comp7_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from helpers.tips import readTips as readTips
from comp7_core.helpers.tips import Comp7BaseTipsCriteria as Comp7BaseTipsCriteria
_COMP7_TIPS_PATTERN = '^(comp7(Core|Ranked)\\d+$)'
_comp7Tips: Any

class Comp7TipsCriteria(Comp7BaseTipsCriteria):
    def _getArenaGuiType(self):
        ...
    @staticmethod
    def _getRegularTips():
        ...
