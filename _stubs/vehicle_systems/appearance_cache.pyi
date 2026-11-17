# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/appearance_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import Event as Event
from skeletons.vehicle_appearance_cache import IAppearanceCache as IAppearanceCache
from soft_exception import SoftException as SoftException
from vehicle_systems.CompoundAppearance import CompoundAppearance as CompoundAppearance
from vehicle_systems.stricted_loading import loadingPriority as loadingPriority
_logger: Any
_AssemblerData: Any

class _LoadInfo(object):
    __slots__: tuple
    appearance: Any
    taskId: Any
    typeDescr: Any
    onConstructed: Any
    def __init__(self, appearance, taskId, typeDescr, onConstructedCallback):
        ...
    def destroy(self):
        ...

class AppearanceCache(IAppearanceCache):
    __slots__: tuple
    __appearanceCache: Any
    __assemblerCache: Any
    __resourceCache: Any
    __loadingAssemblerQueue: Any
    __loadingResourceQueue: Any
    def __init__(self):
        ...
    def getAppearance(self, vId, vInfo, callback=None, strCD=None, needLoad=True):
        ...
    def removeAppearance(self, vId, strCD=None):
        ...
    def stopLoading(self, vId, strCD=None):
        ...
    def loadResources(self, compactDescr, prereqs):
        ...
    def unloadResources(self, compactDescr):
        ...
    def clear(self):
        ...
    def __validateAppearanceCache(self, key):
        ...
    def __validateResourceCache(self, compactDescr):
        ...
    def __construct(self, key, onFinishedCallback):
        ...
    def __load(self, key, info, onLoadedCallback=None):
        ...
    def __onAppearanceLoaded(self, key, resourceRefs):
        ...
    def __onResourceLoaded(self, compactDescr, resourceRefs):
        ...
    @staticmethod
    def __makeUniqueKey(vehID, strCD):
        ...
