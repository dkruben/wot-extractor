# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/arena_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Math as Math
from soft_exception import SoftException as SoftException
from visual_script.block import Meta as Meta, Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.misc import errorVScript as errorVScript, ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf

class ArenaMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...

class GetUDOByNameBase(Block, ArenaMeta):
    _UDOTypes: list
    _nameType: Any
    _type: Any
    _exclude: Any
    _UDOs: Any
    _firstUDO: Any
    _name: Any
    _names: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def captionText(self):
        ...
    def _getAll(self):
        ...
    def _getFirst(self):
        ...
    def _getUDOsOfType(self, typeName):
        ...
    def _allValidUDOs(self):
        ...

class GetDataFromStorageBase(Block, ArenaMeta):
    componentName: Any
    _valueType: Any
    componentSlot: Any
    _keySlot: Any
    _valueSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def _exec(self):
        ...

class GetFlyDirection(Block, ArenaMeta):
    _arena: Any
    _teamID: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def _exec(self):
        ...
