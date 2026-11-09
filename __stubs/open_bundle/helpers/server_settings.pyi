# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/helpers/server_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from shared_utils import makeTupleByDict as makeTupleByDict
_logger: Any

class BundlesConfig(object):
    __slots__: tuple
    __bundles: Any
    def __init__(self, config):
        ...
    def getBundleIDs(self):
        ...
    def getBundles(self):
        ...
    def getBundle(self, bundleID):
        ...

# base nao representavel no stub: namedtuple(...)
class BundleConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def defaults(cls):
        ...
    @classmethod
    def __packStepConfigs(cls, data):
        ...
    @classmethod
    def __packCellConfigs(cls, data):
        ...

# base nao representavel no stub: namedtuple(...)
class StepConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...

# base nao representavel no stub: namedtuple(...)
class CellConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
    @classmethod
    def __packCoordinatesConfig(cls, data):
        ...

# base nao representavel no stub: namedtuple(...)
class CoordinatesConfig:
    __slots__: tuple
    def __new__(cls, **kwargs):
        ...
