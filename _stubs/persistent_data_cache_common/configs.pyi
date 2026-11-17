# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/persistent_data_cache_common/configs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from soft_exception import SoftException as SoftException
from persistent_data_cache_common.types import TPDCVersion as TPDCVersion

class BasePDCConfig(object):
    __slots__: tuple
    version: Any
    cacheFilePath: Any
    def __init__(self, version, cacheFilePath):
        ...
    def __repr__(self):
        ...
