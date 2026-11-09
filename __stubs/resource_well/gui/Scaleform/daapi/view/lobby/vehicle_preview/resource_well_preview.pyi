# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/Scaleform/daapi/view/lobby/vehicle_preview/resource_well_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl.gen.view_models.views.lobby.vehicle_preview.top_panel.top_panel_tabs_model import TabID as TabID
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_PREVIEW_SOUND_SPACE as RESOURCE_WELL_PREVIEW_SOUND_SPACE, SOUNDS as SOUNDS
from resource_well.gui.shared import events as events
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class ResourceWellVehiclePreview(VehiclePreview):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_PREVIEW_SOUND_SPACE
    __hangarSpace: Any
    __resourceWell: Any
    __numberStyle: Any
    __rewardID: Any
    __isBackClicked: Any
    def __init__(self, ctx):
        ...
    def setBottomPanel(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _processBackClick(self, ctx=None):
        ...
    def _getExitEvent(self):
        ...
    def __onViewOpened(self, *_):
        ...
    def __onViewClosed(self, *_):
        ...
    def __onEventStateUpdated(self):
        ...
