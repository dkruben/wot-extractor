# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/entity_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
import Math as Math
import items as items
from constants import IS_CLIENT as IS_CLIENT
from visual_script.block import Meta as Meta, Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class EntityMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class CreateEntity(Block, EntityMeta):
    _in: Any
    _arena: Any
    _type: Any
    _position: Any
    _direction: Any
    _out: Any
    _entity: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...

class CreateApplicationPoint(Block, EntityMeta):
    _in: Any
    _arena: Any
    _vehicle: Any
    _equipmentName: Any
    _position: Any
    _direction: Any
    _level: Any
    _out: Any
    _entity: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...

class DestroyEntity(Block, EntityMeta):
    _in: Any
    _entity: Any
    _ignoreIfMissing: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _execute(self):
        ...

class IsEntityOfType(Block, EntityMeta):
    _types: tuple
    _entity: Any
    _type: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    def _execute(self):
        ...

class BoardEntity(Block, EntityMeta):
    _in: Any
    _entity: Any
    _vehicle: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _exec(self):
        ...

class Teleport(Block, EntityMeta):
    _in: Any
    _entity: Any
    _position: Any
    _direction: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def validate(self):
        ...
    def _exec(self):
        ...

class GetEntityId(Block, EntityMeta):
    _entity: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class GetEntityTransform(Block, EntityMeta):
    _entity: Any
    _position: Any
    _direction: Any
    _yaw: Any
    _pitch: Any
    _roll: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class IsEntityDestroyed(Block, EntityMeta):
    _entity: Any
    _isDestroyed: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _exec(self):
        ...
