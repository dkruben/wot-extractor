# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/common/lootboxes.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import iteritems as iteritems, viewvalues as viewvalues
from constants import LOOTBOX_TOKEN_PREFIX as LOOTBOX_TOKEN_PREFIX
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_lootbox import FunRandomLootbox as FunRandomLootbox
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel as TokenBonusModel
from gui.impl.lobby.awards.packers import MultiAwardVehiclesBonusUIPacker as MultiAwardVehiclesBonusUIPacker
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, CreditsBonus as CreditsBonus, GoldBonus as GoldBonus, CrystalBonus as CrystalBonus
from gui.shared.missions.packers.bonus import TokenBonusUIPacker as TokenBonusUIPacker
from gui.shared.money import Money as Money, Currency as Currency
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.server_events.bonuses import TokensBonus as TokensBonus
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
FEP_CATEGORY = 'FEPLootBoxes'

class FunRandomLootBoxTypes(object):
    ORDINARY = 'fep_ordinary'
    UNUSUAL = 'fep_unusual'
    RARE = 'fep_rare'
    EPIC = 'fep_epic'
    LEGENDARY = 'fep_legendary'
    ALL: tuple
    ORDERED: Any

class FunRandomLootBoxTokenBonusPacker(TokenBonusUIPacker, FunAssetPacksMixin):
    itemsCache: Any
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
    def _getIconPath(cls, iconSize, rarity):
        ...
    @classmethod
    def __packLootBox(cls, tokenID, model, bonus):
        ...
    @classmethod
    def __isSuitable(cls, tokenID, token):
        ...
    @classmethod
    def __isBoxAvailable(cls, tokenID):
        ...

class FunRandomRewardLootBoxTokenBonusPacker(FunRandomLootBoxTokenBonusPacker):
    @classmethod
    def _getIconPath(cls, iconSize, rarity):
        ...

class FunRandomLootBoxVehiclesBonusUIPacker(MultiAwardVehiclesBonusUIPacker):
    COMPENSATION_BONUSES_MAP: dict
    @classmethod
    def _getVehicleCompensationTooltipContent(cls):
        ...
    @classmethod
    def _getCompensation(cls, vehicle, bonus):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def sortTokenFunc(token, itemsCache=...):
    ...
def packLootboxes(lootboxes, lbConfig, lootboxesModel, packer, visibleLBAwardsNames, localeRes, tooltips=None):
    ...
def packLootboxRewards(lootBoxData, rewardsModel, packer, tooltipData=None):
    ...
def parseBonusesWithProbabilities(data):
    ...
