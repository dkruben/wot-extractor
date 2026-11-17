# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/xml/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from gui.wgnc.errors import ParseError as ParseError
from gui.wgnc.xml import actions_parsers as actions_parsers, gui_parsers as gui_parsers, shared_parsers as shared_parsers, proxy_data_parsers as proxy_data_parsers
_PARSER_BY_VER: dict

class _NotificationParser(shared_parsers.SectionParser):
    __slots__: tuple
    _actionsParser: Any
    _guiParser: Any
    _proxyDataParser: Any
    def __init__(self, actionsParser, guiParser, proxyDataParser):
        ...
    def getTagName(self):
        ...
    def parse(self, section):
        ...

def _parse(section):
    ...
def fromString(xml):
    ...
def fromSection(section):
    ...
