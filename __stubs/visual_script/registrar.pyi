# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/registrar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import inspect as inspect
from visual_script.block import Block as Block
from visual_script.context import VScriptContext as VScriptContext
from visual_script.type import VScriptType as VScriptType, VScriptEnum as VScriptEnum, VScriptStruct as VScriptStruct
__all__: list

class VSBlockRegistrar(object):
    _aspects: Any
    _domainBlocks: Any
    _domainContexts: Any
    _domainTypes: Any
    _domainEnums: Any
    _domainStructs: Any
    _isEngineLoadBlocks: Any
    _isEngineLoadContexts: Any
    _isEngineLoadTypes: Any
    def __init__(self, *aspect):
        ...
    @property
    def aspects(self):
        ...
    def regBlock(self, block):
        ...
    def regBlocksFromModule(self, module):
        ...
    def getBlocks(self):
        ...
    def regContext(self, ctx):
        ...
    def getContexts(self):
        ...
    def regType(self, cls):
        ...
    def regTypesFromModule(self, module):
        ...
    def getTypes(self):
        ...
    def getEnums(self):
        ...
    def getStructs(self):
        ...

def _findVScriptConponentsInModule(module, cls):
    ...
def _collectContextMetaData(cls):
    ...
