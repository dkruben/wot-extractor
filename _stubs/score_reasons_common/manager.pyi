# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/common/score_reasons_common/manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from score_reasons_common.schemas.base import ExtensionSchema as ExtensionSchema, ScoreReasonModel as ScoreReasonModel
from typing import Optional as Optional, List as List, Dict as Dict
import section2dict as section2dict
from dict2model import exceptions as exceptions
from extension_utils import ResMgr as ResMgr
_logger: Any
_g_manager = None
DEFAULT_XML = 'scripts/item_defs/score_reasons/score_reasons.xml'

class ScoreReasonsModelsManager(object):
    _UNIQUE_NAME_PARTS_COUNT = 3
    _UNIQUE_NAME_SCOPE_INDEX = 1
    __slots__: tuple
    _reasons: Any
    _reasonsByScope: Any
    def __init__(self):
        ...
    def getScoreReasonModel(self, uniqueName):
        ...
    def getAllUniqueNames(self):
        ...
    @property
    def reasonsByScope(self):
        ...
    def getUniqueNamesByScope(self, scopeKey):
        ...
    def isReasonInScope(self, uniqueName, scopeType):
        ...
    def _registerFromXml(self, xmlPath):
        ...

def _readScoreReasonsXml(xmlPath):
    ...
def init():
    ...
def get():
    ...
