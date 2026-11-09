# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/select_slot_spec_compare_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from wg_async import wg_async as wg_async, wg_await as wg_await
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialogs import showSingleDialogWithResultData as showSingleDialogWithResultData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_spec_model import SelectSlotSpecDialogSpecModel as SelectSlotSpecDialogSpecModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.select_slot_spec_compare_dialog_model import SelectSlotSpecCompareDialogModel as SelectSlotSpecCompareDialogModel
from gui.impl.lobby.common.select_slot_spec_dialog import SelectSlotSpecDialogMainContent as SelectSlotSpecDialogMainContent
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from helpers import dependency as dependency
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from frameworks.wulf import Window as Window
_SLOT_IS_NOT_SELECTED_IDX = 0

class SelectSlotSpecCompareDialogMainContent(SelectSlotSpecDialogMainContent):
    _startIdx: Any
    def __init__(self, vehicle, viewModel, slotIdx=None):
        ...
    def setAvailableSpecs(self, model, optDevices):
        ...

class SelectSlotSpecCompareDialog(FullScreenDialogView):
    __slots__: tuple
    __vehicleComparisonBasket: Any
    __vehicle: Any
    __mainContent: Any
    def __init__(self, vehicle):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getAdditionalData(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __serverSettingsChange(self, *_):
        ...

# decorador original: @wg_async
def showDialog(vehicle, parent=None):
    ...
