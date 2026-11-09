# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/repositories.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui.battle_control.arena_info.interfaces import IArenaController as IArenaController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, REUSABLE_BATTLE_CTRL_IDS as REUSABLE_BATTLE_CTRL_IDS, getBattleCtrlName as getBattleCtrlName
from gui.battle_control.controllers import aiming_sounds_ctrl as aiming_sounds_ctrl
from gui.battle_control.controllers import arena_border_ctrl as arena_border_ctrl, arena_load_ctrl as arena_load_ctrl, battle_field_ctrl as battle_field_ctrl, avatar_stats_ctrl as avatar_stats_ctrl, chat_cmd_ctrl as chat_cmd_ctrl, spectator_ctrl as spectator_ctrl, consumables as consumables, debug_ctrl as debug_ctrl, drr_scale_ctrl as drr_scale_ctrl, dyn_squad_functional as dyn_squad_functional, feedback_adaptor as feedback_adaptor, game_messages_ctrl as game_messages_ctrl, hit_direction_ctrl as hit_direction_ctrl, interfaces as interfaces, msgs_ctrl as msgs_ctrl, period_ctrl as period_ctrl, personal_efficiency_ctrl as personal_efficiency_ctrl, team_bases_ctrl as team_bases_ctrl, vehicle_state_ctrl as vehicle_state_ctrl, view_points_ctrl as view_points_ctrl, ingame_help_ctrl as ingame_help_ctrl, vehicle_passenger as vehicle_passenger, vehicles_tracking as vehicles_tracking, default_maps_ctrl as default_maps_ctrl, anonymizer_fakes_ctrl as anonymizer_fakes_ctrl, game_restrictions_msgs_ctrl as game_restrictions_msgs_ctrl, callout_ctrl as callout_ctrl, deathzones_ctrl as deathzones_ctrl, dog_tags_ctrl as dog_tags_ctrl, team_health_bar_ctrl as team_health_bar_ctrl, battle_notifier_ctrl as battle_notifier_ctrl, prebattle_setups_ctrl as prebattle_setups_ctrl, perk_ctrl as perk_ctrl, kill_cam_ctrl as kill_cam_ctrl, commendations_messages_ctrl as commendations_messages_ctrl, spotting_indicators_ctrl as spotting_indicators_ctrl, prefab_effects_availability_ctrl as prefab_effects_availability_ctrl
from gui.battle_control.controllers import map_zones_ctrl as map_zones_ctrl
from gui.battle_control.controllers import points_of_interest_ctrl as points_of_interest_ctrl
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController as DefaultAppearanceCacheController
from gui.battle_control.controllers.appearance_cache_ctrls.event_appearance_cache_ctrl import EventAppearanceCacheController as EventAppearanceCacheController
from gui.battle_control.controllers.appearance_cache_ctrls.maps_training_appearance_cache_ctrl import MapsTrainingAppearanceCacheController as MapsTrainingAppearanceCacheController
from gui.battle_control.controllers.auto_shoot_guns.auto_shoot_ctrl import AutoShootControllerFactory as AutoShootControllerFactory
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.prebattle_highlights.controller import PrebattleHighlightsController as PrebattleHighlightsController
from gui.battle_control.controllers.quest_progress import quest_progress_ctrl as quest_progress_ctrl
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController as ShotsResultSoundController
from gui.battle_control.controllers.sound_ctrls.stronghold_battle_sounds import StrongholdBattleSoundController as StrongholdBattleSoundController
from gui.battle_control.controllers.spam_protection import battle_spam_ctrl as battle_spam_ctrl
from gui.battle_control.controllers.vse_hud_settings_ctrl import vse_hud_settings_ctrl as vse_hud_settings_ctrl
from gui.battle_control.controllers.w2gt import w2gt_ctrl as w2gt_ctrl
from gui.shared.system_factory import registerBattleControllerRepo as registerBattleControllerRepo
from skeletons.gui.battle_session import ISharedControllersLocator as ISharedControllersLocator, IDynamicControllersLocator as IDynamicControllersLocator
from typing import Any as Any, Optional as Optional
from gui.battle_control.arena_info.interfaces import IW2GTBattleController as IW2GTBattleController
from Avatar import PlayerAvatar as PlayerAvatar
_logger: _Any

class BattleSessionSetup(object):
    __slots__: tuple
    avatar: _Any
    replayCtrl: _Any
    gasAttackMgr: _Any
    sessionProvider: _Any
    def __init__(self, avatar=None, replayCtrl=None, gasAttackMgr=None, sessionProvider=None):
        ...
    @property
    def isReplayPlaying(self):
        ...
    @property
    def isReplayRecording(self):
        ...
    @property
    def battleCtx(self):
        ...
    @property
    def arenaDP(self):
        ...
    @property
    def arenaVisitor(self):
        ...
    @property
    def arenaEntity(self):
        ...
    def registerArenaCtrl(self, controller):
        ...
    def registerViewComponentsCtrl(self, controller):
        ...
    def clear(self):
        ...

class _ControllersLocator(object):
    __slots__: tuple
    _repository: _Any
    def __init__(self, repository=None):
        ...
    def destroy(self):
        ...

class SharedControllersLocator(_ControllersLocator, ISharedControllersLocator):
    __slots__: tuple
    @property
    def ammo(self):
        ...
    @property
    def equipments(self):
        ...
    @property
    def optionalDevices(self):
        ...
    @property
    def prebattleSetups(self):
        ...
    @property
    def vehicleState(self):
        ...
    @property
    def vehiclePassenger(self):
        ...
    @property
    def vehiclesTracking(self):
        ...
    @property
    def hitDirection(self):
        ...
    @property
    def arenaLoad(self):
        ...
    @property
    def arenaPeriod(self):
        ...
    @property
    def feedback(self):
        ...
    @property
    def chatCommands(self):
        ...
    @property
    def messages(self):
        ...
    @property
    def drrScale(self):
        ...
    @property
    def privateStats(self):
        ...
    @property
    def crosshair(self):
        ...
    @property
    def personalEfficiencyCtrl(self):
        ...
    @property
    def anonymizerFakesCtrl(self):
        ...
    @property
    def viewPoints(self):
        ...
    @property
    def questProgress(self):
        ...
    @property
    def calloutCtrl(self):
        ...
    @property
    def spectator(self):
        ...
    @property
    def areaMarker(self):
        ...
    @property
    def arenaBorder(self):
        ...
    @property
    def deathzones(self):
        ...
    @property
    def ingameHelp(self):
        ...
    @property
    def mapZones(self):
        ...
    @property
    def killCamCtrl(self):
        ...
    @property
    def aimingSounds(self):
        ...
    @property
    def autoShootCtrl(self):
        ...
    @property
    def battleSpamCtrl(self):
        ...
    @property
    def armorFlashlight(self):
        ...
    @property
    def spottingIndicatorsCtrl(self):
        ...

class DynamicControllersLocator(_ControllersLocator, IDynamicControllersLocator):
    __slots__: tuple
    def getControllerByID(self, ctrlID):
        ...
    @property
    def debug(self):
        ...
    @property
    def teamBases(self):
        ...
    @property
    def progressTimer(self):
        ...
    @property
    def maps(self):
        ...
    @property
    def missions(self):
        ...
    @property
    def respawn(self):
        ...
    @property
    def dynSquads(self):
        ...
    @property
    def battleField(self):
        ...
    @property
    def repair(self):
        ...
    @property
    def playerGameModeData(self):
        ...
    @property
    def teamHealthBar(self):
        ...
    @property
    def gameNotifications(self):
        ...
    @property
    def progression(self):
        ...
    @property
    def radar(self):
        ...
    @property
    def spawn(self):
        ...
    @property
    def deathScreen(self):
        ...
    @property
    def vehicleCount(self):
        ...
    @property
    def perks(self):
        ...
    @property
    def battleHints(self):
        ...
    @property
    def dogTags(self):
        ...
    @property
    def battleNotifier(self):
        ...
    @property
    def soundPlayers(self):
        ...
    @property
    def appearanceCache(self):
        ...
    @property
    def pointsOfInterest(self):
        ...
    @property
    def prebattleSetup(self):
        ...
    @property
    def overrideSettingsController(self):
        ...
    @property
    def shotsResultSound(self):
        ...
    @property
    def vseHUDSettings(self):
        ...
    @property
    def commendationsMessagesController(self):
        ...
    @property
    def w2GTBattleController(self):
        ...
    @property
    def prebattleHighlightsController(self):
        ...

class _EmptyRepository(interfaces.IBattleControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...
    def destroy(self):
        ...
    def getController(self, ctrlID):
        ...
    def addController(self, ctrl):
        ...

class _ControllersRepository(interfaces.IBattleControllersRepository):
    __slots__: tuple
    _ctrls: _Any
    def __init__(self):
        ...
    @classmethod
    def create(cls, setup):
        ...
    def destroy(self):
        ...
    def getController(self, ctrlID):
        ...
    def addController(self, ctrl):
        ...
    def addArenaController(self, ctrl, setup):
        ...
    def addViewController(self, ctrl, setup):
        ...
    def addArenaViewController(self, ctrl, setup):
        ...

class SharedControllersRepository(_ControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...
    @classmethod
    def getMessagesController(cls, setup):
        ...
    @classmethod
    def getOptionalDevicesController(cls, setup):
        ...
    @classmethod
    def getChatCommandsController(cls, setup, feedback, ammo):
        ...
    @classmethod
    def getAreaMarkersController(cls):
        ...
    @classmethod
    def getArenaBorderController(cls):
        ...

class ControllersRepositoryByBonuses(_ControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class ClassicControllersRepository(ControllersRepositoryByBonuses):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...
    @staticmethod
    def _getAppearanceCacheController(setup):
        ...

class EventControllerRepository(ControllersRepositoryByBonuses):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class MapsTrainingControllerRepository(ControllersRepositoryByBonuses):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class StrongholdControllerRepository(ClassicControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...

class PVEBaseControllerRepository(ClassicControllersRepository):
    __slots__: tuple
    @classmethod
    def create(cls, setup):
        ...
