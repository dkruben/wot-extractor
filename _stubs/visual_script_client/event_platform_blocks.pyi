# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/event_platform_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
import Math as Math
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
battle_session: Any
dependency: Any
Avatar: Any

class EventPlatformMeta(Meta):
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class AddMarkerAtPoint(Block, EventPlatformMeta):
    guiSessionProvider: Any
    _position: Any
    _markerType: Any
    _markerID: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def _execute(self):
        ...

class RemoveMarkerAtPoint(Block, EventPlatformMeta):
    guiSessionProvider: Any
    _number: Any
    _in: Any
    _out: Any
    _markerIds: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def _execute(self):
        ...
    @classmethod
    def initParams(cls):
        ...
