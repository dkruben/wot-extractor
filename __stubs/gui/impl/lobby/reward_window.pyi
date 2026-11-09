# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/reward_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.gui_constants import WindowFlags as WindowFlags, WindowLayer as WindowLayer, ViewFlags as ViewFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import PackRentVehiclesAwardComposer as PackRentVehiclesAwardComposer, AnniversaryAwardComposer as AnniversaryAwardComposer, CurtailingAwardsComposer as CurtailingAwardsComposer, RawLabelBonusComposer as RawLabelBonusComposer
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getMissionInfoData as getMissionInfoData
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.backport import TooltipData as TooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.ui_kit.reward_renderer_model import RewardRendererModel as RewardRendererModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_reward_view_model import SubscriptionRewardViewModel as SubscriptionRewardViewModel
from gui.impl.gen.view_models.windows.piggy_bank_reward_window_content_model import PiggyBankRewardWindowContentModel as PiggyBankRewardWindowContentModel
from gui.impl.gen.view_models.windows.reward_window_content_model import RewardWindowContentModel as RewardWindowContentModel
from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView as showClanSupplyView
from gui.impl.lobby.player_subscriptions.player_subscriptions_reward_window_view import PlayerSubscriptionRewardWindowView as PlayerSubscriptionRewardWindowView
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl, WindowView as WindowView
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.awards_formatters import getPackRentVehiclesAwardPacker as getPackRentVehiclesAwardPacker, getAnniversaryPacker as getAnniversaryPacker, getDefaultAwardFormatter as getDefaultAwardFormatter
from gui.server_events.bonuses import getTutorialBonuses as getTutorialBonuses, CreditsBonus as CreditsBonus, getNonQuestBonuses as getNonQuestBonuses
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_logger: Any
BASE_EVENT_NAME = 'base'
_ADDITIONAL_AWARDS_COUNT = 5

class BaseRewardWindowContent(ViewImpl):
    __slots__: tuple
    _BONUSES_ORDER: tuple
    __items: Any
    _eventName: Any
    def __init__(self, settings, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def handleNextButton(self):
        ...
    def handleGoToButton(self):
        ...
    def createToolTip(self, event):
        ...
    def _keySortOrder(self, bonus):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _setTitles(self):
        ...
    def _getBonuses(self):
        ...
    def _getAwardComposer(self):
        ...
    def _getRewardRendererModelCls(self):
        ...
    def _initRewardsList(self):
        ...
    def _initTooltip(self, bonus, index):
        ...
    def _setShowRewards(self, tx):
        ...
    def _getRewardsModel(self, tx):
        ...
    def _setBonusModel(self, rewardTx, bonus, index):
        ...

class PiggyBankRewardWindowContent(BaseRewardWindowContent):
    __slots__: tuple
    _isPremActive: Any
    _credits: Any
    def __init__(self, settings, ctx=None):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getBonuses(self):
        ...
    def handleNextButton(self):
        ...
    def onHyperLinkClicked(self):
        ...
    def _getAwardComposer(self):
        ...

class QuestRewardWindowContent(BaseRewardWindowContent):
    __slots__: tuple
    _quest: Any
    _vehicles: Any
    def __init__(self, settings, ctx=None):
        ...
    def _getBonuses(self):
        ...
    def _getAwardComposer(self):
        ...
    def _finalize(self):
        ...

class RewardWindowBase(WindowImpl):
    appLoader: Any
    __slots__: tuple
    def __init__(self, parent, content, layer=...):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onConfirmBtnClicked(self, _=None):
        ...
    def _onDecoratorReady(self):
        ...
    def _onSecondBtnClicked(self, _=None):
        ...

class RewardWindow(RewardWindowBase):
    __slots__: tuple
    def __init__(self, ctx=None, parent=None):
        ...

class TwitchRewardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, ctx, parent=None):
        ...

class DynamicRewardWindowContent(BaseRewardWindowContent):
    __slots__: tuple
    _BONUSES_ORDER: tuple
    __bonuses: Any
    def __init__(self, settings, ctx=None):
        ...
    def handleNextButton(self):
        ...
    def handleGoToButton(self):
        ...
    def _getBonuses(self):
        ...
    def _finalize(self):
        ...

class DynamicRewardWindow(RewardWindowBase):
    __slots__: tuple
    _eventName: Any
    def __init__(self, ctx=None, parent=None):
        ...
    def _initialize(self):
        ...

class GiveAwayRewardWindowContent(QuestRewardWindowContent):
    __slots__: tuple
    _BONUSES_ORDER: tuple
    def handleNextButton(self):
        ...
    def _getAwardComposer(self):
        ...

class GiveAwayRewardWindow(RewardWindowBase):
    __slots__: tuple
    def __init__(self, ctx=None, parent=None):
        ...
    def _initialize(self):
        ...

class PiggyBankRewardWindow(RewardWindowBase):
    __slots__: tuple
    def __init__(self, ctx=None, parent=None):
        ...
    def _initialize(self):
        ...
