# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_serial_vehicles_confirm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from helpers import dependency as dependency
from resource_well.gui.feature.resource_well_helpers import fillVehicleCounter as fillVehicleCounter
from resource_well.gui.impl.gen.view_models.views.lobby.no_serial_vehicles_confirm_model import NoSerialVehiclesConfirmModel as NoSerialVehiclesConfirmModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class NoSerialVehiclesConfirm(FullScreenDialogView):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __rewardID: Any
    __additionalData: Any
    def __init__(self, rewardID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
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
    def __onNumberRequesterUpdated(self):
        ...
    def __onEventStateUpdated(self):
        ...
    def __onCancelAction(self):
        ...
