# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from debug_utils import LOG_DEBUG as LOG_DEBUG
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.classic.page import DynamicAliases as DynamicAliases
from gui.Scaleform.daapi.view.battle.shared import drone_music_player as drone_music_player, finish_sound_player as finish_sound_player
from gui.Scaleform.daapi.view.battle.shared.indicators import createPredictionIndicator as createPredictionIndicator
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.impl.gen import R as R
from last_stand.gui.impl.battle.full_stats import FullEventStatsWindow as FullEventStatsWindow, FullEventStatsView as FullEventStatsView
from last_stand.gui.impl.battle.battle_loading_view import BattleLoadingWindow as BattleLoadingWindow
from last_stand.gui.scaleform.daapi.view.battle.indicators import lsCreateDamageIndicator as lsCreateDamageIndicator
from last_stand.gui.scaleform.daapi.view.battle.markers2d.manager import LSMarkersManager as LSMarkersManager
from last_stand.gui.scaleform.daapi.view.battle.players_panel import LSPlayersPanel as LSPlayersPanel
from last_stand.gui.scaleform.daapi.view.battle.shared.crosshair import LSCrosshairPanelContainer as LSCrosshairPanelContainer
from last_stand.gui.scaleform.daapi.view.meta.LastStandBattlePageMeta import LastStandBattlePageMeta as LastStandBattlePageMeta
from last_stand.gui.scaleform.genConsts.LS_BATTLE_VIEW_ALIASES import LS_BATTLE_VIEW_ALIASES as LS_ALIASES
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from PlayerEvents import g_playerEvents as g_playerEvents
import CommandMapping as CommandMapping
_CONFIG: Any
_EXTENDED_CONFIG: Any
_EXTERNAL_COMPONENTS: tuple
_POSTMORTEM_HIDE_VIEW: set
_POSTMORTEM_HIDE_BTN_HINTS: tuple
_BATTLE_LOADING_LAYOUT_ID: Any

class _ComponentsConfig(ComponentsConfig):
    def __init__(self):
        ...

class LastStandBattlePage(LastStandBattlePageMeta):
    CONFIG = _CONFIG
    EXTENDED_CONFIG = _EXTENDED_CONFIG
    POSTMORTEM_HIDE_VIEW = _POSTMORTEM_HIDE_VIEW
    __guiLoader: Any
    __fullStatsIsShown: Any
    _isBattleLoading: Any
    _blToggling: Any
    def __init__(self, components=None, external=..., fullStatsAlias=None):
        ...
    @property
    def hasTabScreen(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _switchToPostmortem(self):
        ...
    def _reloadPostmortem(self):
        ...
    def _getComponentsVideoModeSwitching(self, ctrlMode):
        ...
    def _handleGUIToggled(self, event):
        ...
    def _toggleRadialMenu(self, isShown, allowAction=True):
        ...
    def _toggleFullStats(self, isShown, permanent=None, tabAlias=None):
        ...
    def _onBattleLoadingStart(self):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def _startBattleSession(self):
        ...
    def _stopBattleSession(self):
        ...
    def _canShowPostmortemTips(self):
        ...
    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def __showBattlePageGFComponent(self, layoutID, windowClass):
        ...
    def __destroyBattlePageGFComponent(self, layoutID):
        ...
    def __onPlayerFeedbackReceived(self, feedback):
        ...
    def __onRoundFinished(self, winningTeam, reason):
        ...
