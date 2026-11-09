# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/deconstruction_device_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from itertools import chain as chain
import adisp as adisp
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_pop_over import BackportPopOverContent as BackportPopOverContent, createPopOverData as createPopOverData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.deconstruction_device_view_model import DeconstructionDeviceViewModel as DeconstructionDeviceViewModel
from gui.impl.lobby.tank_setup.array_providers.opt_device import DeconstructOptDeviceOnVehicleProvider as DeconstructOptDeviceOnVehicleProvider, DeconstructOptDeviceStorageProvider as DeconstructOptDeviceStorageProvider
from gui.impl.lobby.tank_setup.backports.tooltips import OptDeviceTooltipBuilder as OptDeviceTooltipBuilder
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.items_actions.actions import ItemSellSpec as ItemSellSpec, ItemDeconstructSpec as ItemDeconstructSpec
from gui.shared.money import Currency as Currency
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
ItemDeconstructContext: Any
Cart: Any

class DeconstructionDeviceView(ViewImpl):
    itemsCache: Any
    __slots__: tuple
    _upgradedItemPair: Any
    _storageProvider: Any
    _onVehicleProvider: Any
    _cart: Any
    __deconstructedCallback: Any
    def __init__(self, upgradedItemPair=None, onDeconstructedCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def createPopOverContent(self, event):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _updateView(self, fullUpdate=False):
        ...
    def _fillUpgradedItem(self):
        ...
    def _fillVehicle(self):
        ...
    def _updateSlots(self, ctx=None, fullUpdate=True, updateData=True):
        ...
    def _updateCounters(self, ctx):
        ...
    def _updateItemByFilter(self):
        ...
    def __fillModules(self):
        ...
    def _onOkClick(self):
        ...
    def _onCloseClick(self):
        ...
    def _onModuleAdd(self, event):
        ...
    def _onModuleReduce(self, event):
        ...
    # decorador original: @adisp.adisp_process
    def __makeAction(self, callback=None):
        ...
    def _getBackportTooltipData(self, event):
        ...
    def __onMoneyUpdated(self, _):
        ...

class DeconstructionDeviceWindow(WindowImpl):
    __slots__: tuple
    __blur: Any
    def __init__(self, upgradedPair=None, parent=None, onDeconstructedCallback=None):
        ...
    def _finalize(self):
        ...
