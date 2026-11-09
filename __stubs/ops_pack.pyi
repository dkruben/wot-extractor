# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/ops_pack.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from future.utils import iteritems as iteritems
from past.builtins import unicode as unicode, xrange as xrange
from external_strings_utils import truncate_utf8 as truncate_utf8
from soft_exception import SoftException as SoftException
MAX_PASCAL_STRING_LEN = 65535

class OpsPacker:
    _packedOps: Any
    def __init__(self):
        ...
    def storeOp(self, op, *args):
        ...
    def _getOpPack(self, op, *args):
        ...
    def _appendOp(self, op, packedArgs):
        ...
    def popPackedOps(self):
        ...

class OpsUnpacker:
    def storeOp(self, op, *args):
        ...
    def _appendOp(self, op, packedArgs):
        ...
    def _onUnpackedOp(self, opCode):
        ...
    def unpackOps(self, packedOps=''):
        ...

def packPascalString(s):
    ...
def unpackPascalString(bufferString, offset=0):
    ...
def initOpsFormatDef(opsFormatDefs):
    ...
