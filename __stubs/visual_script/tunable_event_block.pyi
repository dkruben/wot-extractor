# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/tunable_event_block.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from functools import wraps as wraps
from visual_script.block import Block as Block
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class TunableEventBlock(Block):
    _EVENT_SLOT_NAMES: list
    __out: Any
    _active: Any
    _maxCount: Any
    _cooldown: Any
    __lastCallTime: Any
    __currentCount: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def _isReady(self):
        ...
    def _push(self):
        ...
    @staticmethod
    def eventProcessor(func):
        ...
    def validate(self):
        ...
