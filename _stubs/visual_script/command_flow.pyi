# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/command_flow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block, Meta as Meta
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class _CommandFlowMeta(Meta):
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
    def blockAspects(cls):
        ...

class MutexGate(Block, _CommandFlowMeta):
    _input: Any
    _lockSlot: Any
    _releaseSlot: Any
    _lockedAtStart: Any
    _outSlot: Any
    _isLocked: Any
    _isReady: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def lock(self):
        ...
    def tryActivate(self):
        ...
    def release(self):
        ...
