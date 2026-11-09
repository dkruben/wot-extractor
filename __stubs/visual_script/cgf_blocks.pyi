# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/cgf_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from visual_script.block import Meta as Meta, Block as Block
from visual_script.misc import ASPECT as ASPECT
from visual_script.contexts.cgf_context import GameObjectWrapper as GameObjectWrapper
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.type import VScriptStructField as VScriptStructField, VScriptStruct as VScriptStruct
from vehicle_filters import getVehicleFilters as getVehicleFilters

class CGFMeta(Meta):
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

class GetEntityGameObject(Block, CGFMeta):
    _entity: Any
    _gameObject: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...

class PrefabsToVehFilter(VScriptStruct):
    filter: Any
    prefabs: Any
    @classmethod
    def vs_aspects(cls):
        ...

class GetPrefabsByVehicleFilter(Block, CGFMeta):
    _in: Any
    _vehicle: Any
    _filters: Any
    _defaultPrefabs: Any
    _out: Any
    _prefabs: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...
