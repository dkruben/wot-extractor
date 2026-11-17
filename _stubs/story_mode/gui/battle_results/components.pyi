# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_results/components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from gui.battle_results.components import base as base
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import getUserName as getUserName
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.configs.story_mode_missions import missionsSchema as missionsSchema
from story_mode.gui.shared.utils import getRewardList as getRewardList

class FinishResultItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class FinishReasonItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class MissionIdItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class IsForceOnboardingItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...

class VehicleNameItem(base.StatsItem):
    __slots__: tuple
    _storyModeCtrl: Any
    def _convert(self, value, reusable):
        ...

class VehicleBlock(base.StatsBlock):
    def setRecord(self, result, reusable):
        ...

class RewardsBlock(base.StatsBlock):
    __slots__: tuple
    _battlePass: Any
    def setRecord(self, result, reusable):
        ...

class ProgressionInfoItem(base.StatsItem):
    __slots__: tuple
    def _convert(self, value, reusable):
        ...
