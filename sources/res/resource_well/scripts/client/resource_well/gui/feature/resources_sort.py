# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/feature/resources_sort.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/feature/resources_sort.py
from __future__ import absolute_import
import typing
from gui import GUI_NATIONS, NONE_NATION_NAME
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.shared.money import Currency
from resource_well.gui.feature.constants import ResourceType
_NO_NATION_INDEX = 0
_NATIONS_ORDER = {name: idx for idx, name in enumerate(GUI_NATIONS, 1)}
_NATIONS_ORDER[NONE_NATION_NAME] = _NO_NATION_INDEX
_CURRENCY_ORDER = {name: idx for idx, name in enumerate(Currency.GUI_ALL + (CURRENCIES_CONSTANTS.FREE_XP,))}
_RESOURCE_TYPE_ORDER = (
 ResourceType.CURRENCY,
 ResourceType.BLUEPRINTS)

def sortCurrencyResource(resource):
    return _CURRENCY_ORDER.get(resource.guiName, len(_CURRENCY_ORDER))


def sortBlueprintsResource(resource):
    return _NATIONS_ORDER.get(resource.nation, len(_NATIONS_ORDER))


_RESOURCE_SORTERS = {(ResourceType.BLUEPRINTS): sortBlueprintsResource, 
   (ResourceType.CURRENCY): sortCurrencyResource}

def getSorterByResourceType(resourceType):
    return _RESOURCE_SORTERS.get(resourceType)


def sortAnyResource(resource):
    resourceType = ResourceType.getMember(resource.type)
    sorter = getSorterByResourceType(resourceType)
    if resourceType and sorter:
        return (sortByResourceType(resourceType), sorter(resource))
    return (0, 0)


def sortByResourceType(resourceType):
    if resourceType in _RESOURCE_TYPE_ORDER:
        return _RESOURCE_TYPE_ORDER.index(resourceType)
    return len(_RESOURCE_TYPE_ORDER)
