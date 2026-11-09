# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/configurations/opt_device.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from account_helpers.AccountSettings import AccountSettings as AccountSettings, SHOW_OPT_DEVICE_HINT_TROPHY as SHOW_OPT_DEVICE_HINT_TROPHY, SHOW_OPT_DEVICE_HINT as SHOW_OPT_DEVICE_HINT, SHOW_OPT_MODERNIZED_DEVICE_HINT as SHOW_OPT_MODERNIZED_DEVICE_HINT
from gui.impl.auxiliary.selected_filters import BaseSelectedFilters as BaseSelectedFilters
from gui.impl.common.tabs_controller import tabUpdateFunc as tabUpdateFunc
from gui.impl.lobby.tank_setup.configurations.base import BaseTankSetupTabsController as BaseTankSetupTabsController
from gui.impl.lobby.tank_setup.array_providers.opt_device import SimpleOptDeviceProvider as SimpleOptDeviceProvider, DeluxeOptDeviceProvider as DeluxeOptDeviceProvider, TrophyOptDeviceProvider as TrophyOptDeviceProvider, ModernisedOptDeviceProvider as ModernisedOptDeviceProvider
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from items.components.supply_slots_components import SlotCategories as SlotCategories
from skeletons.gui.shared import IItemsCache as IItemsCache

class OptDeviceTabs(object):
    SIMPLE = 'simple'
    DELUXE = 'deluxe'
    TROPHY = 'trophy'
    MODERNIZED = 'modernized'
    ALL: tuple

class OptDeviceTabsController(BaseTankSetupTabsController):
    __slots__: tuple
    def getDefaultTab(self):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateSimple(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateModernized(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateTrophy(self, viewModel, isFirst=False):
        ...
    # decorador original: @tabUpdateFunc(...)
    def _updateDeluxe(self, viewModel, isFirst=False):
        ...
    def tabOrderKey(self, tabName):
        ...
    def getTabCurrency(self, tabName):
        ...
    def _getAllProviders(self):
        ...
    def __updateSpecial(self, viewModel, tabName, isFirst):
        ...

class OptDeviceSelectedFilters(BaseSelectedFilters):
    __slots__: tuple
    FIREPOWER = SlotCategories.FIREPOWER
    SURVIVABILITY = SlotCategories.SURVIVABILITY
    MOBILITY = SlotCategories.MOBILITY
    STEALTH = SlotCategories.STEALTH
    def changeFilter(self, filterName, model):
        ...
    def __init__(self):
        ...
    @staticmethod
    def __firepowerFilter(item):
        ...
    @staticmethod
    def __survivabilityFilter(item):
        ...
    @staticmethod
    def __mobilityFilter(item):
        ...
    @staticmethod
    def __stealthFilter(item):
        ...

class OptDeviceIntroductionController(object):
    itemsCache: Any
    TROPHY_INTRO = 'trophy'
    DELUXE_INTRO = 'deluxe'
    MODERNIZED_INTRO = 'modernized'
    SETTINGS: dict
    INTRO_BY_TAB: dict
    @classmethod
    def getIntroduction(cls, tabName, hasItems):
        ...
    @classmethod
    def setIntroductionValue(cls, introName):
        ...

def getOptDeviceTabByItem(item):
    ...
