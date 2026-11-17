# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/br_battle_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import WWISE as WWISE
from constants import ATTACK_REASON as ATTACK_REASON, DIRECT_DETECTION_TYPE as DIRECT_DETECTION_TYPE
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import getEquipmentById as getEquipmentById, getSmokeDataByPredicate as getSmokeDataByPredicate
from gui.battle_control.battle_constants import PLAYER_GUI_PROPS as PLAYER_GUI_PROPS
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersController as SoundPlayersController, VehicleStateSoundPlayer as VehicleStateSoundPlayer, BaseEfficiencySoundPlayer as BaseEfficiencySoundPlayer, EquipmentComponentSoundPlayer as EquipmentComponentSoundPlayer
from gui.doc_loaders.battle_royale_settings_loader import getBattleRoyaleSettings as getBattleRoyaleSettings
from helpers import dependency as dependency
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, TIMER_VIEW_STATE as TIMER_VIEW_STATE, COUNTDOWN_STATE as COUNTDOWN_STATE
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from constants import LootAction as LootAction
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, isItemVehicleHull as isItemVehicleHull
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.battle_control.arena_info import vos_collections as vos_collections
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as PERSONAL_EFFICIENCY_TYPE
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BATTLE_EVENT_TYPE
from Math import Matrix as Matrix
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments, BattleRoyaleComponents as BattleRoyaleComponents
from battle_royale.gui.shared.events import AirDropEvent as AirDropEvent
from PlayerEvents import g_playerEvents as g_playerEvents
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener
from battle_royale.gui.battle_control.controllers.spawn_ctrl import ISpawnListener as ISpawnListener
from battle_royale.gui.battle_control.controllers.radar_ctrl import IRadarListener as IRadarListener
from battle_royale.gui.battle_control.controllers.vehicles_count_ctrl import IVehicleCountListener as IVehicleCountListener
from vehicle_systems.tankStructure import TankSoundObjectsIndexes as TankSoundObjectsIndexes
import BattleReplay as BattleReplay
from items import vehicles as vehicles
from items.battle_royale import isSpawnedBot as isSpawnedBot
from gui.battle_control.arena_info.settings import VehicleSpottedStatus as VehicleSpottedStatus
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
_logger: Any

class BREvents(object):
    LOOT_PICKUP_START = 'BR_loot_pickup_start'
    LOOT_PICKUP_DONE = 'BR_loot_pickup_end'
    LOOT_PICKUP_STOP = 'BR_loot_pickup_stop'
    RADAR_ACTIVATED = 'BR_radar_mine'
    RADAR_ACTIVATED_SQUAD = 'BR_radar_ally'
    SPAWN_MINE = 'BR_spawn_mine'
    SPAWN_ALLY = 'BR_spawn_ally'
    SPAWN_TIMER = 'BR_timer'
    SPAWN_TIMER_WARNING = 'BR_timer_warning'
    AIRDROP_SPAWNED = 'BR_airdrop'
    DEATHZONE_ENTER: dict
    DEATHZONE_EXIT: dict
    LEVEL_UP = 'BR_levelup'
    LEVEL_UP_MAX = 'BR_levelup_max'
    UPGRADE_PANEL_SHOW = 'BR_widget_on'
    UPGRADE_PANEL_HIDE = 'BR_widget_off'
    VEH_CONFIGURATOR_SHOW = 'BR_upgrade_view_on'
    VEH_CONFIGURATOR_HIDE = 'BR_upgrade_view_off'
    BATTLE_SUMMARY_SHOW = 'BR_result_screen'
    BR_RESULT_PROGRESS_BAR_STOP = 'BR_result_progress_bar_stop'
    INSTALL_MODULE: dict
    INSTALL_MODULE_CHASSIS = 'BR_upgrade_treads'
    INSTALL_MODULE_HULL = 'BR_upgrade_hull'
    PHASE_MIDDLE = 'BR_combat_phase_activated'
    PLAYER_LEVEL_MIDDLE = 'BR_combat_phase_our'
    SOLO_ENEMIES_AMOUNT: dict
    SQUAD_ENEMIES_AMOUNT: dict
    ENEMY_KILLED = 'BR_enemy_killed'
    REBORN = 'BR_reborn'
    CHARGE_REVIVAL = 'BR_charge_revival'
    PLATOON_REVIVAL_POSSIBLE_SOON = 'BR_platoon_revival_possible_soon'
    PLATOON_REVIVAL_POSSIBLE = 'BR_platoon_revival_possible'
    REVIVAL_EXPIRE_SOON = 'BR_revival_expire_soon'
    REVIVAL_IMPOSSIBLE = 'BR_revival_impossible'
    BATTLE_STARTED = 'BR_start_battle'
    BATTLE_WIN = 'BR_win'
    BATTLE_DEFEAT = 'BR_defeat'
    BERSERKER_ACTIVATION = 'BR_perk_berserker_activation'
    BERSERKER_DEACTIVATION = 'BR_perk_berserker_deactivation'
    BERSERKER_PULSE_RED = 'BR_perk_berserker_pulse_red'
    EQUIPMENT_ACTIVATED: dict
    EQUIPMENT_DEACTIVATED: dict
    TRAP_POINT_ENTER = 'BR_perk_trap_slowdown_affects'
    TRAP_POINT_EXIT = 'BR_perk_trap_slowdown_affects_off'
    REPAIR_POINT_ENTER = 'BR_perk_repairpoint_affects'
    REPAIR_POINT_EXIT = 'BR_perk_repairpoint_affects_off'
    HEAL_POINT_ENTER = 'BR_perk_healzone_affects'
    HEAL_POINT_EXIT = 'BR_perk_healzone_affects_off'
    AIRSTRIKE_AFFECTS = 'BR_perk_airstrike_affects'
    KAMIKAZE_HITS_TARGET = 'BR_perk_kamikaze_hits_target'
    KAMIKAZE_TARGET_LOST = 'BR_perk_kamikaze_target_lost'
    KAMIKAZE_DETECTED = 'BR_brander_detected'
    MINEFIELD_ACTIVATION = 'BR_perk_minefield_activation'
    MINEFIELD_HIT_TARGET = 'BR_perk_minefield_hits_target'
    MINEFIELD_TIMER = 'BR_perk_minefield_timer'
    MINEFIELD_TIMER_STOP = 'BR_perk_minefield_timer_stop'
    MINEFIELD_TIMER_RTPC = 'RTPC_ext_minefield_timer'
    BR_SMOKE_DAMGE_AREA_ENTER = 'BR_smoke_damge_affects'
    BR_SMOKE_DAMGE_AREA_EXIT = 'BR_smoke_damage_affects_off'
    BR_FIRE_CIRCLE_ENTERED = 'BR_perk_fire_circle_affect'
    BR_FIRE_CIRCLE_LEFT = 'BR_perk_fire_circle_affect_off'
    BR_CLING_BRANDER_DESTROYED = 'BR_perk_clingbrander_destroyed'
    BR_SHOT_PASSION_AFFECT = 'BR_perk_shotpassion_affect'
    BR_SHOT_PASSION_AFFECT_OFF = 'BR_perk_shotpassion_affect_off'
    EQUIPMENT_PREPARING: dict
    @staticmethod
    def playSound(eventName):
        ...
    @staticmethod
    def playSoundPos(eventName, pos):
        ...
    @staticmethod
    def getSoundObject(name, pos):
        ...

class BRStates(object):
    STATE_PHASE = 'STATE_BR_gameplay_music_phase'
    STATE_PHASE_START = 'STATE_BR_gameplay_music_phase_start'
    STATE_PHASE_MIDDLE = 'STATE_BR_gameplay_music_phase_middle'
    STATE_PHASE_FINAL = 'STATE_BR_gameplay_music_phase_final'
    STATE_STATUS = 'STATE_BR_gameplay_music_status'
    STATE_STATUS_EXPLORING = 'STATE_BR_gameplay_music_status_exploring'
    STATE_STATUS_COMBAT = 'STATE_BR_gameplay_music_status_combat'
    STATE_POSTMORTEM = 'STATE_postmortem_mode'
    STATE_POSTMORTEM_OFF = 'STATE_postmortem_mode_off'
    STATE_POSTMORTEM_ON = 'STATE_postmortem_mode_on'
    STATE_BR = 'STATE_BR_gameplay'
    STATE_BR_ON = 'STATE_BR_gameplay_on'
    STATE_BR_OFF = 'STATE_BR_gameplay_off'
    STATE_DEATHZONE: dict
    STATE_DEATHZONE_IN: dict
    STATE_DEATHZONE_OUT: dict
    @staticmethod
    def setState(stateName, stateValue):
        ...

class BREventParams(object):
    SHOT_PASSION_MULTIPLIER = 'RTPC_ext_shotpassion_affect'
    @staticmethod
    def setEventParam(paramName, paramValue):
        ...

class BRBattleSoundController(SoundPlayersController):
    _soundPlayers: Any
    def __init__(self):
        ...

class RadarSoundPlayer(IRadarListener):
    def radarInfoReceived(self, radarInfo):
        ...

class LootSoundPlayer(VehicleStateSoundPlayer):
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...

class ClingBranderSoundPlayer(object):
    __sessionProvider: Any
    __CLING_BRANDER_VEH_NAME = 'china:Ch00_ClingeBot_SH'
    def init(self):
        ...
    def destroy(self):
        ...
    def __onVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...

class RevivalSoundPlayer(CallbackDelayer):
    __sessionProvider: Any
    __REVIVAL_IMPOSSIBLE_LIVES_AMOUNT = -1
    __isAlive: Any
    __lives: Any
    __respawnTimestampSent: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onPlayerVehicleAliveChanged(self, isAlive):
        ...
    def __onLivesChanged(self, lives):
        ...
    def __onPeriodChange(self, period, endTime, length, additionalInfo):
        ...
    @staticmethod
    def __getTimeGoneFromStart(endTime, length):
        ...
    def __revivalExpiresSoon(self):
        ...
    def __revivalImpossible(self):
        ...
    def __onVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
    @property
    def __isSquad(self):
        ...
    @property
    def __isRevivalPossible(self):
        ...
    @staticmethod
    def __isSummonedVehicle(veh):
        ...
    def __getAlly(self):
        ...

class DeathScreenSoundPlayer(object):
    __sessionProvider: Any
    def init(self):
        ...
    def destroy(self):
        ...
    def __onShowDeathScreen(self):
        ...

class DeathzoneSoundPlayer(VehicleStateSoundPlayer):
    __isInZone: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stopEvent(self):
        ...

class InstallModuleSoundPlayer(IProgressionListener, IViewComponentsCtrlListener):
    __sessionProvider: Any
    __PLAYER_MIDDLE_LEVEL = 4
    def setVehicleChangeResponse(self, intCD, success):
        ...

class AirDropSoundPlayer(object):
    def init(self):
        ...
    def destroy(self):
        ...
    def __onAirDropSpawned(self, _):
        ...

class LevelSoundPlayer(IProgressionListener):
    __sessionProvider: Any
    __level: Any
    def __init__(self):
        ...
    def updateData(self, arenaLevelData):
        ...

class EnemiesAmountSoundPlayer(IVehicleCountListener):
    __sessionProvider: Any
    __enemiesCount: Any
    __frags: Any
    def __init__(self):
        ...
    def setVehicles(self, count, _, __):
        ...
    def setFrags(self, frags, isPlayerVehicle):
        ...

class PhaseSoundPlayer(IProgressionListener, IVehicleCountListener):
    __slots__: tuple
    __averageLevel: Any
    __enemyTeamsCount: Any
    __currentState: Any
    __finalPhaseEnemiesCount: Any
    __middlePhaseAverageLevel: Any
    def __init__(self):
        ...
    def setVehicles(self, _, __, teamsCount):
        ...
    def setAverageBattleLevel(self, level):
        ...
    def __updatePhase(self):
        ...
    def __setSoundState(self, state):
        ...

class StatusSoundPlayer(VehicleStateSoundPlayer, CallbackDelayer):
    __ON_OBSERVED_DURATION = 20.0
    __seenEnemies: Any
    __isObservedByEnemy: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def destroy(self):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, _):
        ...
    def __onVehicleLeaveWorld(self, vId):
        ...
    def __onObservedByEnemy(self, detectionType, isObserved):
        ...
    def __onObservationDone(self):
        ...
    def __onVehicleEnterWorld(self, vProxy, vInfo, _):
        ...
    def __updateStatus(self):
        ...

class ArenaPeriodSoundPlayer(IAbstractPeriodView, IViewComponentsCtrlListener, IVehicleCountListener):
    __sessionProvider: Any
    __period: Any
    __winStatus: Any
    __isAlive: Any
    __lives: Any
    def __init__(self):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def setPeriod(self, period):
        ...
    def setAdditionalInfo(self, additionalInfo):
        ...
    def setPlayerVehicleAlive(self, isAlive):
        ...
    def setLives(self, lives):
        ...
    def __checkBattleEnd(self):
        ...

class PostmortemSoundPlayer(IVehicleCountListener):
    def setPlayerVehicleAlive(self, isAlive):
        ...

class ArenaTypeSoundPlayer(object):
    def init(self):
        ...
    def destroy(self):
        ...

class SelectRespawnSoundPlayer(ISpawnListener, IAbstractPeriodView):
    __slots__: tuple
    __selectEndingSoonTime: Any
    def __init__(self):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def onSelectPoint(self, pointId):
        ...

class EquipmentSoundPlayer(IVehicleCountListener, IViewComponentsCtrlListener):
    __sessionProvider: Any
    __currentEquipment: Any
    def __init__(self):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def __onEquipmentUpdated(self, _, item):
        ...
    def setPlayerVehicleAlive(self, isAlive):
        ...

class BerserkerSoundPlayer(VehicleStateSoundPlayer, CallbackDelayer):
    __period: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def __updateEffect(self):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stopEffect(self):
        ...

class BomberHitSoundPlayer(BaseEfficiencySoundPlayer):
    __DAMAGE_TYPE: tuple
    def _onEfficiencyReceived(self, events):
        ...

class KamikazeSoundPlayer(BaseEfficiencySoundPlayer):
    __sessionProvider: Any
    __KAMIKAZE_VEH_NAME = 'germany:G00_Bomber_SH'
    def init(self):
        ...
    def destroy(self):
        ...
    def updateVehiclesStats(self, updated, arenaDP):
        ...
    def __onVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
    def __onVehicleEnterWorld(self, vProxy, vInfo, guiProps):
        ...

class MineFieldSoundPlayer(BaseEfficiencySoundPlayer):
    def _onEfficiencyReceived(self, events):
        ...

class _HealingRepairSoundPlayer(VehicleStateSoundPlayer):
    def _onVehicleStateUpdated(self, state, value):
        ...

class _DamagingSmokeAreaSoundPlayer(VehicleStateSoundPlayer):
    __effectIsWorking: Any
    _smokeEquipment: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stopEvent(self):
        ...
    def __isEquipmentWithDamage(self, equipmentId):
        ...

class ShotPassionSoundPlayer(EquipmentComponentSoundPlayer):
    __slots__: tuple
    __sessionProvider: Any
    __isActive: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onEquipmentComponentUpdated(self, _, vehicleID, equipmentInfo):
        ...
    def _getComponentName(self):
        ...
    def _getEquipmentName(self):
        ...
    def _stopSounds(self):
        ...
