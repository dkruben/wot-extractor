# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/vehicle_mechanics_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
_VEHICLE_MECHANICS_CATEGORY = 'Vehicle Mechanics'

# decorador original: @registerComponent
class VehicleMechanicSimpleActivationSounds(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Vehicle Mechanic Simple Activation Sounds'
    domain = CGF.Domain.Client
    soundTrigger: Any
    soundNotReady: Any

# decorador original: @registerComponent
class ConcentrationModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Concentration Mode Mechanic Effects'
    domain = CGF.Domain.Client
    soundTransitionReady: Any
    soundTransitionStart: Any
    soundTransitionBrake: Any
    soundTransitionStop: Any
    soundObservationActiveStart: Any
    soundObservationActiveStop: Any
    soundStateConcentration: Any
    soundStateConcentrationOn: Any
    soundStateConcentrationOff: Any

# decorador original: @registerComponent
class PowerModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Power Mode Mechanic Effects'
    domain = CGF.Domain.Client
    soundPowerModeActivation: Any
    soundPowerModeLoop: Any
    soundPowerModeStop: Any
    soundPowerModeDeactivation: Any
    soundPowerModeActivationNPC: Any
    soundPowerModeLoopNPC: Any
    soundPowerModeStopNPC: Any
    soundPowerModeDeactivationNPC: Any
    startNodesList: Any
    idleNodesList: Any
    endNodesList: Any

# decorador original: @registerComponent
class AccuracyStacksEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Accuracy Stacks Mechanic Effects'
    domain = CGF.Domain.Client
    soundGainStack: Any
    soundStacksLimitReached: Any
    soundWarningNotification: Any
    soundGainStacksStart: Any
    soundGainStacksStop: Any
    soundGainStacksPause: Any
    soundGainStacksResume: Any

# decorador original: @registerComponent
class AccuracyStacksRTPCComponent(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Accuracy stacks gaining RTPC'
    domain = CGF.Domain.Client
    RTPCName: Any
    controllerGO: Any
    progress: Any
    def __init__(self):
        ...

# decorador original: @registerComponent
class BattleFuryModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Battle Fury Mechanic Effects'
    domain = CGF.Domain.Client
    soundGainStack: Any
    soundStacksLimitReached: Any
    soundDropStack: Any
    soundRefreshStack: Any

# decorador original: @registerComponent
class SupportWeaponEffects(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Support Weapon Mechanic Effects'
    domain = CGF.Domain.Client
    delayedReloadMinTime: Any
    delayedReloadMaxTime: Any
    soundDelayedReload: Any
    soundDelayedReloadCancel: Any
    soundTransitionReady: Any
    soundTransitionStart: Any
    soundTransitionBreak: Any
    soundTransitionStop: Any
    soundGeneralUtilityStop: Any

# decorador original: @registerComponent
class OverheatStacksEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Overheat Stacks mechanic effects'
    domain = CGF.Domain.Client
    soundDelayTimerUp: Any
    soundDelayTimerDown: Any
    eventChargingOn: Any
    eventChargingOff: Any
    eventChargingSilentInterrupt: Any
    RTPCChargingProcess: Any
    soundChargeMax: Any

# decorador original: @registerComponent
class RechargeableNitroEffects(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Rechargeable Nitro Effects'
    domain = CGF.Domain.Client
    idle: Any
    start: Any
    end: Any
    endSwitch: Any
    startFail: Any
    nearEnd: Any
    soundNodes: Any
    rtpcHolder: Any
    soundActivePC: Any
    soundStopPC: Any
    soundActiveNPC: Any
    soundStopNPC: Any
    soundReady: Any
    soundDisable: Any
    soundDelayEnded: Any
    soundExhausted: Any
    eventRTPCStart: Any
    eventRTPCStop: Any

# decorador original: @registerComponent
class ChargeShotEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Charge Shot Mechanic Effects'
    domain = CGF.Domain.Client
    soundActivation: Any
    soundActivationDisabled: Any
    soundChargeStart: Any
    soundChargeLevel1: Any
    soundChargeLevel2: Any
    soundChargeLevelMax: Any
    soundShootLevel0: Any
    soundShootLevel1: Any
    soundShootLevel2: Any
    soundShootLevelMax: Any
    soundOverheat: Any
    soundMechanicStop: Any

# decorador original: @registerComponent
class TargetDesignatorEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Target Designator Mechanic Effects'
    domain = CGF.Domain.Client
    soundReadyState: Any
    soundActiveState: Any
    soundCooldownState: Any
    soundActivation: Any
    soundActivationDisabled: Any
    soundMechanicStop: Any

# decorador original: @registerComponent
class StanceDanceEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Stance Dance Mechanic Effects'
    domain = CGF.Domain.Client
    sound3DTurboActivatedPC: Any
    sound3DTurboDeactivatedPC: Any
    sound3DTurboActivatedNPC: Any
    sound3DTurboDeactivatedNPC: Any
    soundTurboFullEnergy: Any
    soundFightFullEnergy: Any
    soundTurboModeOn: Any
    soundFightModeOn: Any
    soundFightActivated: Any
    soundFightDeactivated: Any
    soundMechanicStopPC: Any
    soundMechanicStopNPC: Any
    soundActivation: Any
    soundActivationDisabled: Any
    soundSwitch: Any

# decorador original: @registerComponent
class StationaryReloadEffects(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Stationary Reload Mechanic Effects'
    domain = CGF.Domain.Client
    soundTurretMoveStart: Any
    soundTurretMoveEnd: Any
    soundTurretLoadStop: Any
    soundTurretStopUtility: Any
    soundTurretBrake: Any
    soundDelayStart: Any
    soundDelayStop: Any

# decorador original: @registerComponent
class OverheatGunEffects(object):
    category = 'OverheatGun'
    editorTitle = 'Overheat Gun Effects'
    domain = CGF.Domain.Client
    soundHeating: Any
    soundCooling: Any
    soundIdle: Any
    soundUtilityStop: Any
    soundOverheatWarning: Any
    soundOverheated: Any
    soundPreCooled: Any
    soundCooled: Any

# decorador original: @registerComponent
class HeatingZonesGunEffects(object):
    category = 'HeatingZonesGun'
    editorTitle = 'Heating Zones Gun State Effects'
    domain = CGF.Domain.Client
    soundHeatingOn: Any
    soundHeatingOff: Any
    soundHeatingDropMarker: Any
    soundHeatingIdleMarker: Any
    soundUtilityStop: Any

# decorador original: @registerComponent
class PropellantGunEffects(object):
    category = 'PropellantGun'
    editorTitle = 'Propellant Gun Effects'
    domain = CGF.Domain.Client
    soundActivationDisabled: Any
    soundChargeMin: Any
    soundChargeMax: Any
    soundPreCharge: Any
    soundPreOvercharge: Any
    soundReachCharge: Any
    soundReachOvercharge: Any
    soundStartOvercharge: Any
    soundShotFromMinCharge: Any
    soundShotExitOvercharge: Any
    soundShotNocharge: Any
    soundDropOvercharge: Any
    soundUtilityStop: Any

# decorador original: @registerComponent
class ShellParamsSwitcherGunEffects(object):
    category = 'ShellParamsSwitcherGun'
    editorTitle = 'Shell Params Switcher Gun Effects'
    domain = CGF.Domain.Client
    soundActivationDisabled: Any
    soundTriggered: Any
    soundCharge2Noncharge: Any
    soundNoncharge2Charge: Any
    soundFinish: Any
    soundBroken: Any
    soundUtilityStop: Any

# decorador original: @registerComponent
class ShellCalibrationEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    domain = CGF.Domain.Client
    editorTitle = 'Shell Calibration Mechanic Effects'
    soundShellCalibrationPenetrationActivation: Any
    soundShellCalibrationDamageActivation: Any

# decorador original: @registerComponent
class AutoreloaderSurgeEffects(object):
    editorTitle = 'Autoreloader Surge Effects'
    category = 'AutoreloaderSurge'
    domain = CGF.Domain.Client
    soundActivationStart: Any
    soundChargeAlmostReady: Any

# decorador original: @registerComponent
class BustleFeedEffects(object):
    editorTitle = 'Bustle Feed Effects'
    category = _VEHICLE_MECHANICS_CATEGORY
    domain = CGF.Domain.Client
    soundActivation: Any
    soundActive: Any
    soundDeactivation: Any
    soundInactive: Any
    soundNotReady: Any
    soundStopUtility: Any

# decorador original: @registerComponent
class SightPointerEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Sight Pointer Effects'
    domain = CGF.Domain.Client
    soundReady: Any
    soundActivateButton: Any
    soundActivationFail: Any
    soundActivate: Any
    soundConeOn: Any
    soundRTPCStage: Any
    soundConeOff: Any
    soundEnemyEnterSector: Any
    soundEnemyLeftSector: Any
    soundStop: Any

# decorador original: @registerComponent
class CombatThrottleEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = 'Combat Throttle Effects'
    domain = CGF.Domain.Client
    soundTransitionReady: Any
    soundTransitionBlocked: Any
    soundActivation: Any
    soundActivationDisabled: Any
    soundActivationPC: Any
    soundDeactivationPC: Any
    soundActivationNPC: Any
    soundDeactivationNPC: Any
