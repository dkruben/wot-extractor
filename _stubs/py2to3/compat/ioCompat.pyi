# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/py2to3/compat/ioCompat.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from past.builtins import unicode as unicode

class UnicodeFileAdapter(object):
    target: Any
    def __init__(self, target):
        ...
    def write(self, data):
        ...
    def writelines(self, lines):
        ...
    def __getattr__(self, name):
        ...

def _toUnicode(value, errors='replace'):
    ...
