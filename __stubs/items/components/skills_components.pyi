# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/skills_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from items.components import legacy_stuff as legacy_stuff
from items.components import skills_constants as skills_constants
from items.components.perks_constants import StubPerkIDs as StubPerkIDs
from items.components.skills_constants import SkillTypeName as SkillTypeName

class BasicSkill(legacy_stuff.LegacyStuff):
    __slots__: tuple
    __name: Any
    __vsePerk: Any
    __uiSettings: Any
    def __init__(self, name, vsePerk=None, uiSettings=None):
        ...
    def __repr__(self):
        ...
    @property
    def name(self):
        ...
    @property
    def vsePerk(self):
        ...
    @property
    def kpi(self):
        ...
    @property
    def tooltipSection(self):
        ...
    def recreate(self, *args):
        ...
    @property
    def uiSettings(self):
        ...
    @property
    def situational(self):
        ...
    @property
    def typeName(self):
        ...
    @property
    def params(self):
        ...

class ExtendedSkill(BasicSkill):
    __slots__: tuple
    _setOfParameters: Any
    def __init__(self, basicSkill, *args):
        ...
    def recreate(self, *args):
        ...

class BrotherhoodSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def crewLevelIncrease(self):
        ...

class CommanderTutorSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def xpBonusFactorPerLevel(self):
        ...
    @property
    def efficiency(self):
        ...

class CommanderSkillWithDelay(ExtendedSkill):
    __slots__: tuple
    @property
    def delay(self):
        ...

class CommanderEnemyShotPredictor(ExtendedSkill):
    __slots__: tuple
    @property
    def minExplosionRadius(self):
        ...
    @property
    def explosionMultiplier(self):
        ...
    @property
    def recalculatingHeight(self):
        ...
    @property
    def targetRadius(self):
        ...

class CommonSkill(ExtendedSkill):
    __slots__: tuple

class DriverSmoothDrivingSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def shotDispersionFactorPerLevel(self):
        ...

class GunnerArmorerSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def shotDispersionFactorPerLevel(self):
        ...

class GunnerSniperSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def deviceChanceToHitBoost(self):
        ...

class RadiomanLastEffortSkill(ExtendedSkill):
    __slots__: tuple
    @property
    def durationPerLevel(self):
        ...
    @property
    def chanceToHitPerLevel(self):
        ...

class CrewMasterySkill(ExtendedSkill):
    __slots__: tuple
    @property
    def crewLevelIncrease(self):
        ...

class SkillsConfig(legacy_stuff.LegacyStuff):
    __slots__: Any
    vsePerkToSkill: Any
    def __init__(self):
        ...
    @staticmethod
    def getNumberOfActiveSkills():
        ...
    def addSkill(self, name, skill):
        ...
    def getSkill(self, name):
        ...
