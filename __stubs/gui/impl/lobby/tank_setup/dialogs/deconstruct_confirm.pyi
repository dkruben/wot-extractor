# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/deconstruct_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from itertools import chain as chain
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CustomSoundButtonPresenter as CustomSoundButtonPresenter, getConfirmButton as getConfirmButton, CancelButton as CancelButton
from gui.impl.gen import R as R
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.confirm_actions_with_equipment_dialog_model import ConfirmActionsWithEquipmentDialogModel as ConfirmActionsWithEquipmentDialogModel, DialogType as LocationDialogType
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.deconstruct_confirm_model import DeconstructConfirmModel as DeconstructConfirmModel, DialogType as ActionDialogType
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.deconstruct_confirm_item_model import DeconstructConfirmItemModel as DeconstructConfirmItemModel
from gui.impl.lobby.tank_setup.array_providers.opt_device import DeconstructOptDeviceStorageProvider as DeconstructOptDeviceStorageProvider, DeconstructOptDeviceOnVehicleProvider as DeconstructOptDeviceOnVehicleProvider, ListTypes as ListTypes
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.balance import initBalance as initBalance
from gui.impl.lobby.tank_setup.dialogs.dialog_helpers.model_formatters import initItemInfo as initItemInfo
from gui.impl.lobby.tank_setup.tooltips.deconstruct_from_inventory_tooltip import DeconstructFromInventoryTooltip as DeconstructFromInventoryTooltip
from gui.impl.lobby.tank_setup.tooltips.deconstruct_from_vehicle_tooltip import DeconstructFromVehicleTooltip as DeconstructFromVehicleTooltip
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_SUBMIT_CLICK_SOUND = 'mod_equipment_disassemble'

class DeconstructMultConfirm(DialogTemplateView):
    itemsCache: Any
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = DeconstructConfirmModel
    ctx: Any
    storageItems: Any
    vehicleItems: Any
    upgradeModulePair: Any
    __tooltipCache: Any
    _storageProvider: Any
    _onVehicleProvider: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    def updateArray(self, array, items, isInventory=False):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _sortItemsKey(self, item):
        ...
    def _update(self):
        ...
    def __initBalance(self):
        ...
    def __onMoneyUpdated(self, _):
        ...

class DeconstructConfirm(DialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = ConfirmActionsWithEquipmentDialogModel
    __itemsCache: Any
    __device: Any
    __currency: Any
    __fromVehicle: Any
    __curCount: Any
    def __init__(self, itemIntCD, fromVehicle=False):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getAdditionalData(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onDeconstruct(self, count):
        ...
    def __onClose(self, *args, **kwargs):
        ...
    def __onMoneyUpdated(self, _):
        ...
