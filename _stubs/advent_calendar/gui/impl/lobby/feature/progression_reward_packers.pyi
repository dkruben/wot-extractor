# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/progression_reward_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING, List as List
from constants import LOOTBOX_TOKEN_PREFIX as LOOTBOX_TOKEN_PREFIX
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import first as first
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel as ProgressionRewardItemViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getHolidayOpsStartTime as getHolidayOpsStartTime, getProgressionRewardType as getProgressionRewardType
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
from gui.shared.formatters.date_time import getRegionalDateTime as getRegionalDateTime
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker, BonusUIPacker as BonusUIPacker
from helpers import dependency as dependency
from gui.server_events.bonuses import TmanTemplateTokensBonus as TmanTemplateTokensBonus, CustomizationsBonus as CustomizationsBonus, TokensBonus as TokensBonus, SimpleBonus as SimpleBonus
_logger: Any

class ProgressionBonusUIPacker(BonusUIPacker):
    def getCustomToolTip(self, bonus, questID):
        ...

class BaseProgressionRewardPacker(BaseBonusUIPacker):
    @classmethod
    def _createModel(cls, bonus):
        ...
    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        ...

class TmanTemplatePacker(BaseProgressionRewardPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class CustomizationPacker(BaseProgressionRewardPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        ...

class LootboxTokensPacker(BaseProgressionRewardPacker):
    _adventController: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def getCustomToolTip(cls, bonus, questID):
        ...
    @classmethod
    def packTooltipPayload(cls):
        ...

def getProgressionBonusMapping():
    ...
def getProgressionBonusPacker():
    ...
