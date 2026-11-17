# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_results/components/comp7_core_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import EntityCaptured as EntityCaptured
from gui.battle_results.components import base as base, style as style
from gui.battle_results.components.vehicles import RegularVehicleStatValuesBlock as RegularVehicleStatValuesBlock, RegularVehicleStatsBlock as RegularVehicleStatsBlock, TeamStatsBlock as TeamStatsBlock, _getStunFilter as _getStunFilter
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R

class EfficiencyTitleWithSkills(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class IsDeserterFlag(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class Comp7CoreVehicleStatsBlock(RegularVehicleStatsBlock):
    __slots__: tuple
    prestigePoints: Any
    isSuperSquad: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class Comp7CoreTeamStatsBlock(TeamStatsBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class Comp7CoreVehicleStatValuesBlock(RegularVehicleStatValuesBlock):
    __slots__: tuple
    damageDealtBySkills: Any
    healed: Any
    capturedPointsOfInterest: Any
    roleSkillUsed: Any
    def setRecord(self, result, reusable):
        ...

class AllComp7CoreVehicleStatValuesBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class PersonalVehiclesComp7CoreStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

def checkIfDeserter(reusable, fairplayViolation):
    ...
