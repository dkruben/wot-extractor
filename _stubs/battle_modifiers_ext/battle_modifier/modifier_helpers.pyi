# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/battle_modifier/modifier_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as Any, Optional as Optional, Callable as Callable, Union as Union, Tuple as Tuple, Dict as Dict
from ResMgr import DataSection as DataSection
from battle_modifiers_ext.constants_ext import UseType as UseType
from soft_exception import SoftException as SoftException

class Serializable(object):
    def __init__(self, source, *args):
        ...
    def descr(self):
        ...
    def _initFromDescr(self, descr):
        ...
    def _initFromConfig(self, source, *args):
        ...

def makeUseTypeMethods(method, copy=False):
    ...
def createLevelTag(level):
    ...
def parseLevelTag(levelTag):
    ...
