# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/helpers/tips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from cgf_components.marker_component import IBattleSessionProvider as IBattleSessionProvider
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode as hasBattleSubMode
from gui.impl.gen import R as R
from helpers import dependency as dependency
from helpers.tips import TipsCriteria as TipsCriteria, TipData as TipData

class FunRandomTipsCriteria(TipsCriteria, FunSubModesWatcher):
    __sessionProvider: Any
    # decorador original: @hasBattleSubMode(...)
    def find(self):
        ...
    def _getTipsValidator(self):
        ...
