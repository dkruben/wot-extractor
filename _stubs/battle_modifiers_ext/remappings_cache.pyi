# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/remappings_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Any as Any, Dict as Dict, TYPE_CHECKING as TYPE_CHECKING, Optional as Optional
from battle_modifiers_ext.constants_ext import REMAPPING_XML_PATH as REMAPPING_XML_PATH, RemappingNames as RemappingNames
from battle_modifiers_ext.remapping.remapping_readers import ERR_TEMPLATE as ERR_TEMPLATE, readComposers as readComposers, readConditions as readConditions
from extension_utils import ResMgr as ResMgr
from ResMgr import DataSection as DataSection
from soft_exception import SoftException as SoftException
from battle_modifiers_common import ModifiersContext as ModifiersContext
from battle_modifiers_ext.remapping.remapping_composers import IComposer as IComposer
_ERR_TEMPLATE = "[Remapping] {} for remapping '{}'"
g_cache = None

class RemappingCache(object):
    __slots__: tuple
    __remapping: _Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def getValue(self, modifierName, remappingName, oldValue, ctx):
        ...
    def getValues(self, modifierName, remappingName, oldValue):
        ...
    def reloadCache(self, configPath=''):
        ...
    def __readConfig(self, configPath=''):
        ...
    def __readRemappingSection(self, config):
        ...

def init():
    ...
