# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/top_panel_tabs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from frameworks.wulf import Array as Array, ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.meta.VehiclePreviewTopPanelTabsMeta import VehiclePreviewTopPanelTabsMeta as VehiclePreviewTopPanelTabsMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_preview.top_panel.top_panel_tabs_model import TabID as TabID, TopPanelTabsModel as TopPanelTabsModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showStylePreview as showStylePreview, showVehiclePreviewWithoutBottomPanel as showVehiclePreviewWithoutBottomPanel
from shared_utils import first as first
from typing import Dict as Dict, Optional as Optional, Tuple as Tuple
from gui.shared.gui_items.customization.c11n_items import Style as Style
_logger: Any
_TAB_COMMAND: dict
_TAB_CUSTOM_NAME_GETTER: dict
PERSONAL_NUMBER_STYLE_TABS: tuple

class VehiclePreviewTopPanelTabs(VehiclePreviewTopPanelTabsMeta):
    __view: Any
    def __init__(self):
        ...
    def setData(self, **kwargs):
        ...
    def setParentCtx(self, **kwargs):
        ...
    def _makeInjectView(self, *args):
        ...

class VehiclePreviewTopPanelTabsView(ViewImpl):
    __parentCtx: Any
    __tabIDs: Any
    __currentTabID: Any
    __style: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def setData(self, tabIDs, currentTabID, style):
        ...
    def setParentCtx(self, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __updateVMData(self, *_):
        ...
    def __onTabChanged(self, *args, **kwargs):
        ...
    def __makeTopPanelData(self):
        ...
    def __processPersonalNumberStyleTab(self):
        ...
