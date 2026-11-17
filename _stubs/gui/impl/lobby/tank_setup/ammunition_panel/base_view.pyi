# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/base_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from Event import Event as Event
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_context_menu import BackportContextMenuWindow as BackportContextMenuWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel as AmmunitionPanelViewModel
from gui.impl.lobby.tank_setup.ammunition_panel.hangar import HangarAmmunitionPanel as HangarAmmunitionPanel
from gui.impl.lobby.tank_setup.backports.context_menu import getHangarContextMenuData as getHangarContextMenuData
from gui.impl.lobby.tank_setup.backports.tooltips import getSlotTooltipData as getSlotTooltipData, getSlotSpecTooltipData as getSlotSpecTooltipData
from gui.impl.lobby.tank_setup.tank_setup_helper import setLastSlotAction as setLastSlotAction, clearLastSlotAction as clearLastSlotAction
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import AmmunitionPanelViewEvent as AmmunitionPanelViewEvent
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_logger: Any

class BaseAmmunitionPanelView(ViewImpl):
    _VIEW_MODEL = AmmunitionPanelViewModel
    _itemsCache: Any
    _hangarSpace: Any
    __slots__: tuple
    _ammunitionPanel: Any
    _wasVehicleOnLoading: Any
    onPanelSectionResized: Any
    onVehicleChanged: Any
    def __init__(self, flags=...):
        ...
    def createToolTip(self, event):
        ...
    def createContextMenu(self, event):
        ...
    def setHangarSwitchAnimState(self, isComplete):
        ...
    def setPrbSwitching(self, value):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def vehItem(self):
        ...
    def setLastSlotAction(self, *args, **kwargs):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def update(self, fullUpdate=True):
        ...
    def destroy(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _createAmmunitionPanel(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onPanelSectionSelected(self, args):
        ...
    def _onPanelSectionResized(self, kwargs):
        ...
    def _currentVehicleChanged(self):
        ...
    def _onDequeued(self, *args, **kwargs):
        ...
    def __onVehicleChangeStarted(self):
        ...
    def __itemCacheChanged(self, *_):
        ...
    @staticmethod
    def _getIsDisabled():
        ...
    def _getIsReady(self):
        ...
    def __canChangeVehicle(self):
        ...
    def _updateView(self):
        ...
    def _getBackportTooltipData(self, event):
        ...
