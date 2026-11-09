# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/vehicle_preview_bottom_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelWellMeta import VehiclePreviewBottomPanelWellMeta as VehiclePreviewBottomPanelWellMeta
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from resource_well.gui.feature.constants import PurchaseMode as PurchaseMode
from resource_well.gui.feature.resource_well_helpers import convertPurchaseToEventMode as convertPurchaseToEventMode
from resource_well.gui.impl.gen.view_models.views.lobby.well_panel_model import WellPanelModel as WellPanelModel
from resource_well.gui.shared.event_dispatcher import showResourcesLoadingWindow as showResourcesLoadingWindow
from shared_utils import findFirst as findFirst
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class VehiclePreviewBottomPanel(VehiclePreviewBottomPanelWellMeta):
    __view: Any
    def __init__(self):
        ...
    def _makeInjectView(self, *args):
        ...
    def setRewardID(self, rewardID):
        ...

class _BottomPanelView(ViewImpl):
    __resourceWell: Any
    __rewardID: Any
    __vehicle: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def setRewardID(self, rewardID):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __showResourcesLoading(self):
        ...
    def __updateModel(self):
        ...
    def __onNumberRequesterUpdated(self):
        ...
