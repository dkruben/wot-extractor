# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/scene_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.arena_blocks import ArenaMeta as ArenaMeta
from material_kinds import EFFECT_MATERIAL_NAMES_BY_INDEXES as EFFECT_MATERIAL_NAMES_BY_INDEXES, EFFECT_MATERIAL_INDEXES_BY_IDS as EFFECT_MATERIAL_INDEXES_BY_IDS

class GetSpaceId(Block, ArenaMeta):
    _spaceId: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetSpaceName(Block, ArenaMeta):
    _spaceName: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetTerrainMaterialUnderPoint(Block, ArenaMeta):
    _in: Any
    _spaceID: Any
    _position: Any
    _dropDistance: Any
    _out: Any
    _material: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class TerrainIndexToName(Block, ArenaMeta):
    _in: Any
    _index: Any
    _out: Any
    _material: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
