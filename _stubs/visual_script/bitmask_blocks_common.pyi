# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/bitmask_blocks_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import long as long, xrange as xrange
from visual_script.block import Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue, Meta as Meta
from visual_script.misc import errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE, BLOCK_MODE as BLOCK_MODE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class BitMaskMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class BitMaskBase(Block, BitMaskMeta):
    _MASK_TYPES: dict
    _flags: Any
    _inFlags: Any
    _bitMask: Any
    def __init__(self, *args, **kwargs):
        ...
    def _addInputNode(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def _getValue(self):
        ...

class BitwiseOperationBase(Block, BitMaskMeta):
    _masks: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    @property
    def _maskValues(self):
        ...
    def _addInputNode(self):
        ...
    def _addOutputNode(self):
        ...
    def _getValue(self):
        ...
    @classmethod
    def mode(cls):
        ...
