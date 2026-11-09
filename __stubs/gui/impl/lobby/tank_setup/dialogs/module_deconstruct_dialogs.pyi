# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/module_deconstruct_dialogs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
import logging as logging
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.balance import initBalance as initBalance
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.model_formatters import initItemInfo as initItemInfo
from helpers import dependency as dependency
from gui.impl.gen import R as R
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.shared.gui_items.processors.module import ModuleDeconstruct as ModuleDeconstruct
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.confirm_actions_with_equipment_dialog_model import ConfirmActionsWithEquipmentDialogModel as ConfirmActionsWithEquipmentDialogModel, DialogType as DialogType
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.dialogs.ConfirmModuleMeta import MAX_ITEMS_FOR_OPERATION as MAX_ITEMS_FOR_OPERATION
_logger: Any

class DeconstructDialogView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    __itemsCache: Any
    __device: Any
    __currency: Any
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
    # decorador original: @adisp_process
    def __onDeconstruct(self, count):
        ...
    def __onClose(self, *args, **kwargs):
        ...
    def __onMoneyUpdated(self, _):
        ...

class DeconstructDialogWindow(WindowImpl):
    __slots__: tuple
    __blur: Any
    def __init__(self, itemIntCD, parent=None):
        ...
    def _finalize(self):
        ...
