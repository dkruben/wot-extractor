# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN as BATTLE_BONUS_X5_TOKEN, AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, ItemsBonus as ItemsBonus, TokensBonus as TokensBonus, CrewBooksBonus as CrewBooksBonus, CustomizationsBonus as CustomizationsBonus, BlueprintsBonusSubtypes as BlueprintsBonusSubtypes, TmanTemplateTokensBonus as TmanTemplateTokensBonus
from gui.server_events.finders import isPMPoints as isPMPoints, PM_POINTS_TOKEN as PM_POINTS_TOKEN
from gui.server_events.formatters import parseComplexToken as parseComplexToken
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, getItemTypeID as getItemTypeID
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as CustomizationBonusUIPacker, getLocalizedBonusName as getLocalizedBonusName, DossierBonusUIPacker as DossierBonusUIPacker, DOSSIER_BADGE_ICON_PREFIX as DOSSIER_BADGE_ICON_PREFIX, DOSSIER_BADGE_POSTFIX as DOSSIER_BADGE_POSTFIX, ItemBonusUIPacker as ItemBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, CrewBookBonusUIPacker as CrewBookBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap, BonusUIPacker as BonusUIPacker, SimpleBonusUIPacker as SimpleBonusUIPacker, BlueprintBonusUIPacker as BlueprintBonusUIPacker, GoodiesBonusUIPacker as GoodiesBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from items.components.c11n_constants import Rarity as Rarity
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from personal_missions import PM_BRANCH as PM_BRANCH, PM_BRANCH_TO_FREE_TOKEN_NAME as PM_BRANCH_TO_FREE_TOKEN_NAME
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.style_bonus_model import StyleBonusModel as StyleBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.tooltips.umg_reward_model import UmgRewardModel as UmgRewardModel
from frameworks.wulf.view.array import Array as Array
from typing import List as List, Dict as Dict
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
_logger: Any
REWARDS_ORDER: tuple
LAST_ORDER: Any

class PM3GoodiesBonusUIPacker(GoodiesBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...

class PM3BlueprintBonusUIPacker(BlueprintBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getNationalLabel(cls, bonus):
        ...
    @classmethod
    def _blueprintsChecker(cls, bonus):
        ...

class PM3PremiumPacker(SimpleBonusUIPacker):
    __PREMIUM_YEAR = 360
    @classmethod
    def _pack(cls, bonus):
        ...

class PM3DashboardCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    __c11n: Any
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...
    @classmethod
    def _customizationsChecker(cls, item):
        ...
    @classmethod
    def _getToolTipData(cls, itemCustomization):
        ...

class PM3CustomizationBonusUIPacker(PM3DashboardCustomizationBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class PM3DossierBonusUIPacker(DossierBonusUIPacker):
    @classmethod
    def _packAchievements(cls, bonus):
        ...
    @classmethod
    def _packBadges(cls, bonus):
        ...
    @staticmethod
    def _dossierChecker(badge):
        ...

class PM3ItemBonusUIPacker(ItemBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @staticmethod
    def _itemsChecker(item):
        ...

class PM3TokenBonusUIPacker(TokenBonusUIPacker):
    __isOperationCompleted = False
    @classmethod
    def setIsOperationCompleted(cls, isOperationCompleted):
        ...
    @classmethod
    def _pack(cls, bonus):
        ...
    @staticmethod
    def _tokensChecker(token):
        ...

class PM3CrewBookBonusUIPacker(CrewBookBonusUIPacker):
    __itemsCache: Any
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _crewBooksChecker(cls, book):
        ...

class PM3TmanTemplateBonusPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def __packTmanTemplateToken(cls, tokenID, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class PawnedBonusPacker(BaseBonusUIPacker):
    eventsCache: Any
    @classmethod
    def _pack(cls, bonus):
        ...

def getRewardOrder(rewardName):
    ...
def getNotificationBonusOrder(bonus):
    ...
def getBonusPacker(isRewardScreen=False, isOperationCompleted=False):
    ...
def packMissionsBonusModelAndTooltipData(bonuses, packer, model, tooltipData=None):
    ...
