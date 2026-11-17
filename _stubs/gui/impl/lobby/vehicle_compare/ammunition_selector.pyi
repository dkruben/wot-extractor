# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/ammunition_selector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.warning_tooltip_view_model import WarningDescription as WarningDescription
from gui.impl.gen.view_models.views.lobby.tank_setup.vehicle_compare_ammunition_setup_model import VehicleCompareAmmunitionSetupModel as VehicleCompareAmmunitionSetupModel
from gui.impl.lobby.tank_setup.main_tank_setup.base import MainTankSetupView as MainTankSetupView
from gui.impl.lobby.tank_setup.tooltips.warning_tooltip_view import WarningTooltipView as WarningTooltipView
from gui.impl.lobby.vehicle_compare.builder import CompareTankSetupBuilder as CompareTankSetupBuilder
from gui.impl.lobby.vehicle_compare.tooltips import getCmpSlotTooltipData as getCmpSlotTooltipData
from gui.impl.lobby.tank_setup.tooltips.setup_tab_tooltip_view import SetupTabTooltipView as SetupTabTooltipView
from gui.impl.pub import ViewImpl as ViewImpl

class CompareAmmunitionSelectorView(ViewImpl):
    __slots__: tuple
    _vehItem: Any
    _selectedSlotID: Any
    _tankSetup: Any
    def __init__(self, layoutID, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, selectedSection='', selectedSlot=None):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onViewRendered(self):
        ...
    def __onAnimationEnd(self):
        ...
    def __onClose(self):
        ...
    def __onItemSelected(self, *_):
        ...
