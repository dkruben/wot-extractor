# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/blueprints/FragmentLayouts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from bitstring import BitArray as BitArray
from bit_coder import BitCoder as BitCoder
from past.builtins import xrange as xrange, long as long

class Layout(object):
    __slots__: tuple
    LAYOUTS: Any
    filledCount: Any
    emptyCount: Any
    columns: Any
    rows: Any
    stamps: Any
    layoutData: Any
    @classmethod
    def fromInt(cls, packedLayout=None, length=None):
        ...
    @classmethod
    def calcFilledfromInt(cls, packedLayout, length):
        ...
    @classmethod
    def calcEmptyfromInt(cls, packedLayout, length):
        ...
    def asInt(self):
        ...
    def __init__(self, intLayout, length):
        ...
    def __iadd__(self, other):
        ...
    def __isub__(self, other):
        ...
    def __len__(self):
        ...
    def __setitem__(self, key, value):
        ...
    def __getitem__(self, item):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def __checkParams(packedLayout, length):
        ...
    @staticmethod
    def __numberOfSetBits(i):
        ...
