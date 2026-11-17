# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_helpers/comp7_light_packers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7_light.skeletons.gui.game_control import IComp7LightProgressionController as IComp7LightProgressionController
from constants import EVENT_TYPE as EVENT_TYPE
from gui.battle_pass.battle_pass_bonuses_packers import getBattlePassBonusPacker as getBattlePassBonusPacker
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel
from gui.server_events.formatters import COMPLEX_TOKEN as COMPLEX_TOKEN
from gui.shared.missions.packers.bonus import SimpleBonusUIPacker as SimpleBonusUIPacker, TokenBonusUIPacker as TokenBonusUIPacker, getLocalizedBonusName as getLocalizedBonusName
from gui.shared.missions.packers.events import DailyQuestUIDataPacker as DailyQuestUIDataPacker, packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
from gui.shared.money import Currency as Currency
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.server_events.bonuses import CurrenciesBonus as CurrenciesBonus

class Comp7LightDailyQuestUIDataPacker(DailyQuestUIDataPacker):
    _tooltipData: Any
    def _packBonuses(self, model):
        ...

class Comp7LightTokenBonusUIPacker(TokenBonusUIPacker):
    _comp7LightProgressionController: Any
    _COMP7_LIGHT_PROGRESSION_TOKEN = 'Comp7LightProgressionToken'
    @classmethod
    def _getTokenBonusType(cls, tokenID, complexToken):
        ...
    @classmethod
    def _getTooltipsPackers(cls):
        ...
    @classmethod
    def _getTokenBonusPackers(cls):
        ...
    @classmethod
    def __getComp7LightProgressionTooltip(cls, *_):
        ...

class _CurrencyBonusUIPacker(SimpleBonusUIPacker):
    @classmethod
    def _pack(cls, bonus):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, label):
        ...
    @classmethod
    def _getBonusModel(cls):
        ...

def getComp7LightBonusPacker():
    ...
def getComp7LightEventUIDataPacker(event):
    ...
