# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/bonus_packer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from battle_royale.gui.constants import STP_COIN as STP_COIN
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.battle_pass.battle_pass_bonuses_packers import getBattlePassBonusPacker as getBattlePassBonusPacker
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel as ConditionGroupModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
from gui.server_events.bonuses import mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from gui.server_events.formatters import COMPLEX_TOKEN as COMPLEX_TOKEN
from gui.shared.missions.packers.bonus import SimpleBonusUIPacker as SimpleBonusUIPacker, getLocalizedBonusName as getLocalizedBonusName, TokenBonusUIPacker as TokenBonusUIPacker, BattlePassPointsBonusPacker as BattlePassPointsBonusPacker
from gui.shared.missions.packers.conditions import CONDITION_GROUP_AND as CONDITION_GROUP_AND, CONDITION_GROUP_OR as CONDITION_GROUP_OR
from gui.shared.missions.packers.events import findFirstConditionModel as findFirstConditionModel, getEventUIDataPacker as getEventUIDataPacker
from gui.shared.money import Currency as Currency
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import List as List, Union as Union
from gui.server_events.bonuses import CurrenciesBonus as CurrenciesBonus
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as PreformattedConditionModel
BR_PROGRESSION_TOKEN = 'BRProgressionToken'

class ExtendedCurrencyBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

class CurrenciesBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packCommon(cls, bonus, model):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _getContentId(cls, bonus):
        ...

class BRBattlePassPointsBonusPacker(BattlePassPointsBonusPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...

class BRTokenBonusUIPacker(TokenBonusUIPacker):
    _brProgressionController: Any
    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        ...
    @classmethod
    def _getTooltipsPackers(cls):
        ...
    @classmethod
    def __getBRProgressionTooltip(cls, *_):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...

def getBonusPacker():
    ...
def packQuestBonuses(bonuses, bonusPacker, order=None):
    ...
def _getSortKey(order):
    ...
def getFirstConditionModelFromQuestModel(dailyQuestModel):
    ...
def _buildDescription(conditionalModel):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def packMissionItem(model, raw, questPacker=None, eventsCache=None):
    ...
