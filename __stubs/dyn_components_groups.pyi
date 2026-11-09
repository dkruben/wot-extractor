# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dyn_components_groups.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from functools import partial as partial
from cache import cached_property as cached_property
from constants import IS_CELLAPP as IS_CELLAPP
from extension_utils import importClass as importClass, ResMgr as ResMgr
from py2to3.backport.inspect import getargspec as getargspec
from soft_exception import SoftException as SoftException
from xml_config_specs import ObjParam as ObjParam
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Dict as Dict, List as List, Tuple as Tuple, Any as Any
from ResMgr import DataSection as DataSection

class _UnregisteredComponentConfig(object):
    ...

class DynComponentsGroupsRepo(object):
    _CONFIG = 'scripts/item_defs/dyn_components_groups.xml'
    _DOMAIN: _Any
    _RELOAD = False
    _reader = None
    @classmethod
    def init(cls):
        ...
    @classmethod
    def getGroup(cls, groupName):
        ...

class DynComponentsGroupsReader(object):
    _configPath: _Any
    _domain: _Any
    _hotReload: _Any
    _groups: _Any
    def __init__(self, configPath, domain='', hotReload=False):
        ...
    def getGroup(self, groupName):
        ...
    def _readGroups(self, section):
        ...
    def _readGroup(self, section):
        ...
    @classmethod
    def _createInitParams(cls, compCls, cfg, kwargs):
        ...
    @staticmethod
    def _getParam(paramName, cfg, kwargs, defaults):
        ...

def groupComponent(**specs):
    ...
