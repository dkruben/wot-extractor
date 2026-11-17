# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/notification/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_BOND_EQUIPMENT_REMINDER_SHOWN_TIMESTAMP as COMP7_BOND_EQUIPMENT_REMINDER_SHOWN_TIMESTAMP, COMP7_LAST_SEASON_WITH_SEEN_REWARD as COMP7_LAST_SEASON_WITH_SEEN_REWARD, COMP7_LAST_MASKOT_WITH_SEEN_REWARD as COMP7_LAST_MASKOT_WITH_SEEN_REWARD
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import hasAvailableOfferTokens as hasAvailableOfferTokens
from comp7.gui.impl.lobby.rewards_screen import TokensRewardsView as TokensRewardsView, YearlyRewardsView as YearlyRewardsView
from comp7.gui.impl.lobby.rewards_selection_screen import Comp7RewardsSelectionView as Comp7RewardsSelectionView
from comp7.notification.decorators import Comp7BondEquipmentDecorator as Comp7BondEquipmentDecorator
from comp7_common_const import COMP7_MASKOT_ID as COMP7_MASKOT_ID
from frameworks.wulf import ViewStatus as ViewStatus
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from notification.decorators import MessageDecorator as MessageDecorator
from notification.listeners import BaseReminderListener as BaseReminderListener
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE, NotificationData as NotificationData
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class Comp7OfferTokenListener(BaseReminderListener, Notifiable):
    __comp7Controller: Any
    __guiLoader: Any
    __TYPE = NOTIFICATION_TYPE.COMP7_OFFER_TOKENS
    __ENTITY_ID = 0
    __TEMPLATE = 'BondEquipmentChoosingMessage'
    __noNoftifyRewardViews: tuple
    __noNoftifyRewardSelectionViews: tuple
    __noNotifyViewTypes: Any
    __isNotificationBlockedByView: Any
    def __init__(self):
        ...
    def start(self, model):
        ...
    def stop(self):
        ...
    def _createNotificationData(self, priority, **__):
        ...
    def _createDecorator(self, data):
        ...
    def __onTokensUpdate(self, *_):
        ...
    def __onComp7ConfigChanged(self, *_):
        ...
    def __onViewStatusChanged(self, viewID, status):
        ...
    def __tryNotify(self):
        ...
    def __addNotifier(self, notificationTime):
        ...
    def __getTimeToStart(self, startDate):
        ...
