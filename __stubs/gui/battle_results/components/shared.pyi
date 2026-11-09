# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE as ACHIEVEMENT_TYPE
from gui.battle_results import stored_sorting as stored_sorting
from gui.battle_results.components import base as base
from gui.battle_results.components.style import makeTeamKillerText as makeTeamKillerText
from gui.battle_results.pbs_helpers.common import getAchievementCustomData as getAchievementCustomData, getVehicleLevel as getVehicleLevel
from gui.shared.gui_items.dossier.achievements import MarkOnGunAchievement as MarkOnGunAchievement

class TrueFlag(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class FalseFlag(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class ClientIndexItem(base.StatsItem):
    def _convert(self, value, reusable):
        ...

class PlayerNameBlock(base.StatsBlock):
    __slots__: tuple
    _dbID: Any
    realNameLabel: Any
    fullNameLabel: Any
    isTeamKiller: Any
    fakeNameLabel: Any
    clanLabel: Any
    regionLabel: Any
    tags: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setTeamKillerInfo(self):
        ...
    def setPlayerInfo(self, playerInfo):
        ...
    def setRecord(self, result, reusable):
        ...

class WasInBattleItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class WasInEpicBattleItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class SortingBlock(base.StatsBlock):
    __slots__: tuple
    criteria: Any
    direction: Any
    __setting: Any
    def __init__(self, setting, meta=None, field='', *path):
        ...
    @property
    def settingKey(self):
        ...
    def getVO(self):
        ...
    def setRecord(self, result, reusable):
        ...

class RegularSortingBlock(SortingBlock):
    __slots__: tuple
    def __init__(self, meta=None, field='', *path):
        ...

class AchievementIcon(base.StatsBlock):
    __slots__: tuple
    small: Any
    big: Any
    def __init__(self, meta=None, field='', *path):
        ...
    def setRecord(self, result, reusable):
        ...

class AchievementBlock(base.StatsBlock):
    __slots__: tuple
    isUnique: Any
    type: Any
    block: Any
    icon: Any
    specialIcon: Any
    title: Any
    description: Any
    hasRibbon: Any
    customData: Any
    rank: Any
    i18nValue: Any
    arenaType: Any
    vehicleLevel: Any
    def setUnique(self, value):
        ...
    def setRecord(self, result, reusable):
        ...

class AchievementsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, record, reusable):
        ...

class BiDiStatsBlock(base.StatsBlock):
    __slots__: tuple
    @property
    def left(self):
        ...
    @property
    def right(self):
        ...
