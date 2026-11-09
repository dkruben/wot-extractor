# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/ammunition_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import wg_async as future_async
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel as AmmunitionPanelViewModel
from gui.impl.lobby.tank_setup.backports.tooltips import getSlotSpecTooltipData as getSlotSpecTooltipData
from gui.impl.lobby.tank_setup.tank_setup_helper import setLastSlotAction as setLastSlotAction, NONE_ID as NONE_ID
from gui.impl.lobby.vehicle_compare.panel import CompareAmmunitionPanel as CompareAmmunitionPanel
from gui.impl.lobby.vehicle_compare.select_slot_spec_compare_dialog import showDialog as showDialog
from gui.impl.lobby.vehicle_compare.tooltips import getCmpSlotTooltipData as getCmpSlotTooltipData
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showCompareAmmunitionSelectorView as showCompareAmmunitionSelectorView

class CompareAmmunitionPanelView(ViewImpl):
    __slots__: tuple
    __vehItem: Any
    __ammunitionPanel: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def update(self):
        ...
    def updateSection(self, sectionName):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onPanelSlotClear(self, args):
        ...
    @staticmethod
    def __onPanelSectionSelected(args):
        ...
    @staticmethod
    def __onEscKeyDown():
        ...
    def __onSlotAction(self, *args, **kwargs):
        ...
    def __onDragDropSwap(self, args):
        ...
    # decorador original: @future_async.wg_async
    def __onSpecializationSelect(self, *_):
        ...
    def __sendDragAndDropSlotAction(self, sectionName, currentLayout, leftID, rightID):
        ...
