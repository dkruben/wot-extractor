# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/general.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from uuid_utils import genUUID as genUUID
from visual_script.block import Block as Block, makeResEditorData as makeResEditorData, InitParam as InitParam
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class ResourceSelector(Block):
    _res: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
    @classmethod
    def initParams(cls):
        ...

class GenerateUniqueString(Block):
    _prefix: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    def _getData(self):
        ...
