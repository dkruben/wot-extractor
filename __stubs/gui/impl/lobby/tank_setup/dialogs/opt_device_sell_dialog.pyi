# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/opt_device_sell_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import MAX_ITEMS_FOR_OPERATION as MAX_ITEMS_FOR_OPERATION
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sell_view_model import SellViewModel as SellViewModel, ModuleType as ModuleType
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.balance import initBalance as initBalance
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.gui_items.processors.module import ModuleSeller as ModuleSeller
from gui.shared.money import Currency as Currency
from gui.shared.utils import decorators as decorators
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice

class OptDeviceSellDialog(ViewImpl):
    __itemsCache: Any
    __slots__: tuple
    LAYOUT_ID: Any
    __device: Any
    def __init__(self, itemIntCD):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onClose(self, *args, **kwargs):
        ...
    def __onMoneyUpdated(self, _):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __onSell(self, count):
        ...

class OptDeviceSellDialogWindow(WindowImpl):
    __slots__: tuple
    __blur: Any
    def __init__(self, itemIntCD, parent=None):
        ...
    def _finalize(self):
        ...

def _initItem(viewModel, device, currency):
    ...
