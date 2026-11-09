# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/helpers/server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from fun_random_common.fun_constants import DEFAULT_ASSETS_PACK as DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY as DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY as DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING as UNKNOWN_WWISE_REMAPPING, UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID, FunSubModeImpl as FunSubModeImpl
from shared_utils import makeTupleByDict as makeTupleByDict

# base nao representavel no stub: namedtuple(...)
class FunSubModeClientConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: namedtuple(...)
class FunSubModeFiltrationConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: namedtuple(...)
class FunSubModeSeasonalityConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    def asDict(self):
        ...
    @classmethod
    def __packSeasonalityConfig(cls, data):
        ...

# base nao representavel no stub: namedtuple(...)
class FunSubModeConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        ...
    @classmethod
    def __packConfigPart(cls, configPartCls, configPartName, data):
        ...

# base nao representavel no stub: namedtuple(...)
class FunProgressionConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...

# base nao representavel no stub: namedtuple(...)
class FunMetaProgressionConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def __packProgressionsConfigs(cls, data):
        ...

# base nao representavel no stub: namedtuple(...)
class FunRandomConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    def replace(self, data):
        ...
    @classmethod
    def __filterAllowedFields(cls, data, allowedFields):
        ...
    @classmethod
    def __packMetaProgressionConfig(cls, data):
        ...
    @classmethod
    def __packSubModesConfigs(cls, data):
        ...
