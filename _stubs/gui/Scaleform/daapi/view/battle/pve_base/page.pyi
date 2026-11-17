# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.classic import ClassicPage as ClassicPage
from gui.Scaleform.daapi.view.battle.classic.page import COMMON_CLASSIC_CONFIG as COMMON_CLASSIC_CONFIG, EXTENDED_CLASSIC_CONFIG as EXTENDED_CLASSIC_CONFIG, DynamicAliases as DynamicAliases
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.events import ViewEventType as ViewEventType
from pve_battle_hud import WidgetType as WidgetType
from VehicleRespawnComponent import VehicleRespawnComponent as VehicleRespawnComponent
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.minimap import MinimapClientModel as MinimapClientModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.chat import ChatModel as ChatModel
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.respawn_hud import RespawnHUDClientModel as RespawnHUDClientModel
from gui.shared.events import LoadViewEvent as LoadViewEvent
_REMOVED_COMPONENTS: set
_FULL_MAP_HUD_STATE_COMPONENTS: set
_POSTMORTEM_HIDDEN_COMPONENTS: set
_GUI_CONTROL_MODE_CONSUMERS: tuple
_PVE_BASE_CONFIG: Any
_COMMON_CONFIG: Any
_EXTENDED_CONFIG: Any

class PveBaseComponentsConfig(ComponentsConfig):
    def getConfig(self):
        ...
    def __iadd__(self, other):
        ...
    def __add__(self, other):
        ...

class PveBaseBattlePage(ClassicPage):
    __isFullMapVisible: Any
    __defaultStateVisibleComponents: Any
    __currentGUIConsumer: Any
    __canToggleFullMap: Any
    __isChatHidden: Any
    def __init__(self, components=None, external=None, fullStatsAlias=..., **kwargs):
        ...
    @property
    def isFullMapVisible(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _startBattleSession(self):
        ...
    def _stopBattleSession(self):
        ...
    def _toggleFullMap(self, isVisible):
        ...
    def _setComponentsVisibility(self, visible=None, hidden=None):
        ...
    def _filterExistingViewAliases(self, income):
        ...
    def as_isComponentVisibleS(self, componentKey):
        ...
    def _minimapVisibleCmdHandler(self, event):
        ...
    def _settingsChangeHandler(self, settingsID):
        ...
    def _loadViewHandler(self, event):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _onRespawnBaseMoving(self):
        ...
    def _onVehicleRespawned(self, vehicle):
        ...
    def _canShowPostmortemTips(self):
        ...
    def _changeCtrlMode(self, ctrlMode):
        ...
