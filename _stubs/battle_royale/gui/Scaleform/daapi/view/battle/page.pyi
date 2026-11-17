# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from BattleReplay import g_replayEvents as g_replayEvents
from battle_royale.gui.Scaleform.daapi.view.battle.respawn_message_panel import RespawnMessagePanel as RespawnMessagePanel
from gui.battle_control.event_dispatcher import toggleCrosshairVisibility as toggleCrosshairVisibility
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
import PlayerEvents as PlayerEvents
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ARENA_PERIOD as ARENA_PERIOD
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from gui.battle_control import avatar_getter as avatar_getter
from Event import EventsSubscriber as EventsSubscriber
from battle_royale.gui.Scaleform.daapi.view.battle.markers2d.manager import BattleRoyaleMarkersManager as BattleRoyaleMarkersManager
from battle_royale.gui.Scaleform.daapi.view.battle.player_format import BattleRoyalePlayerFullNameFormatter as BattleRoyalePlayerFullNameFormatter
from battle_royale.gui.Scaleform.daapi.view.battle.spawned_bot_msg import SpawnedBotMsgPlayerMsgs as SpawnedBotMsgPlayerMsgs
from battle_royale.gui.Scaleform.daapi.view.battle.minefield_player_messenger import MinefieldPlayerMessenger as MinefieldPlayerMessenger
from gui.Scaleform.daapi.view.meta.BattleRoyalePageMeta import BattleRoyalePageMeta as BattleRoyalePageMeta
from gui.Scaleform.daapi.view.battle.classic.page import DynamicAliases as DynamicAliases
from gui.Scaleform.daapi.view.battle.shared import crosshair as crosshair, drone_music_player as drone_music_player
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig as ComponentsConfig
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from battle_royale.gui.battle_control.controllers.spawn_ctrl import ISpawnListener as ISpawnListener
from battle_royale.gui.br_effect_player import BRUpgradeEffectPlayer as BRUpgradeEffectPlayer
from battle_royale.gui.game_control.br_battle_messages import ProgressionMessagesPlayer as ProgressionMessagesPlayer
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BRBattleSoundController as BRBattleSoundController, RadarSoundPlayer as RadarSoundPlayer, LevelSoundPlayer as LevelSoundPlayer, EnemiesAmountSoundPlayer as EnemiesAmountSoundPlayer, PhaseSoundPlayer as PhaseSoundPlayer, PostmortemSoundPlayer as PostmortemSoundPlayer, InstallModuleSoundPlayer as InstallModuleSoundPlayer, EquipmentSoundPlayer as EquipmentSoundPlayer, SelectRespawnSoundPlayer as SelectRespawnSoundPlayer, ArenaPeriodSoundPlayer as ArenaPeriodSoundPlayer
_BATTLE_ROYALE_CFG: Any

class _DynamicAliases(CONST_CONTAINER):
    SELECT_RESPAWN_SOUND_PLAYER = 'selectRespawnSoundPlayer'
    PROGRESSION_MESSAGES_PLAYER = 'progressionMessagesPlayer'
    RADAR_SOUND_PLAYER = 'radarSoundPlayer'
    LEVEL_SOUND_PLAYER = 'levelSoundPlayer'
    ENEMIES_AMOUNT_SOUND_PLAYER = 'enemiesAmountSoundPlayer'
    PHASE_SOUND_PLAYER = 'phaseSoundPlayer'
    POSTMORTEM_SOUND_PLAYER = 'postmortemSoundPlayer'
    INSTALL_MODULE_SOUND_PLAYER = 'installModuleSoundPlayer'
    ARENA_PERIOD_SOUND_PLAYER = 'arenaPeriodSoundPlayer'
    EQUIPMENT_SOUND_PLAYER = 'equipmentSoundPlayer'
    VEH_UPGRADE_EFFECT_PLAYER = 'vehicleUpgradeEffectPlayer'
    SPAWNED_BOT_MSG_PUBLISHER = 'SpawnedBotMsgPublisher'
    MINEFIELD_MSG_PUBLISHER = 'MinefieldMsgPublisher'
    RESPAWN_PANEL = 'RespawnPanel'

class _BattleRoyaleComponentsConfig(ComponentsConfig):
    def __init__(self):
        ...

class BattleRoyalePage(BattleRoyalePageMeta, ISpawnListener):
    __PANELS_FOR_SHOW_HIDE: list
    __battleRoyaleController: Any
    __selectSpawnToggling: Any
    __winScreenToggling: Any
    __brSoundControl: Any
    __isFullStatsShown: Any
    __isWinnerScreenShown: Any
    __panelsIsVisible: Any
    __es: Any
    __isAllowToogleGuiVisible: Any
    __canShowHUD: Any
    __hudComponents: Any
    _isInPostmortem: Any
    _fsToggling: Any
    def __init__(self, components=None, **kwargs):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...
    def isFullStatsShown(self):
        ...
    def _onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    @property
    def isPostmortemTipsVisible(self):
        ...
    def _canShowPostmortemTips(self):
        ...
    def _updatePostmortemTips(self):
        ...
    def __onRespawnTimeFinished(self):
        ...
    def _onDefeatedTeamsUpdated(self, *_):
        ...
    def _toggleFullStats(self, isShown, permanent=None, tabAlias=None):
        ...
    def _toggleRadialMenu(self, isShown, allowAction=True):
        ...
    def _populate(self):
        ...
    def _onWinScreenReload(self):
        ...
    def _startBattleSession(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onBattleLoadingFinish(self):
        ...
    def _setComponentsVisibility(self, visible=None, hidden=None):
        ...
    def _toggleGuiVisible(self):
        ...
    def _dispose(self):
        ...
    def _switchToPostmortem(self):
        ...
    def _getComponentsVideoModeSwitching(self, ctrlMode):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __onCameraChanged(self, ctrlMode, _=None):
        ...
    def __onConfWindowTriggered(self, isOpened):
        ...
    def __getProgressionWindowCtrl(self):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onHideDeathScreen(self):
        ...
    def __onShowDeathScreen(self):
        ...
    def __onWinnerScreen(self, *_):
        ...
    def __onTimeWarpStart(self):
        ...
    def __hideRadialMenu(self):
        ...
    @property
    def __isDeadAfterRespawnTimeFinished(self):
        ...
