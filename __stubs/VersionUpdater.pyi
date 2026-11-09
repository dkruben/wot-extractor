# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/VersionUpdater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
from past.builtins import xrange as xrange
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV

class VersionUpdaterBase(object):
    latestVersion: Any
    _startVersion: Any
    _updaters: Any
    _template: Any
    _latestVersion: Any
    _module: Any
    def __init__(self, template, latestVersion, moduleWithUpdaters=None):
        ...
    def __buildUpdaters(self):
        ...
    def __getUpdaters(self, startVersion):
        ...
    def _updateToLatestVersion(self, versionOrGetter, checkerForCallback, logID, *args):
        ...
