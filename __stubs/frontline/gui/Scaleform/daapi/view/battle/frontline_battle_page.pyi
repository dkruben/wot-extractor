# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD
from frontline.gui.Scaleform.daapi.view.battle.frontline_crosshair import FrontlineCrosshairPanelContainer as FrontlineCrosshairPanelContainer
from frontline.gui.Scaleform.daapi.view.battle.frontline_drone_music_player import FrontlineDroneMusicPlayer as FrontlineDroneMusicPlayer
from frontline.gui.Scaleform.daapi.view.battle.frontline_finish_sound_player import FrontlineFinishSoundPlayer as FrontlineFinishSoundPlayer
from frontline.gui.Scaleform.daapi.view.battle.frontline_markers2d import FrontlineMarkersManager as FrontlineMarkersManager
from frontline.gui.Scaleform.daapi.view.meta.FrontlineBattlePageMeta import FrontlineBattlePageMeta as FrontlineBattlePageMeta
from frontline.gui.Scaleform.genConsts.FRONTLINE_BATTLE_VIEW_ALIASES import FRONTLINE_BATTLE_VIEW_ALIASES as FRONTLINE_BATTLE_VIEW_ALIASES
from gui.Scaleform.daapi.view.battle.classic.page import DynamicAliases as ClassicDynAliases
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import KillCamMarkersManager as KillCamMarkersManager
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.daapi.view.battle.shared.start_countdown_sound_player import StartCountdownSoundPlayer as StartCountdownSoundPlayer
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.sound_ctrls.epic_battle_sounds import EpicBattleSoundController as EpicBattleSoundController
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic
FRONTLINE_BATTLE_CLASSIC_CONFIG: Any
_FRONTLINE_BATTLE_CLASSICS_COMPONENTS = FRONTLINE_BATTLE_CLASSIC_CONFIG
_FRONTLINE_BATTLE_EXTENDED_COMPONENTS: Any
_NEVER_HIDE: set
_GAME_UI: set
_SPECTATOR_UI: set
_POSTMORTEM_UI: set
_ENABLE_CONTROL_MODE: set
_PAGE_STATE_TO_CONTROL_PARAMS: dict
_STATE_TO_UI: dict
_FRONTLINE_EXTERNAL_COMPONENTS: tuple

class DynamicAliases(CONST_CONTAINER):
    EPIC_FINISH_SOUND_PLAYER = 'epicFinishSoundPlayer'
    EPIC_DRONE_MUSIC_PLAYER = 'epicDroneMusicPlayer'

class _FrontlineBattleComponentsConfig(ComponentsConfig):
    def __init__(self):
        ...

class PageStates(object):
    NONE = -1
    GAME = 0
    LOADING = 1
    TABSCREEN = 2
    OVERVIEWMAP = 3
    RADIAL = 4
    RESPAWN = 5
    COUNTDOWN = 6
    SPECTATOR_FREE = 7
    SPECTATOR_FOLLOW = 8
    SPECTATOR_DEATHCAM = 9
    GAME_OVER = 10

class FrontlineBattlePage(FrontlineBattlePageMeta, BattleGUIKeyHandler):
    __currPeriod: Any
    __epicSoundControl: Any
    __pageState: Any
    __topState: Any
    __activeState: Any
    __respawnAvailable: Any
    _isInPostmortem: Any
    def __init__(self, components=None, external=..., fullStatsAlias=...):
        ...
    @staticmethod
    def _swapVisibleStates(visibleUI, hiddenUI, value, fromVisibleUI=False):
        ...
    def _invalidateState(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __arena_onPeriodChange(self, period, *args):
        ...
    def handleEscKey(self, isDown):
        ...
    def _handleToggleOverviewMap(self, event):
        ...
    def _handleToggleFullStats(self, event):
        ...
    def _onBattleLoadingStart(self):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def _toggleRadialMenu(self, isShown, allowAction=True):
        ...
    def _toggleFullStats(self, isShown, permanent=None, tabAlias=None):
        ...
    def _toggleOverviewMap(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def _handleGUIToggled(self, event):
        ...
    def __onSpectatorModeChanged(self, mode):
        ...
    def __onRespawnVisibility(self, isVisible, fromTab=False):
        ...
    def _onPostMortemReload(self):
        ...
    def __onPostmortemDisable(self):
        ...
    def _onAvatarCtrlModeChanged(self, ctrlMode):
        ...
    def __onRoundFinished(self, winningTeam, reason):
        ...
    def __checkOverviewMap(self):
        ...
    def __checkRadialMenu(self):
        ...
    def _startBattleSession(self):
        ...
    def _stopBattleSession(self):
        ...
    def onDeactivateRadialMenu(self):
        ...
