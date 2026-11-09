# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_style_progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelStyleProgressionMeta import VehiclePreviewBottomPanelStyleProgressionMeta as VehiclePreviewBottomPanelStyleProgressionMeta
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.progression_styles.stage_switcher_model import SwitcherType as SwitcherType
from gui.impl.gen.view_models.views.lobby.vehicle_preview.buying_panel.progression_styles_buying_panel_model import ProgressionStylesBuyingPanelModel as ProgressionStylesBuyingPanelModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import BattlePassEvent as BattlePassEvent
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

class VehiclePreviewBottomPanelStyleProgression(VehiclePreviewBottomPanelStyleProgressionMeta):
    __backAlias: Any
    __backCallback: Any
    __styleLevel: Any
    __view: Any
    def __init__(self):
        ...
    def setBackAlias(self, backAlias):
        ...
    def setBackCallback(self, backCallback):
        ...
    def setStyleLevel(self, styleLevel):
        ...
    def setAvailableLevel(self, availableLevel):
        ...
    def setCtx(self, ctx):
        ...
    def _makeInjectView(self):
        ...

class ProgressionStylesBuyingPanelView(ViewImpl):
    __slots__: tuple
    __customizationService: Any
    __hangarSpace: Any
    __styleLevel: Any
    __availableLevel: Any
    __ctx: Any
    def __init__(self, flags=...):
        ...
    @property
    def viewModel(self):
        ...
    def setStyleLevel(self, styleLevel):
        ...
    def setAvailableLevel(self, availableLevel):
        ...
    def setCtx(self, ctx):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onChange(self, *args):
        ...
    def __onVehicleChangeStarted(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __onVehicleLoadStarted(self):
        ...
    def __onVehicleLoadFinished(self):
        ...
    def __unsubscribeEntity(self):
        ...
