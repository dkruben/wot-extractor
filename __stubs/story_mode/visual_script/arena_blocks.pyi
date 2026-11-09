# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/visual_script/arena_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from story_mode_common.story_mode_constants import MissionId as MissionId, MissionsDifficulty as MissionsDifficulty
from visual_script import ASPECT as ASPECT
from visual_script.arena_blocks import ArenaMeta as ArenaMeta
from visual_script.block import Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
story_mode_missions: Any

class GetStoryModeDifficulty(Block, ArenaMeta):
    _arena: Any
    _result: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getResult(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...
