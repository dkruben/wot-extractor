# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from advent_calendar.gui.impl.lobby.feature.progression_reward_packers import LootboxTokensPacker as LootboxTokensPacker
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker as BaseTmanTemplateBonusPacker
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel as RewardItemModel
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN
from gui.server_events.bonuses import C11nProgressTokenBonus as C11nProgressTokenBonus
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker, BonusUIPacker as BonusUIPacker
from gui.shared.missions.packers.bonus import CrewSkinBonusUIPacker as BaseCrewSkinBonusUIPacker
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as BaseCustomizationBonusUIPacker
from gui.shared.missions.packers.bonus import SimpleBonusUIPacker as SimpleBonusUIPacker
from gui.shared.missions.packers.bonus import TokenBonusUIPacker as BaseTokenBonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap
from helpers import dependency as dependency
from typing import List as List
from gui.shared.gui_items.customization.c11n_items import Style as Style
from gui.server_events.bonuses import LootBoxTokensBonus as LootBoxTokensBonus
from gui.server_events.bonuses import TokensBonus as TokensBonus

class TokenBonusUIPacker(BaseTokenBonusUIPacker):
    @classmethod
    def _packToken(cls, bonusPacker, bonus, *args):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...

class CrewSkinBonusUIPacker(BaseCrewSkinBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, crewSkin, count, label):
        ...

class CustomizationBonusUIPacker(BaseCustomizationBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class ProgressionCustomizationBonusUIPacker(BaseBonusUIPacker):
    _c11nService: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, level=None):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class TmanTemplateBonusPacker(BaseTmanTemplateBonusPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus):
        ...

class LootBoxPacker(SimpleBonusUIPacker):
    _itemsCache: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

def getRewardBonusMapping():
    ...
def getRewardBonusPacker():
    ...
