# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/pickle_intern.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import pickle as pickle
from copy import deepcopy as deepcopy
from io import BytesIO as BytesIO
from past.builtins import intern as intern
from struct_helpers import unpackByte as unpackByte
STR_LEN_FOR_INTERN = 20

class UnpicklerWithIntern(pickle.Unpickler, object):
    dispatch: Any
    def __init__(self, file):
        ...
    def load_short_binstring(self):
        ...
    @classmethod
    def loads(cls, data):
        ...
