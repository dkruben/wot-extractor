# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/respawn_ammunition_panel_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event, EventManager as EventManager
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.battle_control.event_dispatcher import showIngameMenu as showIngameMenu
from gui.impl.common.ammunition_panel.ammunition_groups_controller import GROUPS_MAP as GROUPS_MAP
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.battle_page.respawn_ammunition_panel_view_model import RespawnAmmunitionPanelViewModel as RespawnAmmunitionPanelViewModel
from frontline.gui.impl.battle.battle_page.ammunition_panel.ammunition_panel import FLRespawnAmmunitionPanel as FLRespawnAmmunitionPanel
from gui.impl.pub import ViewImpl as ViewImpl

class RespawnAmmunitionPanelView(ViewImpl):
    __slots__: tuple
    __ammunitionPanel: Any
    __vehicle: Any
    __eventManager: Any
    onSwitchLayout: Any
    def __init__(self, vehicle):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createContextMenu(self, event):
        ...
    def updateViewVehicle(self, vehicle, fullUpdate=True):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onChangeSetupByButton(self, args):
        ...
    def __changeSetup(self, hudGroupID, newLayoutIdx=None):
        ...
    def __setVehicleData(self):
        ...
    def __onEscKeyDown(self):
        ...
