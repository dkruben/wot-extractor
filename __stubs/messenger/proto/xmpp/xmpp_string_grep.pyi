# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_string_grep.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import stringprep as stringprep
import unicodedata as unicodedata
from future.utils import lmap as lmap
from past.builtins import unicode as unicode
from soft_exception import SoftException as SoftException
_NODE_PREP_PROHIBITED: set
NodePrep: Any
ResourcePrep: Any

class XmppStringPrepError(SoftException):
    ...

class _StringPrepProfile(object):
    __slots__: tuple
    _unassigned: Any
    _mapping: Any
    _normalization: Any
    _prohibited: Any
    _bidi: Any
    def __init__(self, mapping=None, unassigned=None, normalization=None, prohibited=None, bidi=True):
        ...
    def prepare(self, data):
        ...
    def _doMapping(self, data):
        ...
    def _doNormalization(self, data):
        ...
    def _checkProhibited(self, data):
        ...
    def _checkUnassigned(self, data):
        ...
    def _checkBidi(self, data):
        ...

def doMappingToNothing(char):
    ...
def doMappingSpaceChars(char):
    ...
def normalizeToNFKC(data):
    ...
def normalizeToNFC(data):
    ...
def inNodeProhibitedChars(char):
    ...
def _isCharProhibited(table, char):
    ...
def _isCharUnassigned(table, char):
    ...
