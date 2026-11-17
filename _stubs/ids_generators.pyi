# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/ids_generators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time

class Int32IDGenerator(object):
    next: Any
    currSequenceID: Any
    __nextID: Any
    __currID: Any
    def __init__(self):
        ...
    def __next__(self):
        ...

class SequenceIDGenerator(object):
    next: Any
    currSequenceID: Any
    nextSequenceID: Any
    __lowBound: Any
    __highBound: Any
    __sequenceID: Any
    def __init__(self, lowBound=0, highBound=32767):
        ...
    def __next__(self):
        ...
    def max(self):
        ...
    def clear(self):
        ...
