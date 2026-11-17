# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/xml/actions_parsers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import resource_helper as resource_helper
from gui.wgnc import actions as actions
from gui.wgnc.errors import ParseError as ParseError
from gui.wgnc.wgnc_helpers import parseSize as parseSize
from gui.wgnc.xml.shared_parsers import ParsersCollection as ParsersCollection, SectionParser as SectionParser
import ResMgr as ResMgr

class _CallbackActionParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _BrowseActionParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _OpenWindowParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _CustomActionsParser(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...
    def __parse(self, ctx, section):
        ...
    def __getKeyName(self, section):
        ...

class _ReplaceButtonsAction(SectionParser):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class _ActionsParser(ParsersCollection):
    def getTagName(self):
        ...
    def parse(self, section):
        ...

class ActionsParser_v2(_ActionsParser):
    def __init__(self):
        ...
