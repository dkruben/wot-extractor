# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfilePersonnelView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from adisp import adisp_process as adisp_process
from constants import CLAN_MEMBER_FLAGS as CLAN_MEMBER_FLAGS
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from gui.Scaleform.daapi.view.lobby.clans.profile import MAX_MEMBERS_IN_CLAN as MAX_MEMBERS_IN_CLAN
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import HeaderItemsTypes as HeaderItemsTypes, ProfileUtils as ProfileUtils
from gui.Scaleform.daapi.view.meta.ClanProfilePersonnelViewMeta import ClanProfilePersonnelViewMeta as ClanProfilePersonnelViewMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.clans import formatters as clans_fmts
from gui.clans.data_wrapper.utils import formatField as formatField, isValueAvailable as isValueAvailable
from gui.clans.settings import CLIENT_CLAN_RESTRICTIONS as RES
from gui.impl import backport as backport
from gui.shared.event_dispatcher import showClanInvitesWindow as showClanInvitesWindow
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import sortByFields as sortByFields, weightedAvg as weightedAvg
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from gui.wgcg.web_controller import SYNC_KEYS as SYNC_KEYS
from helpers import i18n as i18n
from helpers.i18n import makeString as _ms
from messenger.gui.Scaleform.data.contacts_vo_converter import ContactConverter as ContactConverter
from messenger.m_constants import USER_ACTION_ID as USER_ACTION_ID
from messenger.proto.bw.find_criteria import BWClanChannelFindCriteria as BWClanChannelFindCriteria
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, ChannelsStorage as ChannelsStorage, UsersStorage as UsersStorage
OPEN_INVITES_ACTION_ID = 'openInvites'
OPEN_CLAN_CHANNEL_ACTION_ID = 'openClanChannel'
_UNAVAILABLE_EFFICIENCY_VALUE = -1
_CLAN_MEMBERS_SORT_INDEXES: tuple

class _SORT_IDS(object):
    USER_NAME = 'userName'
    POST = 'post'
    RATING = 'rating'
    BATTLES_COUNT = 'battlesCount'
    BATTLES_PERFORMANCE = 'battlesPerformance'
    AWG_XP = 'awgXP'
    DAYS_IN_CLAN = 'daysInClan'

class ClanProfilePersonnelView(ClanProfilePersonnelViewMeta):
    channelsStorage: Any
    __membersDP: Any
    _dummyMustBeShown: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def setClanDossier(self, clanDossier):
        ...
    def onHeaderButtonClick(self, actionId):
        ...
    def onAccountClanProfileChanged(self, profile):
        ...
    def onClanAppsCountReceived(self, clanDbID, appsCount):
        ...
    def _dispose(self):
        ...
    def _updateHeaderState(self):
        ...
    def _initHeaderBtnStates(self):
        ...

class _ClanMembersDataProvider(SortableDAAPIDataProvider, UsersInfoHelper):
    usersStorage: Any
    _list: Any
    __mapping: Any
    __selectedID: Any
    __accountsList: Any
    __sortMapping: Any
    def __init__(self):
        ...
    def setFlashObject(self, movieClip, autoPopulate=True, setScript=True):
        ...
    @property
    def collection(self):
        ...
    @property
    def sortedCollection(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def getSelectedIdx(self):
        ...
    def setSelectedID(self, clanID):
        ...
    def getVO(self, index):
        ...
    def buildList(self, accounts, syncUserInfo=False):
        ...
    def refreshItem(self, cache, clanDBID):
        ...
    def pyGetSelectedIdx(self):
        ...
    def onUserNamesReceived(self, names):
        ...
    def pySortOn(self, fields, order):
        ...
    def getAvgGlobalRating(self):
        ...
    def getAvgBattlesCount(self):
        ...
    def getAvgPerformanceBattles(self):
        ...
    def getAvgXp(self):
        ...
    def _makeVO(self, memberData):
        ...
    def _dispose(self):
        ...
    def __me_onUserActionReceived(self, actionID, contact, shadowMode):
        ...
    def __me_onClanMembersListChanged(self):
        ...
    def __me_onUserStatusUpdated(self, _):
        ...
    def __sortingMethod(self, item, field):
        ...
    def __getMemberName(self, memberData):
        ...
    def __getMemberRole(self, memberData):
        ...
    def __getMemberRating(self, memberData):
        ...
    def __getMemberBattlesCount(self, memberData):
        ...
    def __getMemberBattlesPerformance(self, memberData):
        ...
    def __getMemberAwgExp(self, memberData):
        ...
    def __getMemberDaysInClan(self, memberData):
        ...

def _packStat(description, tooltip, icon, isEnabled, text):
    ...
def _packColumn(columdID, label, buttonWidth, tooltip, icon='', sortOrder=-1, showSeparator=True, defaultSortDirection='descending'):
    ...
def _getAvgStringValue(dataList, key, formatter=None):
    ...
def _getWeighedAvgStringValue(dataList, key, weightKey, formatter=None):
    ...
