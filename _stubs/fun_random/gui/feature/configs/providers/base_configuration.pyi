# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/providers/base_configuration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import schemas as schemas
from gui.shared.utils.functions import deepMergeDicts as deepMergeDicts
from soft_exception import SoftException as SoftException
from dict2model import models as models
g_configurationsCache: dict

class FunBaseConfigurationProvider(object):
    _CONFIGURATION_SCHEMA: Any
    _EMPTY_CONFIGURATION_PATH = ''
    _configurationModel: Any
    def __init__(self, overridesPath, *args):
        ...
    @classmethod
    def initConfigurationsCache(cls):
        ...
    @classmethod
    def getConfigurationByPath(cls, configPath, overridesPath=''):
        ...
    def getConfigurationModel(self):
        ...
    def _getRuntimeConfiguration(self, *args):
        ...
