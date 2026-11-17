# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/prebattle_ammunition_panel_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import CommandMapping as CommandMapping
from Event import Event as Event, EventManager as EventManager
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.battle.battle_page.ammunition_panel.ammunition_panel import PrebattleAmmunitionPanel as PrebattleAmmunitionPanel
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import COMMAND_MAPPING as COMMAND_MAPPING
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP as GROUPS_MAP
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_panel_view_model import PrebattleAmmunitionPanelViewModel as PrebattleAmmunitionPanelViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.tooltips.consumables_panel import makeShellTooltip as makeShellTooltip, buildEquipmentSlotTooltipTextBySlotInfo as buildEquipmentSlotTooltipTextBySlotInfo
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from typing import Optional as Optional
from frameworks.wulf import ViewEvent as ViewEvent, View as View
_R_SIMPLE_TOOLTIPS: tuple

class PrebattleAmmunitionPanelView(ViewImpl):
    __slots__: tuple
    __settingsCore: Any
    __ammunitionPanel: Any
    __vehicle: Any
    __eventManager: Any
    onSwitchLayout: Any
    onViewLoaded: Any
    def __init__(self, vehicle, *args):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
    def setNextShellCD(self, shellCD):
        ...
    def setCurrentShellCD(self, shellCD):
        ...
    def updateViewActive(self, isActive):
        ...
    def updateViewVehicle(self, vehicle, fullUpdate=True):
        ...
    def updateState(self, state):
        ...
    def setTimer(self, timeLeft):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, currShellCD, nextShellCD, state, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onChangeSetupByButton(self, args):
        ...
    def __onChangeSetupByKey(self, event):
        ...
    def __changeSetup(self, hudGroupID, newLayoutIdx=None):
        ...
    def __onSettingsApplied(self, diff):
        ...
