# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_const.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class FrontlineState(Enum):
    ANNOUNCE = 'announce'
    ACTIVE = 'active'
    FINISHED = 'finished'
    FROZEN = 'frozen'
    INTRO = 'intro'

class FrontlineConst(ViewModel):
    __slots__: tuple
    BATTLE_ABILITIES = 'battleAbilities'
    def __init__(self, properties=0, commands=0):
        ...
    def _initialize(self):
        ...
