# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/resource.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
import typing as typing
from builtins import str as str
from future.utils import itervalues as itervalues, iteritems as iteritems
import nations as nations
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from gui import NONE_NATION_NAME as NONE_NATION_NAME
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData, TooltipData as TooltipData
from gui.shared.money import Currency as Currency
from gui.shared.utils.requesters.blueprints_requester import makeIntelligenceCD as makeIntelligenceCD, makeNationalCD as makeNationalCD, getFragmentNationID as getFragmentNationID
from helpers import dependency as dependency
from resource_well.gui.feature.constants import ResourceType as ResourceType
from resource_well.gui.feature.resources_sort import sortByResourceType as sortByResourceType, getSorterByResourceType as getSorterByResourceType
from shared_utils import findFirst as findFirst
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, List as List, Tuple as Tuple
_INTELLIGENCE_BLUEPRINT = 'intelligence'
_CURRENCY_TOOLTIPS: dict
_RESOURCE_FACTORIES: dict

class Resource(object):
    _itemsCache: Any
    _resourceWell: Any
    _name: Any
    _rate: Any
    _limit: Any
    _type: Any
    def __init__(self, name, rate, limit, resourceType):
        ...
    @property
    def inventoryCount(self):
        ...
    @property
    def tooltip(self):
        ...
    @property
    def name(self):
        ...
    @property
    def rate(self):
        ...
    @property
    def limit(self):
        ...
    @property
    def type(self):
        ...
    @property
    def guiName(self):
        ...
    @property
    def balance(self):
        ...

class CurrencyResource(Resource):
    @property
    def inventoryCount(self):
        ...
    @property
    def tooltip(self):
        ...

class BlueprintResource(Resource):
    _fragmentCD: Any
    def __init__(self, fragmentCD, name, rate, limit, resourceType):
        ...
    @property
    def inventoryCount(self):
        ...
    @property
    def tooltip(self):
        ...
    @property
    def nation(self):
        ...
    @property
    def name(self):
        ...
    def _getTooltipSpecialArgs(self):
        ...

class IntelligenceBlueprintResource(BlueprintResource):
    def __init__(self, fragmentCD, rate, limit, resourceType):
        ...
    @property
    def inventoryCount(self):
        ...
    def _getTooltipSpecialArgs(self):
        ...

class NationalBlueprintResource(BlueprintResource):
    def __init__(self, fragmentCD, rate, limit, resourceType):
        ...
    @property
    def inventoryCount(self):
        ...
    @property
    def nation(self):
        ...
    def _getTooltipSpecialArgs(self):
        ...
    @staticmethod
    def __getNation(fragmentCD):
        ...

def _currencyResourceFactory(resources):
    ...
def _blueprintResourceFactory(resources):
    ...
def processResourcesConfig(resourcesConfig):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def processLoadingResources(rewardID, loadingResources, resourceWell=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def mergeResources(splitResources, rewardID, resourceWell=None):
    ...
def splitResourcesByType(resources):
    ...
