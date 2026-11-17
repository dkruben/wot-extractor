# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/bonus_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from copy import deepcopy as deepcopy
import typing as typing
from adisp import adisp_process as adisp_process
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.lobby.awards.packers import MultiAwardVehiclesBonusUIPacker as MultiAwardVehiclesBonusUIPacker
from gui.server_events.bonuses import mergeBonuses as mergeBonuses, splitBonuses as splitBonuses, getNonQuestBonuses as getNonQuestBonuses
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap, BonusUIPacker as BonusUIPacker, Customization3Dand2DbonusUIPacker as Customization3Dand2DbonusUIPacker, BaseBonusUIPacker as BaseBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID as BACKPORT_TOOLTIP_CONTENT_ID
from gui.shared.money import Currency as Currency
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, findFirst as findFirst, first as first
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache as IPurchaseCache
from typing import Dict as Dict, List as List, Optional as Optional
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus, SimpleBonus as SimpleBonus, TmanTemplateTokensBonus as TmanTemplateTokensBonus
_logger: Any
BONUSES_ORDER: list

class QuestReward(CONST_CONTAINER):
    INDUSTRIAL_RESOURCE = 'industrial_resource'
    TOUR_COIN = 'tourcoin'
    CURRENCY_REWARDS: tuple

class CustomizationsBonusPacker(Customization3Dand2DbonusUIPacker):
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

class TmanTemplateBonusPacker(BaseBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packTmanTemplateToken(cls, tokenID, bonus):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...
    @classmethod
    def __getBonusImageName(cls, recruitInfo):
        ...

def composeBonuses(rewards, bonusesOrder=None):
    ...
def getCurrencyReward(rewards):
    ...
def findVehicle(rewards):
    ...
def getClanSupplyBonusPacker(isProgression=False):
    ...
def _normalizeCurrencyName(name):
    ...
# decorador original: @adisp_process
# decorador original: @replace_none_kwargs(...)
def extractBonuses(invoiceData, productCode, callback, purchaseCache=None):
    ...
