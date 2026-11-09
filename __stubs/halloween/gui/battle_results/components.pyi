# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_results/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.battle_results.components import base as base, common as common
from halloween_common.halloween_constants import INVALID_BATTLE_PLACE as INVALID_BATTLE_PLACE

class HwPhaseItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class HwPhasesCountItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class HwEffectivenessArtefactKeysItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class HwBossArtefactKeysItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class HwHangarLoot(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class PersonalFirstTeamItemSortKey(sort_keys.TeamItemSortKey):
    __slots__: tuple
    _sortKey: Any
    def __init__(self, vehicleInfo, compareKey):
        ...
    def _cmp(self, other):
        ...

class HWAfkSortKey(sort_keys.TeamItemSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...
    @staticmethod
    def _isAfk(info):
        ...

class HWVehicleStatsBlock(base.StatsBlock):
    __slots__: tuple
    playerDBID: Any
    playerName: Any
    vehicleName: Any
    vehicleType: Any
    vehicleCD: Any
    vehicleLvl: Any
    clanAbbrev: Any
    artefactKeys: Any
    killerName: Any
    deathReason: Any
    kills: Any
    damageDealt: Any
    isPlayer: Any
    squadID: Any
    isOwnSquad: Any
    badgeID: Any
    badgeSuffixID: Any
    hwVehiclesRespawnCount: Any
    hasPenalties: Any
    hwBossFightDamage: Any
    hwHangarLoot: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class HWBattlesTeamStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class HWBattleFinishResultBlock(common.RegularFinishResultBlock):
    shortResultLabel: Any
    fullResultLabel: Any
    finishReasonLabel: Any
    finishReasonClarificationLabel: Any
    def setRecord(self, result, reusable):
        ...
