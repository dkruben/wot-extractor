# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/SpaceVisibilityFlags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from constants import ARENA_GAMEPLAY_IDS as ARENA_GAMEPLAY_IDS, HANGAR_VISIBILITY_TAGS as HANGAR_VISIBILITY_TAGS
from extension_utils import ResMgr as ResMgr
from soft_exception import SoftException as SoftException
from debug_utils import LOG_WARNING as LOG_WARNING

class SpaceVisibilityFlagsFactory(object):
    _g_cache: dict
    @staticmethod
    def create(geometryName):
        ...

class SpaceVisibilityFlags(object):
    FLAGS_CONFIG_SECTION = 'spaceVisibilityFlags'
    _CONFIG_FILE = 'space.settings'
    _HANGAR_CONFIG_SECTION = 'hangarSettings'
    _CONFIG_DIRECTORY = 'spaces'
    _ERROR_BIT_INDEX = -1
    _SERVER_FLAGS_NUMBER = 20
    types: Any
    typeIDToIndex: Any
    def __init__(self, geometryName):
        ...
    def getMaskForGameplayID(self, gameplayID):
        ...
    def getMaskForGameplayIDs(self, gameplayIDs):
        ...
    def __formMapping(self, flagsSection):
        ...
    @staticmethod
    def __isHangarSpace(settingsSection):
        ...
    @staticmethod
    def __formSettingPath(geometryName):
        ...

def _openSection(path):
    ...
