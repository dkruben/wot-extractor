# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import wg_async as wg_async
from persistent_data_cache_common.common import getLogger as getLogger, DEFAULT_SAVING_TIMEOUT as DEFAULT_SAVING_TIMEOUT
from persistent_data_cache_common.manager import ForceCreatingPDCManager as ForceCreatingPDCManager
from persistent_data_cache_common.serializers import defaultSerializer as defaultSerializer
from soft_exception import SoftException as SoftException
from persistent_data_cache_common.manager import DefaultPDCManager as DefaultPDCManager
from persistent_data_cache_common.types import TData as TData, TDataFactory as TDataFactory
from persistent_data_cache_common.serializers import ISerializer as ISerializer
_logger: Any
_g_manager = None

def init(mgr):
    ...
def load(name, factory, serializer=None):
    ...
def start():
    ...
# decorador original: @wg_async.wg_async
def save(timeout=...):
    ...
def fini():
    ...
def isEnabled():
    ...
