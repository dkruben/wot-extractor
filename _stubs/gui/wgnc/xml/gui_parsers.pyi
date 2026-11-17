# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/xml/gui_parsers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.wgnc.settings import WGNC_POP_UP_PRIORITIES as WGNC_POP_UP_PRIORITIES
from gui.wgnc.xml.format_by_tags import formatText as formatText
from gui.wgnc.xml.shared_parsers import ParsersCollection as ParsersCollection, SectionParser as SectionParser
from gui.wgnc import gui_items as gui_items

class _ButtonsParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _GUIActionsParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _PopUpParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _WindowParser(SectionParser):
    __slots__: tuple
    _itemClass: Any
    def __init__(self, itemClass=...):
        ...
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _PollParser(_WindowParser):
    def __init__(self, itemClass=...):
        ...
    def getTagName(self):
        ...

class _BrowserParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _GUIItemsParser(ParsersCollection):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class GUIItemsParser_v2(_GUIItemsParser):
    def __init__(self):
        ...
