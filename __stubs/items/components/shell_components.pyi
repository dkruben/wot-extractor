# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/shell_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SHELL_TYPES as SHELL_TYPES, DamageAbsorptionTypeToLabel as DamageAbsorptionTypeToLabel, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE
from items.components.component_constants import DEFAULT_ENABLE_TRACE_RICOCHET as DEFAULT_ENABLE_TRACE_RICOCHET, ZERO_FLOAT as ZERO_FLOAT, ZERO_TUPLE2 as ZERO_TUPLE2
from typing import Set as Set, Optional as Optional, Tuple as Tuple, Union as Union

class ShellType(object):
    __slots__: tuple
    name: Any
    def __init__(self, name):
        ...
    def __repr__(self):
        ...

class ArmorPiercingType(ShellType):
    __slots__: tuple
    normalizationAngle: Any
    ricochetAngleCos: Any
    enableTraceRicochet: Any
    protectFromDirectHits: Any
    mechanics: Any
    nonPiercingArmorDamage: Any
    def __init__(self, name):
        ...
    def __repr__(self):
        ...

class HollowChargeType(ShellType):
    __slots__: tuple
    piercingPowerLossFactorByDistance: Any
    ricochetAngleCos: Any
    enableTraceRicochet: Any
    protectFromDirectHits: Any
    mechanics: Any
    nonPiercingArmorDamage: Any
    def __init__(self, name):
        ...
    def __repr__(self):
        ...

class HighExplosiveImpactParams(object):
    __slots__: tuple
    radius: Any
    armorDamage: Any
    deviceDamage: Any
    coneAngleCos: Any
    piercingSpalls: Any
    damageAbsorptionType: Any
    hasSplash: Any
    isActive: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...

class HighExplosiveType(ShellType):
    __slots__: tuple
    explosionRadius: Any
    explosionDamageFactor: Any
    explosionDamageAbsorptionFactor: Any
    explosionEdgeDamageFactor: Any
    shellFragmentsDamageAbsorptionFactor: Any
    mechanics: Any
    obstaclePenetration: Any
    shieldPenetration: Any
    blastWave: Any
    shellFragments: Any
    armorSpalls: Any
    protectFromDirectHits: Any
    protectFromIndirectHits: Any
    maxDamage: Any
    def __init__(self, name):
        ...
    def __repr__(self):
        ...
    @property
    def impacts(self):
        ...

class SmokeType(ShellType):
    __slots__: tuple
    def __init__(self, name):
        ...
    def __repr__(self):
        ...

class Stun(object):
    __slots__: tuple
    stunRadius: Any
    stunDuration: Any
    stunFactor: Any
    guaranteedStunDuration: Any
    damageDurationCoeff: Any
    guaranteedStunEffect: Any
    damageEffectCoeff: Any
    def __init__(self, stunRadius=..., stunDuration=..., stunFactor=..., guaranteedStunDuration=..., damageDurationCoeff=..., guaranteedStunEffect=..., damageEffectCoeff=...):
        ...
    def __repr__(self):
        ...

def createShellType(typeName):
    ...
