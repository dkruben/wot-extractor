# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/vehicles_sidebar/vehicles_sidebar_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.customization.vehicles_sidebar.customization_3D_attachments import Customization3DAttachments as Customization3DAttachments
from gui.impl.gen.view_models.views.lobby.customization.vehicles_sidebar.vehicles_sidebar_model import VehiclesSidebarModel as VehiclesSidebarModel
from gui.impl.gen.view_models.views.lobby.customization.vehicles_sidebar.vehicles_sidebar_item_model import VehiclesSidebarItemModel as VehiclesSidebarItemModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.common.components_presenter import ComponentsPresenterView as ComponentsPresenterView
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from uilogging.customization_3d_objects.logger import VehicleSidebarLogger as VehicleSidebarLogger
from uilogging.customization_3d_objects.logging_constants import CustomizationViewKeys as CustomizationViewKeys
_logger: Any

class VehiclesSidebarView(ComponentsPresenterView, FullScreenDialogBaseView):
    __itemsCache: Any
    __service: Any
    __uiLogger: Any
    def __init__(self, layoutID, parentScreen, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateModel(self, model=None):
        ...
    def _registerSubModels(self):
        ...
    def __updateVehiclesModel(self, model=None):
        ...
