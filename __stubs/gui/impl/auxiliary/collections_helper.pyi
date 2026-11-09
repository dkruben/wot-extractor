# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/collections_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import IS_BATTLE_PASS_COLLECTION_SEEN as IS_BATTLE_PASS_COLLECTION_SEEN
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.collection.collections_constants import COLLECTION_ITEM_BONUS_NAME as COLLECTION_ITEM_BONUS_NAME
from gui.collection.collections_helpers import getItemName as getItemName, getItemResKey as getItemResKey
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel as RewardModel
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker as BaseBonusUIPacker, BonusUIPacker as BonusUIPacker, CustomizationBonusUIPacker as CustomizationBonusUIPacker, SimpleBonusUIPacker as SimpleBonusUIPacker, getDefaultBonusPackersMap as getDefaultBonusPackersMap
from gui.shared.money import Currency as Currency
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController
from typing import Dict as Dict
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.collection_entry_point_view_model import CollectionEntryPointViewModel as CollectionEntryPointViewModel
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus, CollectionEntitlementBonus as CollectionEntitlementBonus, BpcoinBonus as BpcoinBonus, CustomizationsBonus as CustomizationsBonus

class CurrencyBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class BattlePassCoinBonusPacker(CurrencyBonusUIPacker):
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class TmanTemplateBonusPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __packTmanTemplateToken(cls, tokenID, bonus):
        ...

class CustomizationsBonusPacker(CustomizationBonusUIPacker):
    _3D_STYLE_ICON_NAME = 'style_3d'
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class CollectionItemBonusPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

# decorador original: @replace_none_kwargs(...)
def fillCollectionModel(model, collectionId, collectionsSystem=None):
    ...
def getCollectionsBonusPacker():
    ...
