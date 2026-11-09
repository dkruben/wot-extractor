# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/debug_manager_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
from DebugManager import isGroupEnabled as isGroupEnabled
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.debug_manager_blocks_base import DebugManagerBlock as DebugManagerBlock, DEFAULT_COLOR as DEFAULT_COLOR

class DebugManagerRegisterObject(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...
    def _groupAutoEnable(self):
        ...

class DebugManagerClearObject(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...
    def _groupAutoEnable(self):
        ...

class DebugManagerIsGroupEnabled(DebugManagerBlock):
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    def _eventSlotsEnabled(self):
        ...
    def _nameSlotEnabled(self):
        ...
    def _groupAutoEnable(self):
        ...

class DebugManagerRemoveObject(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...
    def _groupAutoEnable(self):
        ...

class DebugManagerRemoveGroup(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...
    def _nameSlotEnabled(self):
        ...
    def _groupAutoEnable(self):
        ...

class DebugManagerShowMessage(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowText2D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowPoint2D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowLine2D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowCircle2D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowRectangle2D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowText3D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowLine3D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowPoint3D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowBox3D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowCircle3D(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowSphere(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...

class DebugManagerShowCylinder(DebugManagerBlock):
    def __init__(self, *args, **kwargs):
        ...
