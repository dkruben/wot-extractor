# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewStatus as ViewStatus
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.tank_setup.ammunition_panel.base_view import BaseAmmunitionPanelView as BaseAmmunitionPanelView
from gui.impl.lobby.tank_setup.ammunition_panel.hangar_shells_counter_mapping import ShellCounterMapping as ShellCounterMapping
from gui.impl.lobby.tank_setup.intro_ammunition_setup_view import showIntro as showIntro
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import AmmunitionPanelViewEvent as AmmunitionPanelViewEvent
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from wg_async import wg_async as wg_async
_logger: Any

class HangarAmmunitionPanelView(BaseAmmunitionPanelView):
    _settingsCore: Any
    def update(self, fullUpdate=True):
        ...
    def _updateViewModel(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    # decorador original: @wg_async
    def _onPanelSectionSelected(self, args):
        ...
    def _onChangeSetupIndex(self, args):
        ...
    def __onEscKeyDown(self):
        ...
    def _updateView(self):
        ...
