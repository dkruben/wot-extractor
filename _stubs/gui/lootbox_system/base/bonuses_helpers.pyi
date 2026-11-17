# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/bonuses_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from itertools import izip_longest as izip_longest
from future.utils import listitems as listitems
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.reward_row_model import RewardRowModel as RewardRowModel
from gui.lootbox_system.base.bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.lootbox_system.base.awards_manager import AwardsManager as AwardsManager
from gui.server_events.bonuses import _BONUSES as _BONUSES, getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from gui.shared.money import Money as Money
from items import EQUIPMENT_TYPES as EQUIPMENT_TYPES, ITEM_TYPE_INDICES as ITEM_TYPE_INDICES, parseIntCompactDescr as parseIntCompactDescr
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX as RECRUIT_TMAN_TOKEN_PREFIX
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr
RewardsGroup: Any
REWARDS_GROUP_NAME_RES = R.strings.lootbox_system.autoOpenView.rewardGroups

def isOptionalDevice(itemTypeID, _):
    ...
def isBattleBooster(itemTypeID, itemCD):
    ...
def isCrewBook(itemTypeID, _):
    ...
def noCompensation(info, _):
    ...
def getVehiclesFilter(conditions):
    ...
def getItemsFilter(conditions):
    ...
def getGoodiesFilter(conditions):
    ...
def getTankmenFilter(tokens):
    ...
def packBonusGroups(bonuses, groupModels, groupsLayout, eventName, tooltipsData=None, packer=None):
    ...
def _groupBonuses(bonuses, groupsLayout):
    ...
def _mergeCompensations(bonusesGroup):
    ...
def _getLootBoxBonuses(rewards):
    ...
