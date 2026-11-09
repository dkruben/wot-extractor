# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SafeUnpickler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import sys as sys
import copy as copy
from io import BytesIO as BytesIO
from future.moves import pickle as pickle

class SafeUnpickler(object):
    PICKLE_SAFE: dict
    def __init__(self):
        ...
    @classmethod
    def find_class(cls, module, name):
        ...
    @classmethod
    def loads(cls, pickle_string):
        ...
