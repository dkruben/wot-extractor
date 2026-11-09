# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/xml/shared_parsers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.wgnc.errors import ParseError as ParseError

class SectionParser(object):
    __slots__: tuple
    def getTagName(self):
        ...
    def parse(self, section):
        ...
    def _readString(self, name, section):
        ...

class ParsersCollection(SectionParser):
    __slots__: tuple
    _parsers: Any
    def __init__(self, seq):
        ...
    def clear(self):
        ...
    def parse(self, section):
        ...
