# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/html/templates.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from collections import defaultdict as defaultdict
from past.builtins import unicode as unicode
import ResMgr as ResMgr
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from helpers import html as html
from typing import Optional as Optional, Dict as Dict

class Template(object):
    source: Any
    ctx: Any
    def __init__(self, source, ctx=None):
        ...
    def __repr__(self):
        ...
    def format(self, ctx=None, **kwargs):
        ...

class DummyTemplate(Template):
    source: Any
    def __init__(self, source, ctx=None):
        ...
    def __repr__(self):
        ...
    def format(self, ctx=None, **kwargs):
        ...

class Collection(defaultdict):
    _domain: Any
    _ns: Any
    def __init__(self, domain, ns):
        ...
    def __repr__(self):
        ...
    def __missing__(self, key):
        ...
    def load(self, *args):
        ...
    def unload(self):
        ...
    def _make(self, source):
        ...
    def format(self, key, ctx=None, **kwargs):
        ...

class XMLCollection(Collection):
    def load(self, section=None, clear=False):
        ...
    def _make(self, source):
        ...
