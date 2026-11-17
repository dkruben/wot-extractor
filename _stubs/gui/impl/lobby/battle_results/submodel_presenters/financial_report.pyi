# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/financial_report.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from math import ceil as ceil
import typing as typing
from shared_utils import first as first
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import PremiumConfigs as PremiumConfigs, PREMIUM_TYPE as PREMIUM_TYPE
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl, getWotPlusShopUrl as getWotPlusShopUrl
from gui.battle_results.pbs_helpers.additional_bonuses import getAccountStatusToBRPS as getAccountStatusToBRPS, getAdditionalXpBonusStatus as getAdditionalXpBonusStatus, isAddXpBonusStatusAcceptable as isAddXpBonusStatusAcceptable, isAdditionalXpBonusAvailable as isAdditionalXpBonusAvailable, getLeftAdditionalBonus as getLeftAdditionalBonus, getAdditionalXPFactor10FromResult as getAdditionalXPFactor10FromResult, getAdditionalXpBonusDiff as getAdditionalXpBonusDiff
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.presenters.packers.economics.financial_report_packers import CrystalsDetailsPacker as CrystalsDetailsPacker, XpDetailsPacker as XpDetailsPacker, FreeXpDetailsPacker as FreeXpDetailsPacker, CreditsStatisticsPacker as CreditsStatisticsPacker, GoldStatisticsPacker as GoldStatisticsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.game_control.wot_plus.utils import WOT_PLUS_TIER_MAP as WOT_PLUS_TIER_MAP
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import AdditionalBonusModel as AdditionalBonusModel, PremiumXpBonusRestriction as PremiumXpBonusRestriction, BonusStates as BonusStates
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel as CurrencyRecordsItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.financial_report_model import FinancialReportModel as FinancialReportModel
from gui.impl.lobby.premacc import premacc_helpers as premacc_helpers
from gui.shared import events as events
from gui.shared.event_dispatcher import showShop as showShop, showDailyExpPageView as showDailyExpPageView
from helpers import dependency as dependency, server_settings as server_settings, time_utils as time_utils
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import ViewModel as ViewModel

class ManageableBonusSubPresenter(BattleResultsSubPresenter):
    __itemsCache: Any
    __lobbyContext: Any
    __wotPlusController: Any
    __gameSession: Any
    @classmethod
    def getViewModelType(cls):
        ...
    @property
    def arenaUniqueID(self):
        ...
    def packBattleResults(self, battleResults):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getCallbacks(self):
        ...
    def __onXpBonusApplied(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    def __onWotPlusChanged(self, data):
        ...
    def __onPremiumStatusChanged(self, _=None):
        ...
    def __onXpBonusStatusChanged(self, _=None):
        ...
    def __onLocalStorageUpdated(self, event):
        ...
    def _onShowDetails(self, _=None):
        ...

class FinancialReportSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def _getListeners(self):
        ...
    def _getCallbacks(self):
        ...
    def __onXpBonusStatusChanged(self, _=None):
        ...
