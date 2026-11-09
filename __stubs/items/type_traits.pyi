# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/type_traits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from past.builtins import unicode as unicode
from typing import Any as Any, Callable as Callable, Sequence as Sequence
import Math as Math
EQUAL_COMPARATORS: dict
DEFAULT_GETTERS: dict

def allowEqualNone(eq):
    ...
def equal(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalFloat(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalString(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalVector2(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalVector3(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalVector4(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalMatrix(lhs, rhs):
    ...
# decorador original: @allowEqualNone
def equalSeq(lhs, rhs, eq=...):
    ...
def equalComparator(tp):
    ...
def defaultGetter(tp):
    ...
def default(tp):
    ...
