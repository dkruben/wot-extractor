# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/cgf_client_module.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import CameraComponents as CameraComponents
import Vehicular as Vehicular
import cgf_components.vehicle_mechanics_components
import GenericComponents as GenericComponents
import CgfStateMachine as CgfStateMachine
import GpuDecals as GpuDecals
from CustomEffectManager import CustomEffectManager as CustomEffectManager, CustomEffectManagerSystem as CustomEffectManagerSystem
from DestructibleEntityState import DestructibleEntityStatesSystem as DestructibleEntityStatesSystem
from DetachedTurret import DetachedTurretSystem as DetachedTurretSystem
from cgf_components.audition_component_2d import AuditionsSystem as AuditionsSystem
from cgf_components.mechanic_components.cyclic_rocket.accelerator_status_tracker import AcceleratorStatusTrackerComponentSystem as AcceleratorStatusTrackerComponentSystem, AcceleratorStatusTrackerComponent as AcceleratorStatusTrackerComponent
from cgf_components.mechanic_components.cyclic_rocket.nozzle_controller import NozzleController as NozzleController, NozzleActivationSyncComponent as NozzleActivationSyncComponent, NozzleControllerComponentSystem as NozzleControllerComponentSystem
from cgf_components.mechanic_components.cyclic_rocket.staged_jet_boosters import StagedJetBoostersComponentSystem as StagedJetBoostersComponentSystem
from cgf_components.mechanic_components.bustle_feed import BustleFeedVariableStorageCachingSystem as BustleFeedVariableStorageCachingSystem
from constants import IS_EDITOR as IS_EDITOR, IS_CGF_DUMP as IS_CGF_DUMP
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from cgf_components.client_worlds_helpers import clientWorldsPredicate as clientWorldsPredicate, ClientWorld as ClientWorld
from cgf_components.temperature_gun_rtpc_component import TemperatureGunMechanicSystem as TemperatureGunMechanicSystem
from constants import HAS_DEV_RESOURCES as HAS_DEV_RESOURCES, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from cgf_script.registration import bonusCapsPredicate as bonusCapsPredicate, registerModule as registerModule
from cgf_components.accuracy_stacks_manager import AccuracyStacksMechanicSystem as AccuracyStacksMechanicSystem
from cgf_components.arena_camera_manager import ArenaCameraSystem as ArenaCameraSystem
from cgf_components.armor_inspector_component import ArmorInspectorComponent as ArmorInspectorComponent, ArmorInspectorSystem as ArmorInspectorSystem
from cgf_components.attack_artillery_fort_components import ArtilleryFortColorComponent as ArtilleryFortColorComponent, AttackArtilleryFortColorSystem as AttackArtilleryFortColorSystem
from cgf_components.color_components import ColorComponent as ColorComponent, ColorSystem as ColorSystem
from cgf_components.color_blind_component import ChangeModelOnColorBlindComponent as ChangeModelOnColorBlindComponent, ChangeModelOnColorBlindComponentSystem as ChangeModelOnColorBlindComponentSystem
from cgf_components.gun_audition_component import GunAuditionsSystem as GunAuditionsSystem
from cgf_components.hangar_camera_manager import HangarCameraSystem as HangarCameraSystem
from cgf_components.highlight_component import HighlightComponent as HighlightComponent, HighlightSystem as HighlightSystem, IsHighlighted as IsHighlighted
from cgf_components.hover_component import HoverSystem as HoverSystem, IsHoveredComponent as IsHoveredComponent, SelectionComponent as SelectionComponent, HoverGroupTrackerComponent as HoverGroupTrackerComponent
from cgf_components.hover_group_components import HoverGroupSystem as HoverGroupSystem, HoverableComponent as HoverableComponent, HoverSoundComponent as HoverSoundComponent
from cgf_components.marker_component import CombatMarker as CombatMarker, CombatMarkerSystem as CombatMarkerSystem, GFMarkersCreatorSystem as GFMarkersCreatorSystem, LobbyFlashMarker as LobbyFlashMarker, LobbyFlashMarkerVisibility as LobbyFlashMarkerVisibility, LobbyMarkersSystem as LobbyMarkersSystem, LobbyMarkersVisibilitySystem as LobbyMarkersVisibilitySystem
from cgf_components.on_click_components import ClickSystem as ClickSystem, ClickVSEComponentsSystem as ClickVSEComponentsSystem, ClientSelectableComponentsSystem as ClientSelectableComponentsSystem, OpenBrowserOnClickComponent as OpenBrowserOnClickComponent
from cgf_components.on_death_components import ChangeModelOnDeathComponent as ChangeModelOnDeathComponent, EffectOnDeathComponent as EffectOnDeathComponent, SoundOnDeathComponent as SoundOnDeathComponent
from cgf_components.on_player_in_zone_manager import OnPlayerInZoneSystem as OnPlayerInZoneSystem
from cgf_components.on_shot_components import EffectOnShotComponent as EffectOnShotComponent, SoundOnShotComponent as SoundOnShotComponent
from cgf_components.pbs_components import PostBattleBoardComponent as PostBattleBoardComponent, PostBattleSystem as PostBattleSystem
from cgf_components.pm30_hangar_components import AssemblingStagesComponent as AssemblingStagesComponent, HangarOperationsComponent as HangarOperationsComponent, HangarOperationsSystem as HangarOperationsSystem, PersonalMissionsSelectionComponent as PersonalMissionsSelectionComponent
from cgf_components.power_mode_components import PowerModeActiveProgressLayers as PowerModeActiveProgressLayers, PowerModeMechanicSystem as PowerModeMechanicSystem, PowerModeRTPCComponent as PowerModeRTPCComponent
from cgf_components.rechargeable_nitro_components import RechargeableNitroMechanicSystem as RechargeableNitroMechanicSystem, RechargeableNitroRTPCComponent as RechargeableNitroRTPCComponent
from cgf_components.rocket_acceleration_component import RocketAccelerationStateListener as RocketAccelerationStateListener, RocketAccelerationSystem as RocketAccelerationSystem, RocketAccelerationTerrainEffect as RocketAccelerationTerrainEffect
from cgf_components.rtpc_component_manager import RTPCComponentSystem as RTPCComponentSystem
from cgf_components.sequence_components import PrefabSpawnerSystem as PrefabSpawnerSystem
from cgf_components.serial_number_component import SerialNumberComponent as SerialNumberComponent, SerialNumberComponentSystem as SerialNumberComponentSystem, SerialNumberSwitcher as SerialNumberSwitcher
from cgf_components.shot_color_transmission_component import ShotColorTransmissionComponent as ShotColorTransmissionComponent
from cgf_components.stats_display_components import StatisticDisplayComponent as StatisticDisplayComponent, TrackedStatisticComponentSystem as TrackedStatisticComponentSystem
from cgf_components.target_designator_manager import TargetDesignatorSoundSystem as TargetDesignatorSoundSystem
from cgf_components.trigger_vse_component import TriggerVSEComponent as TriggerVSEComponent, TriggerVisualScriptComponentsSystem as TriggerVisualScriptComponentsSystem
from cgf_components.vehicle_components.avatar_attached_vehicle_watcher import AvatarAttachedVehicleWatcherComponent as AvatarAttachedVehicleWatcherComponent, AvatarAttachedVehicleWatcherSystem as AvatarAttachedVehicleWatcherSystem
from cgf_components.vehicle_components.nitro import VehicleNitroExhaustEffectComponent as VehicleNitroExhaustEffectComponent, VehicleNitroExhaustEffectComponentSystem as VehicleNitroExhaustEffectComponentSystem
from cgf_components.vehicle_health_observer_manager import VehicleHealthObserverSystem as VehicleHealthObserverSystem
from cgf_components.visual_effect_component_manager import KillCamVisualEffectComponentSystem as KillCamVisualEffectComponentSystem
from cgf_components.zone_components import MapZoneSystem as MapZoneSystem, RandomEventZoneUINotification as RandomEventZoneUINotification, WeatherZoneUINotification as WeatherZoneUINotification, ZoneHint as ZoneHint, ZoneMarker as ZoneMarker
from cgf_components.crest_moving_effects_component import CrestMovingEffectsComponent as CrestMovingEffectsComponent
from gui.pet_system.cgf_components.pet_place_component import PetPlaceComponent as PetPlaceComponent, PetPrefabSystem as PetPrefabSystem
from vehicle_systems.components.vehicle_to_camera_alignment_components import VehicleToCameraAlignmentSystem as VehicleToCameraAlignmentSystem, VehicleToCameraAlignmentComponent as VehicleToCameraAlignmentComponent
from DeathComponent import DeathComponentSystem as DeathComponentSystem
from SequenceNetworkSync import SequenceNetworkSyncSystem as SequenceNetworkSyncSystem
from StateMachineNetworkSync import StateMachineNetworkSyncSystem as StateMachineNetworkSyncSystem
from ShotsReceiver import ShotReceiverSystem as ShotReceiverSystem, ShotsReceiver as ShotsReceiver
from VehicleStickers import VehicleStickersSystem as VehicleStickersSystem
from vehicle_systems.components.hull_aiming_controller import HullAimingSystem as HullAimingSystem, HullAimingController as HullAimingController
from vehicle_systems.components.CrashedTracks import CrashedTracksController as CrashedTracksController, CrashedTracksSystem as CrashedTracksSystem
from vehicle_systems.components.highlighter import Highlighter as Highlighter, HighlighterSystem as HighlighterSystem
from vehicle_systems.components.vehicle_shadow_manager import VehicleShadowManager as VehicleShadowManager, VehicleShadowSystem as VehicleShadowSystem
from vehicle_systems.components.siegeEffectsController import SiegeEffectsController as SiegeEffectsController
from vehicle_appearance.component import VehicleAppearanceComponent as VehicleAppearanceComponent
from vehicle_appearance.systems import CommonTankAppearanceActivateSystem as CommonTankAppearanceActivateSystem, CommonTankAppearanceUpdateSystem as CommonTankAppearanceUpdateSystem, CompoundAppearanceDirtUpdateSystem as CompoundAppearanceDirtUpdateSystem
from cgf_components.rocket_acceleration_component import RocketAccelerationSystemDebug as RocketAccelerationSystemDebug

class HangarAppearanceSystem(object):
    Reactions: Any

class CrestMovingEffectsSystem(object):
    Reactions: Any

# decorador original: @registerModule
class ClientCommonModule(object):
    name = 'Client Module'
    desc = 'Client Common Functionalities'
    group = 'Common'
    systems: list
    components: list

# decorador original: @registerModule
class ClientKillCamModule(object):
    name = 'Kill Cam Client Module'
    desc = 'Client side for killcam support'
    group = 'Common'
    systems: list
    components: list

# decorador original: @registerModule
class ClientArmorInspectorModule(object):
    name = 'Armor Inspector Client Module'
    group = 'Armor Inspector'
    systems: list
    components: list

# decorador original: @registerModule
class ClientUiModule(object):
    name = 'UI Client Module'
    group = 'UI'
    systems: list
    components: list

# decorador original: @registerModule
class ClientAbilitiesModule(object):
    name = 'Abilities Client Module'
    group = 'Abilities'
    systems: list
    components: list

# decorador original: @registerModule
class HangarSelectionModule(object):
    name = 'Hangar Selection Client Module'
    group = 'Hangar rules'
    systems: list
    components: list

# decorador original: @registerModule
class HangarCameraModule(object):
    name = 'Hangar Camera Client Module'
    group = 'Hangar rules'
    systems: list

# decorador original: @registerModule
class VehicleToCameraAlignmentModule(object):
    name = 'Vehicle To Camera Alignment Module'
    group = 'Hangar rules'
    systems: list
    components: list

# decorador original: @registerModule
class PostBattleModule(object):
    name = 'Post Battle Client Module'
    group = 'Hangar rules'
    systems: list
    components: list

# decorador original: @registerModule
class HangarOperationsModule(object):
    name = 'Hangar Operations Client Module'
    group = 'Hangar rules'
    systems: list
    components: list

# decorador original: @registerModule
class LobbyModule(object):
    name = 'Lobby Client Module'
    group = 'lobby'
    systems: list
    components: list

# decorador original: @registerModule
class PetModule(object):
    group = 'Hangar rules'
    name = 'Pet Placement Module'
    systems: list
    components: list

# decorador original: @registerModule
class VehicleAppearanceModule(object):
    name = 'Vehicle Appearance Module'
    group = 'Vehicle'
    systems: list
    components: list

# decorador original: @registerModule
class ClientVehicleAbilitiesModule(object):
    name = 'Client Vehicle Abilities Module'
    desc = 'Client vehicle abilities mechanics'
    group = 'Vehicle abilities'
    systems: list
    components: list

# decorador original: @registerModule
class RamDebugModule(object):
    name = 'Rocker Acceleration Debug Module'
    desc = 'Debug RAM in battles'
    group = 'Debug'
    systems: list
    components: list
