# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/comparison_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName
from gui.shared.items_parameters.params import VehicleParams as VehicleParams
from halloween.gui.impl.gen.view_models.views.lobby.comparison_vehicle_model import ComparisonVehicleModel as ComparisonVehicleModel
from halloween.gui.impl.gen.view_models.views.lobby.comparison_view_model import ComparisonViewModel as ComparisonViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView, HWLobbyWindow as HWLobbyWindow
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import COMPARISON_VIEW_ENTER as COMPARISON_VIEW_ENTER, COMPARISON_VIEW_EXIT as COMPARISON_VIEW_EXIT
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys, HWLogActions as HWLogActions
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class ComparisonWindowView(BaseView):
    __slots__: tuple
    layoutID: Any
    _itemsCache: Any
    _halloweenCtrl: Any
    __uiLogger: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getVehicles(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...

class ComparisonWindow(HWLobbyWindow):
    def __init__(self, layoutID, parent=None):
        ...
    def _finalize(self):
        ...
