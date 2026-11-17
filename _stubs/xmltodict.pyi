# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/xmltodict.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lzip as lzip
from defusedexpat import pyexpat as expat
from xml.parsers import expat as expat
from xml.sax.saxutils import XMLGenerator as XMLGenerator
from xml.sax.xmlreader import AttributesImpl as AttributesImpl
from cStringIO import StringIO as StringIO
from StringIO import StringIO as StringIO
from io import StringIO as StringIO
import sys as sys
import marshal as marshal
OrderedDict: Any
_basestring: Any
_unicode: Any
__author__ = 'Martin Blech'
__version__ = '0.11.0'
__license__ = 'MIT'
stdin = sys.stdin
stdout = sys.stdout
item_depth_arg: Any
root: Any

class ParsingInterrupted(Exception):
    ...

class _DictSAXHandler(object):
    path: Any
    stack: Any
    data: Any
    item: Any
    item_depth: Any
    xml_attribs: Any
    item_callback: Any
    attr_prefix: Any
    cdata_key: Any
    force_cdata: Any
    cdata_separator: Any
    postprocessor: Any
    dict_constructor: Any
    strip_whitespace: Any
    namespace_separator: Any
    namespaces: Any
    namespace_declarations: Any
    force_list: Any
    def __init__(self, item_depth=0, item_callback=..., xml_attribs=True, attr_prefix='@', cdata_key='#text', force_cdata=False, cdata_separator='', postprocessor=None, dict_constructor=..., strip_whitespace=True, namespace_separator=':', namespaces=None, force_list=None):
        ...
    def _build_name(self, full_name):
        ...
    def _attrs_to_dict(self, attrs):
        ...
    def startNamespaceDecl(self, prefix, uri):
        ...
    def startElement(self, full_name, attrs):
        ...
    def endElement(self, full_name):
        ...
    def characters(self, data):
        ...
    def push_data(self, item, key, data):
        ...
    def _should_force_list(self, key, value):
        ...

def parse(xml_input, encoding=None, expat=..., process_namespaces=False, namespace_separator=':', disable_entities=True, **kwargs):
    ...
def _process_namespace(name, namespaces, ns_sep=':', attr_prefix='@'):
    ...
def _emit(key, value, content_handler, attr_prefix='@', cdata_key='#text', depth=0, preprocessor=None, pretty=False, newl='\n', indent='\t', namespace_separator=':', namespaces=None, full_document=True):
    ...
def unparse(input_dict, output=None, encoding='utf-8', full_document=True, short_empty_elements=False, xml_generator_cls=None, **kwargs):
    ...
def handle_item(path, item):
    ...
