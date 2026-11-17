# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/common/comp7_core_common/items/comp7_core_artefacts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from items.artefacts import BaseMarkerConfigReader as BaseMarkerConfigReader, EffectsConfigReader as EffectsConfigReader, LevelBasedVisualScriptEquipment as LevelBasedVisualScriptEquipment, PointVisualScriptEquipment as PointVisualScriptEquipment, VisualScriptEquipment as VisualScriptEquipment

class Comp7CoreAoeHealEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    radius: Any
    heal: Any
    secondaryHealDebuff: Any
    tickInterval: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreAllySupportEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    crewBuff: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreAllyHunterEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    heal: Any
    gunReloadTimeBuff: Any
    tickInterval: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreConcentrationEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    aimingTimeBuff: Any
    shotDispersionFactors: Any
    clipReloadTimeBoost: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreBerserkEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    gunReloadTimeBuff: Any
    damageDistance: Any
    cooldownSeconds: Any
    shotDispersionFactors: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreAoeInspireEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    crewBuff: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreRedlineEquipment(PointVisualScriptEquipment, LevelBasedVisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    _CONFIG_SLOTS: Any
    delay: Any
    cooldownSeconds: Any
    damage: Any
    stunDuration: Any
    areaShow: Any
    duration: Any
    fraction: Any
    requireAssists: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreFastRechargeEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    gunReloadTimeBuff: Any
    gunTemperatureBuff: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreJuggernautEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    enginePowerFactor: Any
    cooldownSeconds: Any
    dmgAbsorb: Any
    fwMaxSpeedBonus: Any
    bkMaxSpeedBonus: Any
    rammingDamageBonus: Any
    vehicleRotationSpeedFactor: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreSureShotEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    shotDispersionFactors: Any
    slvl: Any
    sdlvl: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreSniperEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    dispersionFactor: Any
    damageDistance: Any
    cooldownSeconds: Any
    damageFactors: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreRiskyAttackEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    healDuration: Any
    baseHeal: Any
    extraHealFactor: Any
    fwdSpeedBoost: Any
    bkwSpeedBoost: Any
    enginePowerBuff: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreReconEquipment(PointVisualScriptEquipment, LevelBasedVisualScriptEquipment, BaseMarkerConfigReader):
    _CONFIG_SLOTS: Any
    duration: Any
    delay: Any
    startupDelay: Any
    cooldownSeconds: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreAggressiveDetectionEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    visionFactor: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Comp7CoreMarchEquipment(VisualScriptEquipment):
    _CONFIG_SLOTS: tuple
    duration: Any
    enginePowerBuff: Any
    fwdSpeedBoost: Any
    invisibilityFactor: Any
    cooldownSeconds: Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...
