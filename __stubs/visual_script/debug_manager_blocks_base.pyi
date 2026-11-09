# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/debug_manager_blocks_base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import DebugManager as DebugManager
from DebugManager import COLORS as COLORS, isGroupEnabled as isGroupEnabled, setGroupEnabled as setGroupEnabled
from visual_script.block import Block as Block, Meta as Meta
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
DEFAULT_COLOR: Any

class DebugManagerBlockMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class DebugManagerBlock(Block, DebugManagerBlockMeta):
    _params: Any
    _func: Any
    _in: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    def _createDataInputSlot(self, slotName, slotType=..., slotDefaultValue=None):
        ...
    def _eventSlotsEnabled(self):
        ...
    def _nameSlotEnabled(self):
        ...
    def _groupAutoEnable(self):
        ...
    def _slotGetValue(self, slotName):
        ...
    def captionText(self):
        ...

def uint32toInt32(value):
    ...
def int32ToUint32(value):
    ...
