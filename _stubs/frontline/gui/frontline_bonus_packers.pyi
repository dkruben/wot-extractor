# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/frontline_bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from epic_constants import FRONTLINE_BONUSES_ORDER as FRONTLINE_BONUSES_ORDER, EPIC_SKILL_TOKEN_NAME as EPIC_SKILL_TOKEN_NAME, EPIC_SELECT_BONUS_NAME as EPIC_SELECT_BONUS_NAME
from frontline.gui.bonus import FrontlineSkillBonus as FrontlineSkillBonus
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel as FrontlineRewardModel, ClaimState as ClaimState
from gui.impl.backport import createTooltipData as createTooltipData, TooltipData as TooltipData
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap, SimpleBonusUIPacker as SimpleBonusUIPacker, BonusUIPacker as BonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, BattlePassPointsBonusPacker as BattlePassPointsBonusPacker, CustomizationBonusUIPacker as CustomizationBonusUIPacker
from gui.shared.money import Currency as Currency
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, EpicSelectTokensBonus as EpicSelectTokensBonus, GoodiesBonus as GoodiesBonus, CustomizationsBonus as CustomizationsBonus

class FrontlineCrystalBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, *args):
        ...
    @classmethod
    def getToolTip(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class FrontlineTokenBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, **kwargs):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...

class FrontlineBattlePassPointsBonusPacker(BattlePassPointsBonusPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class FrontlineGoodiesBonusPacker(GoodiesBonusUIPacker):
    @classmethod
    def _packIconBonusModel(cls, bonus, icon, count, label):
        ...

class FrontlineCrewBookBonusPacker(CrewBookBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, book, count):
        ...

class FrontlineAbilityTokenPacker(SimpleBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, *args):
        ...

class FrontlineCustomizationBonusPacker(CustomizationBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

def getFrontlineBonusPacker():
    ...
def _keySortOrder(bonus):
    ...
def packBonusModelAndTooltipData(bonuses, listVM, tooltipData=None):
    ...
