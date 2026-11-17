# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/ac_visual_script_client/blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script.block import Block as Block, Meta as Meta
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
event_dispatcher: Any
dependency: Any
game_controller: Any
CurrentVehicle: Any

class AdventCalendarMeta(Meta):
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

class OpenAdventCalendar(Block, AdventCalendarMeta):
    _in: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self, *_):
        ...

class OnAdventCalendarConfigChanged(Block, AdventCalendarMeta):
    __adventController: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def __onConfigChanged(self):
        ...

class IsAdventCalendarAvailable(Block, AdventCalendarMeta):
    __adventController: Any
    _isAvailable: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class ADOnPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def __onPreviewVehicleSelected(self):
        ...

class ADIsPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):
    _isSelected: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
