# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/qa_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, IS_CELLAPP as IS_CELLAPP
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.misc import ASPECT as ASPECT, BLOCK_MODE as BLOCK_MODE, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf

class QAMeta(Meta):
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def mode(cls):
        ...

class TestIdentifier(Block, QAMeta):
    _nameType: Any
    inInt: Any
    outID: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def initParams(cls):
        ...

class TestSlotPyObjectToArrayVSEBlock(Block, QAMeta):
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class Assert(Block, QAMeta):
    _in: Any
    _value: Any
    _msg: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class AddTestResult(Block, QAMeta):
    _in: Any
    _success: Any
    _msg: Any
    _arena: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _storageKey(self):
        ...
    def _execute(self):
        ...
    def onStartScript(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class TestCase(Block):
    _in: Any
    _name: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
