# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dossiers2/common/DossierBuilder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import struct as struct
from typing import Callable as Callable, Tuple as Tuple
from dossiers2.common.DossierDescr import DossierDescr as DossierDescr
from dossiers2.common.DossierBlockBuilders import TYPE_BLOCK_BUILDER as TYPE_BLOCK_BUILDER
from dossiers2.custom.updaters import DossierVersionUpdaterBase as DossierVersionUpdaterBase

class DossierBuilder(object):
    __blockBuilders: Any
    __versionFormat: Any
    __headerFormat: Any
    __latestVersion: Any
    __updater: Any
    __initializer: Any
    __emptyCompDescr: Any
    def __init__(self, blockBuilders, versionFormat, blockSizeFormat, version, updater, initializer):
        ...
    def build(self, compDescr=''):
        ...
