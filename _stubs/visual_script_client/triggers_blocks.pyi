# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/triggers_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from visual_script.block import Block as Block, Meta as Meta
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.misc import ASPECT as ASPECT
from constants import IS_VS_EDITOR as IS_VS_EDITOR

class TriggerMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class TriggerExternal(Block, TriggerMeta):
    _subscribeSlot: Any
    _unsubscribeSlot: Any
    _eventIDSlot: Any
    _isActiveInputSlot: Any
    _outSlot: Any
    _active: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def isActive(self):
        ...
    def setActive(self, value):
        ...
    def _onTrigger(self, eventId, *args, **kwargs):
        ...
    def _onSubscribe(self):
        ...
    def _onUnsubscribe(self):
        ...
