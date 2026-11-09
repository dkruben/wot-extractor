# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_style_buying.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info import dyn_currencies_utils as dyn_utils
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.style_buying import StyleBuyingProcessor as StyleBuyingProcessor
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelStyleBuyingMeta import VehiclePreviewBottomPanelStyleBuyingMeta as VehiclePreviewBottomPanelStyleBuyingMeta
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_preview.buying_panel.style_buying_panel_model import StyleBuyingPanelModel as StyleBuyingPanelModel, StyleBuyingStatus as StyleBuyingStatus
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from typing import Dict as Dict, Optional as Optional
from gui.shared.gui_items.customization.c11n_items import Style as Style

class VehiclePreviewBottomPanelStyleBuying(VehiclePreviewBottomPanelStyleBuyingMeta):
    __view: Any
    def __init__(self):
        ...
    def setStyleInfo(self, style, price, level):
        ...
    def setBuyParams(self, buyParams):
        ...
    def _makeInjectView(self):
        ...

class _StyleBuyingPanelView(ViewImpl):
    __slots__: tuple
    __battlePass: Any
    __customizationService: Any
    __itemsCache: Any
    __hangarSpace: Any
    __ordPrice: Any
    __dynPrice: Any
    __level: Any
    __buyingProcessor: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def setStyleInfo(self, style, price, level):
        ...
    def setBuyParams(self, buyParams):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __onVehicleChangeStarted(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __onVehicleLoadStarted(self):
        ...
    def __onVehicleLoadFinished(self):
        ...
    def __updateVMData(self, *_):
        ...
    def __prepareVMData(self):
        ...
    def __applyStyle(self):
        ...
    def __onBuy(self, *_):
        ...
