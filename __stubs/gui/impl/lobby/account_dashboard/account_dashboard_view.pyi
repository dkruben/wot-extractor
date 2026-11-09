# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/account_dashboard_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.account_dashboard.account_dashboard_model import AccountDashboardModel as AccountDashboardModel
from gui.impl.lobby.account_dashboard.features.bonus_xp_feature import BonusXPFeature as BonusXPFeature
from gui.impl.lobby.account_dashboard.features.dog_tags_feature import DogTagsFeature as DogTagsFeature
from gui.impl.lobby.account_dashboard.features.excluded_maps_feature import ExcludedMapsFeature as ExcludedMapsFeature
from gui.impl.lobby.account_dashboard.features.header_feature import HeaderFeature as HeaderFeature
from gui.impl.lobby.account_dashboard.features.parental_control_feature import ParentalControlFeature as ParentalControlFeature
from gui.impl.lobby.account_dashboard.features.premium_account_feature import PremiumAccountFeature as PremiumAccountFeature
from gui.impl.lobby.account_dashboard.features.premium_quests_feature import PremiumQuestsFeature as PremiumQuestsFeature
from gui.impl.lobby.account_dashboard.features.reserve_stock_feature import ReserveStockFeature as ReserveStockFeature
from gui.impl.lobby.account_dashboard.features.subscriptions_feature import SubscriptionsFeature as SubscriptionsFeature
from gui.impl.lobby.account_dashboard.sound_constants import ACC_DASHBOARD_SOUND_SPACE as ACC_DASHBOARD_SOUND_SPACE
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from uilogging.wot_plus.loggers import WotPlusAccountDashboardLogger as WotPlusAccountDashboardLogger
_logger: Any

class Feature(CONST_CONTAINER):
    HEADER = 'header'
    SUBSCRIPTIONS = 'subscriptions'
    PREMIUM_ACCOUNT = 'premiumAccount'
    BONUS_XP = 'bonusXp'
    RESERVER_STOCK = 'reserveStock'
    PREMIUM_QUESTS = 'premiumQuests'
    EXCLUDED_MAPS = 'excludedMaps'
    DOG_TAGS = 'dogTags'
    PARENTAL_CONTROL = 'parentalControl'

class AccountDashboardView(ViewImpl):
    __slots__: tuple
    __lobbyContext: Any
    _COMMON_SOUND_SPACE = ACC_DASHBOARD_SOUND_SPACE
    _features: Any
    _wotPlusUILogger: Any
    modelDataControllers: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def createPopOverContent(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onClose(self):
        ...
