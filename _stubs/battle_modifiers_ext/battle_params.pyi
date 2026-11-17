# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/battle_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from future.utils import listvalues as listvalues, viewitems as viewitems
from typing import Any as Any, Optional as Optional, Set as Set, Tuple as Tuple, Union as Union, TYPE_CHECKING as TYPE_CHECKING
from battle_modifiers_common.battle_modifiers import BattleParams as BattleParams, ModifierScope as ModifierScope
from battle_modifiers_ext.battle_modifier.modifier_appliers import registerParamAppliers as registerParamAppliers
from battle_modifiers_ext.battle_modifier.modifier_helpers import Serializable as Serializable
from battle_modifiers_ext.battle_modifier.modifier_restrictions import readRestrictions as readRestrictions
from battle_modifiers_ext.battle_modifier.modifier_readers import registerParamReaders as registerParamReaders
from battle_modifiers_ext.constants_ext import BATTLE_PARAMS_XML_PATH as BATTLE_PARAMS_XML_PATH, DataType as DataType, UseType as UseType, PhysicalType as PhysicalType, ModifierDomain as ModifierDomain, ClientDomain as ClientDomain
from constants import IS_CLIENT as IS_CLIENT
from extension_utils import ResMgr as ResMgr
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
_ERR_TEMPLATE = "[BattleParams] {} for param '{}'"
g_cache = None

class BaseClientParamData(Serializable):
    __slots__: tuple
    resName: _Any
    domain: _Any
    physicalType: _Any
    useTypes: _Any
    def __init__(self, source, techName):
        ...

class ClientParamData(BaseClientParamData):
    __slots__: tuple
    resName: _Any
    physicalType: _Any
    useTypes: _Any
    domain: _Any
    def __repr__(self):
        ...
    def _initFromConfig(self, clientConfig, techName=''):
        ...
    @classmethod
    def _readResName(cls, techName, _):
        ...
    @staticmethod
    def _readUseTypes(tName, physicalType, dataSection):
        ...
    @staticmethod
    def __readDomain(tName, useTypes, dataSection):
        ...
    @staticmethod
    def __readPhysicalType(tName, dataSection):
        ...

class DefaultClientParamData(BaseClientParamData):
    __slots__: tuple
    def _initFromDescr(self, descr):
        ...
    def _initFromConfig(self, source, *args):
        ...

class FakeClientParamData(ClientParamData):
    __slots__: tuple
    __descr: _Any
    resName: _Any
    domain: _Any
    physicalType: _Any
    useTypes: _Any
    def __init__(self, source, techName):
        ...
    def __repr__(self):
        ...
    def descr(self):
        ...
    @classmethod
    def _readResName(cls, techName, config):
        ...
    @classmethod
    def _readUseTypes(cls, tName, physicalType, dataSection):
        ...
    def _initFromDescr(self, descr):
        ...
    @classmethod
    def __getUseTypes(cls, _):
        ...
    def __makeDescr(self):
        ...

class BaseBattleParam(Serializable):
    __slots__: tuple
    id: _Any
    scope: _Any
    domain: _Any
    clientData: _Any
    def __init__(self, source):
        ...
    def isHashable(self):
        ...

class BattleParam(BaseBattleParam):
    __slots__: tuple
    id: _Any
    dataType: _Any
    scope: _Any
    domain: _Any
    clientData: _Any
    validators: _Any
    minValue: _Any
    maxValue: _Any
    def __repr__(self):
        ...
    @staticmethod
    def readId(config):
        ...
    @staticmethod
    def readDataType(config):
        ...
    @staticmethod
    def readScope(config):
        ...
    @staticmethod
    def readDomain(config):
        ...
    @staticmethod
    def readClientData(config):
        ...
    def isHashable(self):
        ...
    def _initFromConfig(self, config, *args):
        ...

class BattleParamStub(BaseBattleParam):
    __slots__: tuple
    id: _Any
    scope: _Any
    domain: _Any
    def __repr__(self):
        ...
    def _initFromConfig(self, config, *args):
        ...

class FakeBattleParam(BaseBattleParam):
    __slots__: tuple
    __descr: _Any
    id: _Any
    scope: _Any
    domain: _Any
    clientData: _Any
    def __init__(self, source):
        ...
    def __repr__(self):
        ...
    def descr(self):
        ...
    def _initFromDescr(self, descr):
        ...
    def _initFromConfig(self, config, *args):
        ...
    def __initialize(self, source):
        ...
    def __makeDescr(self):
        ...

class BattleParamsCache(object):
    __slots__: tuple
    __params: _Any
    def __init__(self):
        ...
    def __iter__(self):
        ...
    def __getitem__(self, id):
        ...
    def __len__(self):
        ...
    def __contains__(self, id):
        ...
    def __repr__(self):
        ...
    def get(self, id):
        ...
    def __initFromConfig(self):
        ...

def init():
    ...
