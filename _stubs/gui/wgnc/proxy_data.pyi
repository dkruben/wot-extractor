# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/proxy_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.view.lobby.referral_program.referral_program_helpers import getReferralProgramURL as getReferralProgramURL
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.awards.event_dispatcher import showRecruiterAward as showRecruiterAward
from gui.integrated_auction.messages import pushRateErrorMessage as pushRateErrorMessage, pushBelowCompetitiveRateMessage as pushBelowCompetitiveRateMessage
from gui.promo.promo_logger import PromoLogSourceType as PromoLogSourceType, PromoLogActions as PromoLogActions
from gui.shared.event_dispatcher import showReferralProgramWindow as showReferralProgramWindow
from gui.wgnc.common import WebHandlersContainer as WebHandlersContainer
from gui.wgnc.events import g_wgncEvents as g_wgncEvents
from gui.wgnc.settings import WGNC_DATA_PROXY_TYPE as WGNC_DATA_PROXY_TYPE
from helpers import dependency as dependency
from gui.wgnc.image_notification_helper import showPaymentMethodLinkNotification as showPaymentMethodLinkNotification, showPaymentMethodUnlinkNotification as showPaymentMethodUnlinkNotification
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IBrowserController as IBrowserController, IPromoController as IPromoController, IReferralProgramController as IReferralProgramController, IClanNotificationController as IClanNotificationController
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.shared.promo import IPromoLogger as IPromoLogger
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any

class _ProxyDataItem(object):
    def getType(self):
        ...
    def show(self, notID):
        ...

class _ClanBaseAooItem(_ProxyDataItem):
    def getID(self):
        ...

class ClanApplicationItem(_ClanBaseAooItem):
    __accountId: Any
    __appId: Any
    __applicationsCount: Any
    def __init__(self, account_id, application_id, active_applications_count):
        ...
    def getType(self):
        ...
    def getAccountID(self):
        ...
    def getApplicationID(self):
        ...
    def getActiveApplicationsCount(self):
        ...
    def getID(self):
        ...

class _ClanApplicationActionItem(_ProxyDataItem):
    __accountId: Any
    __appId: Any
    def __init__(self, account_id, application_id):
        ...
    def getAccountID(self):
        ...
    def getApplicationID(self):
        ...

class ClanAppAcceptedActionItem(_ClanApplicationActionItem):
    def getType(self):
        ...

class ClanAppDeclinedActionItem(_ClanApplicationActionItem):
    def getType(self):
        ...

class ClanInviteItem(_ClanBaseAooItem):
    __inviteId: Any
    __clanId: Any
    __clanName: Any
    __clanTag: Any
    __activeInvitesCount: Any
    def __init__(self, invite_id, clan_id, clan_name, clan_tag, active_invites_count):
        ...
    def getType(self):
        ...
    def getInviteId(self):
        ...
    def getClanId(self):
        ...
    def getClanName(self):
        ...
    def getClanTag(self):
        ...
    def getActiveInvitesCount(self):
        ...
    def getID(self):
        ...
    def getAccountDbID(self):
        ...

class _ClanPersonalAppItem(_ProxyDataItem):
    __clanId: Any
    __clanName: Any
    __clanTag: Any
    __applicationId: Any
    def __init__(self, clan_id, clan_name, clan_tag, application_id):
        ...
    def getClanId(self):
        ...
    def getClanName(self):
        ...
    def getClanTag(self):
        ...
    def getApplicationId(self):
        ...

class ClanAppDeclinedItem(_ClanPersonalAppItem):
    def getType(self):
        ...

class ClanAppAcceptedItem(_ClanPersonalAppItem):
    def getType(self):
        ...

class _ClanInviteActionResultItem(_ProxyDataItem):
    __accountId: Any
    __inviteId: Any
    def __init__(self, account_id, invite_id):
        ...
    def getAccountID(self):
        ...
    def getInviteId(self):
        ...
    def getID(self):
        ...

class ClanInviteDeclinedItem(_ClanInviteActionResultItem):
    def getType(self):
        ...

class ClanInvitesCreatedItem(_ProxyDataItem):
    __accountIds: Any
    __inviteIds: Any
    def __init__(self, account_id, invite_id):
        ...
    def getAccountIDs(self):
        ...
    def getInviteIds(self):
        ...
    def getNewInvitesCount(self):
        ...
    def getType(self):
        ...

class ClanInviteAcceptedItem(_ClanInviteActionResultItem):
    def getType(self):
        ...

class ShowTeaserItem(_ProxyDataItem):
    _loginManager: Any
    _promoCtrl: Any
    __data: Any
    def __init__(self, data):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowInBrowserItem(_ProxyDataItem, WebHandlersContainer):
    browserCtrl: Any
    __url: Any
    __size: Any
    __title: Any
    __titleKey: Any
    __showRefresh: Any
    __webHandlerName: Any
    __isSolidBorder: Any
    def __init__(self, url, size=None, title=None, showRefresh=False, webHandlerName='', titleKey='', isSolidBorder=False):
        ...
    def getType(self):
        ...
    # decorador original: @adisp_process
    def show(self, _):
        ...
    def __getTitle(self):
        ...

class UpdateRefferalBubbleItem(_ProxyDataItem):
    _referralCtrl: Any
    def getType(self):
        ...
    def show(self, _):
        ...

class UpdateClanNotificationItem(_ProxyDataItem):
    _notificationCtrl: Any
    _alias: Any
    _value: Any
    _isIncrement: Any
    def __init__(self, alias, value, isIncrement):
        ...
    def getType(self):
        ...
    def show(self, notID):
        ...

class BecomeRecruiterItem(_ProxyDataItem):
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowReferralWindowItem(_ProxyDataItem):
    __relativeUrl: Any
    def __init__(self, relativeUrl=None):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class PaymentMethodChangeItem(_ProxyDataItem):
    __operation: Any
    __method: Any
    __cdnUrl: Any
    def __init__(self, operation, method, cdnUrl):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowMapboxSurveyAvailableMessage(_ProxyDataItem):
    __systemMessages: Any
    __mapName: Any
    def __init__(self, mapName):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowMapboxEventStartedMessage(_ProxyDataItem):
    __systemMessages: Any
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowMapboxEventEndedMessage(_ProxyDataItem):
    __systemMessages: Any
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowMapboxRewardReceivedMessage(_ProxyDataItem):
    __systemMessages: Any
    __rewardData: Any
    def __init__(self, rewardData):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowAuctionRateErrorMessage(_ProxyDataItem):
    __systemMessages: Any
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowAuctionBelowCompetitiveRateMessage(_ProxyDataItem):
    __systemMessages: Any
    def getType(self):
        ...
    def show(self, _):
        ...

class ShowAuctionLostRateMessage(_ProxyDataItem):
    __systemMessages: Any
    __messageData: Any
    def __init__(self, messageData):
        ...
    def getType(self):
        ...
    def show(self, _):
        ...

class ClanSupplyQuestUpdateMessage(_ProxyDataItem):
    __name: Any
    __progress: Any
    __status: Any
    def __init__(self, name, progress, status):
        ...
    def getName(self):
        ...
    def getProgress(self):
        ...
    def getStatus(self):
        ...
    def getType(self):
        ...

class ProxyDataHolder(object):
    __items: Any
    def __init__(self, items):
        ...
    def all(self):
        ...
    def hasItemType(self, itemType):
        ...
    def getItemByType(self, itemType):
        ...
