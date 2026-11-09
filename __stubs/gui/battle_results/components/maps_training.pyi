# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/components/maps_training.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from ArenaType import parseTypeID as parseTypeID
from gui.battle_results.components import base as base
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from helpers import dependency as dependency
from maps_training_common.helpers import getMapsTrainingAwards as getMapsTrainingAwards
from maps_training_common.maps_training_constants import MAX_SCENARIO_PROGRESS as MAX_SCENARIO_PROGRESS
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
_logger: Any
_IMAGES_FOLDER_PATH = '../maps/icons/maps_training/battle_result/'
_BG_FOLDER_PATH: Any
_BG_IMAGE_FORMAT = '{team_result}.png'
_STAT_ICON_PATH: Any
_STAT_ICON_TOOLTIP_PATH: Any
_STAT_FIELD_NAMES: tuple
BATTLE_STATS_KILLS = 'kills'
BATTLE_STATS_RESULT_FIELDS: dict
BATTLE_STATS_ICONS: dict

class BattleGoalsBlock(base.StatsBlock):
    def setRecord(self, result, reusable):
        ...

class BattleDurationItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, result, reusable):
        ...

class StatsBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class GeometryIdItem(base.StatsItem):
    def _convert(self, result, reusable):
        ...

class TeamItem(base.StatsItem):
    def _convert(self, result, reusable):
        ...

class VehicleBlock(base.StatsBlock):
    def setRecord(self, result, reusable):
        ...

class MTProgressMixin(object):
    mapsTrainingController: Any
    def _getScenarioData(self, result, reusable):
        ...

class DoneValueItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, result, reusable):
        ...

class ScenarioProgressBlock(base.StatsBlock, MTProgressMixin):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class RewardsBlock(base.StatsBlock, MTProgressMixin):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class AccountProgressBlock(base.StatsBlock):
    __slots__: tuple
    def setRecord(self, result, reusable):
        ...

class WasDoneItem(base.StatsItem, MTProgressMixin):
    def _convert(self, result, reusable):
        ...
