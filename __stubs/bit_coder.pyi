# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/bit_coder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any

class BitCoder:
    __dimension: Any
    __fieldDescriptor: Any
    __fieldDescriptorLen: Any
    def __init__(self, *args):
        ...
    @staticmethod
    def mask(bits):
        ...
    def extract(self, bitField):
        ...
    def emplace(self, *fields):
        ...
    def checkFit(self, fieldIndex, value):
        ...
