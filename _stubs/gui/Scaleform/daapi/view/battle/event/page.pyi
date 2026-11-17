# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from debug_utils import LOG_DEBUG as LOG_DEBUG
from adisp import adisp_process as adisp_process
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import KillCamMarkersManager as KillCamMarkersManager
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer as CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage as ClassicPage
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.event.manager import EventMarkersManager as EventMarkersManager
from gui.shared.events import LoadViewEvent as LoadViewEvent
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
EVENT_CONFIG: Any
_TUTORIAL_PAGES: tuple
_EVENT_EXTERNAL_COMPONENTS: tuple

class EventBattlePage(ClassicPage):
    __isRadialMenuShown: Any
    def __init__(self, components=None, external=..., fullStatsAlias=None, **kwargs):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _startBattleSession(self):
        ...
    def _stopBattleSession(self):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __handleFadeOutAndIn(self, event):
        ...
    # decorador original: @adisp_process
    def __fadeProcess(self, settings):
        ...
    def _toggleRadialMenu(self, isShown, allowAction=True):
        ...
    def _toggleEventStats(self, isShown):
        ...
    def _onBattleLoadingStart(self):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def __enterRadialHUD(self):
        ...
    def __exitRadialHUD(self):
        ...
    def __handleToggleEventStats(self, event):
        ...
    def __handleRadialAction(self, _):
        ...
    def _handleGUIToggled(self, event):
        ...
