# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/example.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
from future.utils import lmap as lmap
import BigWorld as BigWorld
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.misc import ASPECT as ASPECT, BLOCK_MODE as BLOCK_MODE, EDITOR_TYPE as EDITOR_TYPE, EDITOR_CUSTOM_ICON as EDITOR_CUSTOM_ICON
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
from visual_script.type import VScriptType as VScriptType, VScriptEnum as VScriptEnum, VScriptStruct as VScriptStruct, VScriptStructField as VScriptStructField

class Example(Meta):
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def mode(cls):
        ...

class HelloFromPython(Block, Example):
    _inSlot: Any
    _outSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class HelloFromPythonOverride(HelloFromPython):
    def _execute(self):
        ...

class StringSelectorExample(Block, Example):
    _inSlot: Any
    _outSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class GetProjectName(Block, Example):
    _outSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class PrintToTerminal(Block, Example):
    _inSlot: Any
    _outSlot: Any
    _msgSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class MulArray(Block, Example):
    _mulValue: Any
    _arrayIn: Any
    _arrayOut: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def mode(cls):
        ...

class SumArray(Block, Example):
    _inArray: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def mode(cls):
        ...

class WeightSequence(Block, Example):
    _in: Any
    _weightSlots: Any
    _outSlots: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def initParams(cls):
        ...

class SelectProjectID(Block, Example):
    convert: dict
    outSlot: Any
    _name: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...

class AnimalComplexKeySelect(Block, Example):
    animals: list
    a: Any
    b: Any
    c: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...

class TestTunableEvent(TunableEventBlock, Example):
    _t: Any
    _a: Any
    _res: Any
    _cbID: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _exec(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class ModeBlock(Block, Example):
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def mode(cls):
        ...

class ClampedBlockEx(Block, Example):
    _int: Any
    _float: Any
    _angle: Any
    _outInt: Any
    _outFloat: Any
    _outAngle: Any
    def __init__(self, *args, **kwargs):
        ...
    def _clampInt(self):
        ...
    def _clampFloat(self):
        ...
    def _clampAngle(self):
        ...

class ClampedBlock(Block, Example):
    _int: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...

class TestStruct(VScriptStruct):
    name: Any
    value: Any
    def __repr__(self):
        ...

class TestType(VScriptType):
    name: Any
    age: Any
    def __init__(self, name, age):
        ...
    @classmethod
    def vs_connectionColor(cls):
        ...

class TestEnum(VScriptEnum):
    A = 0
    B = 1
    C = 2

class MakeTestType(Block, Example):
    _name: Any
    _age: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
    @classmethod
    def mode(cls):
        ...

class BreakTestType(Block, Example):
    _in: Any
    _name: Any
    _age: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execName(self):
        ...
    def _execAge(self):
        ...
    @classmethod
    def mode(cls):
        ...

class MakeTestTypeArray(Block, Example):
    _out: Any
    def __init__(self, *args, **kwargs):
        ...

class SelectTest(Block, Example):
    _enum: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class PrintTestStruct(Block, Example):
    _in: Any
    _out: Any
    _s: Any
    _ns: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class TestOnResult(Block, Example):
    _in: Any
    _a: Any
    _out: Any
    _onResult: Any
    _sqr: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
