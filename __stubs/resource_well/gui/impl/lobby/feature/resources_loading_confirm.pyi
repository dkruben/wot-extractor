# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/resources_loading_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from helpers import dependency as dependency
from resource_well.gui.feature.resource_well_helpers import fillVehicleCounter as fillVehicleCounter
from resource_well.gui.feature.resources_sort import sortAnyResource as sortAnyResource
from resource_well.gui.impl.gen.view_models.views.lobby.loading_resource_model import LoadingResourceModel as LoadingResourceModel
from resource_well.gui.impl.gen.view_models.views.lobby.resources_loading_confirm_model import ResourcesLoadingConfirmModel as ResourcesLoadingConfirmModel, OperationType as OperationType
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
_FULL_PROGRESS = 100

class ResourcesLoadingConfirm(FullScreenDialogView):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __rewardID: Any
    __resources: Any
    __tooltips: Any
    __additionalData: Any
    __operation: Any
    def __init__(self, rewardID, resources, isReturnOperation):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _getAdditionalData(self):
        ...
    def _setBaseParams(self, model):
        ...
    def __fillResources(self, resourceModels):
        ...
    def __fillResourceModel(self, resource, count, resourceModel):
        ...
    def __onNumberRequesterUpdated(self):
        ...
    def __onEventStateUpdated(self):
        ...
    def __onCancelAction(self):
        ...
