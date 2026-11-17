# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from Avatar import PlayerAvatar as PlayerAvatar
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
from gui.battle_control import avatar_getter as avatar_getter, event_dispatcher as event_dispatcher
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, TabsAliases as TabsAliases
from gui.impl.gen import R as R
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from halloween.gui.impl.battle.full_stats import FullEventStatsWindow as FullEventStatsWindow
from halloween.gui.impl.battle.halloween_battle_loading import HalloweenBattleLoadingWindow as HalloweenBattleLoadingWindow
from halloween.gui.scaleform.daapi.view.battle.indicators import hwCreateDamageIndicator as hwCreateDamageIndicator
from halloween.gui.scaleform.daapi.view.battle.markers2d.manager import HalloweenMarkersManager as HalloweenMarkersManager
from halloween.gui.scaleform.daapi.view.battle.players_panel import HWPlayersPanel as HWPlayersPanel
from halloween.gui.scaleform.daapi.view.battle.shared.crosshair import HalloweenCrosshairPanelContainer as HalloweenCrosshairPanelContainer
from halloween.gui.scaleform.daapi.view.meta.HalloweenBattlePageMeta import HalloweenBattlePageMeta as HalloweenBattlePageMeta
from halloween.gui.scaleform.genConsts.HALLOWEEN_BATTLE_VIEW_ALIASES import HALLOWEEN_BATTLE_VIEW_ALIASES as HW_ALIASES
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from PlayerEvents import g_playerEvents as g_playerEvents
import CommandMapping as CommandMapping
from typing import Optional as Optional
_CONFIG: Any
_EXTENDED_CONFIG: Any
_EXTERNAL_COMPONENTS: tuple
_POSTMORTEM_HIDE_VIEW: set
_ANOMALY_RECIPES_PERMANENT_VIEW: set
_POSTMORTEM_HIDE_BTN_HINTS: tuple
_ROUND_FINISHED_HIDE_VIEW: set

class _ComponentsConfig(ComponentsConfig):
    def __init__(self):
        ...

class HalloweenBattlePage(HalloweenBattlePageMeta):
    sessionProvider: Any
    _guiLoader: Any
    _currentFullScreenAlias: Any
    _hasHints: Any
    _isAutoGuiTogglingActive: Any
    _arenaPeriod: Any
    _isBattleLoading: Any
    _blToggling: Any
    def __init__(self, components=None, external=..., fullStatsAlias=None, **kwargs):
        ...
    def isAnyFullScreenViewVisible(self, viewAlias=None):
        ...
    def isFullScreenVisible(self, viewAlias):
        ...
    def setComponentsVisibilityWithFade(self, visible=None, hidden=None):
        ...
    @property
    def hwBattleGuiCtrl(self):
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
    def _handleHelpEvent(self, event):
        ...
    def _handleToggleFullStatsQuestProgress(self, event):
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
    def __hideBattlePageGFComponent(self, layoutID):
        ...
    def __onPlayerFeedbackReceived(self, feedback):
        ...
    def __onSelectAnomaly(self, _):
        ...
    def __onUpgradeOptionsUpdated(self, newUpgrades):
        ...
    def __onChangeAnomaliesViewVisibility(self, isVisible):
        ...
    def __onRoundFinished(self, winningTeam, reason):
        ...
    def __onAvatarVehicleChanged(self):
        ...
