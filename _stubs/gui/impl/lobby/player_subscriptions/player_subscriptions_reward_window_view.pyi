# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/player_subscriptions/player_subscriptions_reward_window_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from constants import OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getMissionInfoData as getMissionInfoData
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker as TmanTemplateBonusPacker
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.player_subscriptions.main_reward_model import MainRewardModel as MainRewardModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events.bonuses import getTutorialBonuses as getTutorialBonuses, splitBonuses as splitBonuses
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap, TokenBonusUIPacker as TokenBonusUIPacker
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_reward_view_model import SubscriptionRewardViewModel as SubscriptionRewardViewModel
from gui.shared.missions.packers.bonus import BaseBonusUIPacker as BaseBonusUIPacker
from frameworks.wulf import Array as Array
_logger: Any
BASE_EVENT_NAME = 'base'
MAIN_REWARD_PREFIX = 'mainReward_'

class PlayerSubscriptionRewardWindowView(ViewImpl):
    _offersProvider: Any
    _BONUSES_ORDER: tuple
    _tooltips: Any
    _eventName: Any
    _quest: Any
    _vehicles: Any
    def __init__(self, settings, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _setTitles(self):
        ...
    def _setMainRewards(self):
        ...
    def _getEvents(self):
        ...
    def _initRewardsList(self):
        ...
    def _getBonuses(self):
        ...
    def __onCloseButtonClick(self):
        ...
    def __onChoseButtonClick(self):
        ...
    def __getOffer(self):
        ...
    def __keySortOrder(self, bonus):
        ...
    def __getPackerMap(self):
        ...

class PSTokenBonusUIPacker(TokenBonusUIPacker):
    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        ...
