# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_results/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from ArenaType import parseTypeID as parseTypeID
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.battle_results.components import base as base, common as common
from last_stand_common.last_stand_constants import INVALID_BATTLE_PLACE as INVALID_BATTLE_PLACE

class LSTimeItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class LSPrevBestMissionsCountItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class LSCompletedDifficultyMissions(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class LSPhaseItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class LSPhasesCountItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class LSEffectivenessPointsItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class LSObeliskPointsItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class LSGeometryIdItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class PersonalFirstTeamItemSortKey(sort_keys.TeamItemSortKey):
    __slots__: tuple
    _sortKey: Any
    def __init__(self, vehicleInfo, compareKey):
        ...
    def _cmp(self, other):
        ...

class LSAfkSortKey(sort_keys.TeamItemSortKey):
    __slots__: tuple
    def _cmp(self, other):
        ...
    @staticmethod
    def _isAfk(info):
        ...

class LSVehicleStatsBlock(base.StatsBlock):
    __slots__: tuple
    playerDBID: Any
    playerName: Any
    vehicleName: Any
    vehicleShortName: Any
    vehicleType: Any
    vehicleCD: Any
    vehicleLvl: Any
    clanAbbrev: Any
    progressPoints: Any
    killerName: Any
    deathReason: Any
    kills: Any
    damageDealt: Any
    isPlayer: Any
    squadID: Any
    isOwnSquad: Any
    badgeID: Any
    badgeSuffixID: Any
    respawnsCount: Any
    hasPenalties: Any
    vehicleIsIGR: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class LSBattlesTeamStatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class LSBattleFinishResultBlock(common.RegularFinishResultBlock):
    shortResultLabel: Any
    fullResultLabel: Any
    finishReasonLabel: Any
    finishReasonClarificationLabel: Any
    def setRecord(self, result, reusable):
        ...
