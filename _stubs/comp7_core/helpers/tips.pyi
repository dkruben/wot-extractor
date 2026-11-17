# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/helpers/tips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from helpers.tips import TipsCriteria as TipsCriteria, readTips as readTips
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from comp7_core_constants import SubMode as SubMode
_COMP7_NIGHT_MAPS_TIPS_PATTERN = '^(comp7NightMaps\\d+$)'
_comp7NightMapsTips: Any

class Comp7BaseTipsCriteria(TipsCriteria):
    _sessionProvider: Any
    def _getTargetList(self):
        ...
    def _getSubModeTips(self):
        ...
    @staticmethod
    def _getRegularTips():
        ...
