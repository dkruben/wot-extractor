# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/view_helpers/UsersInfoHelper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from Event import Event as Event
from constants import IGR_TYPE as IGR_TYPE
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.shared import formatters as shared_fmts
from gui.shared.view_helpers.UsersInfoController import UsersInfoController as UsersInfoController
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.m_constants import USER_GUI_TYPE as USER_GUI_TYPE, UserEntityScope as UserEntityScope, USER_TAG as USER_TAG
from messenger.proto import proto_getter as proto_getter, PROTO_TYPE as PROTO_TYPE
from messenger.proto.entities import SharedUserEntity as SharedUserEntity
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class UsersInfoHelper(object):
    lobbyContext: Any
    _rqCtrl: Any
    usersStorage: Any
    _invalid: Any
    __callback: Any
    onNamesReceived: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    @classmethod
    def clear(cls):
        ...
    @classmethod
    def fini(cls):
        ...
    def onUserNamesReceived(self, names):
        ...
    def onUserRatingsReceived(self, ratings):
        ...
    def onUserClanAbbrevsReceived(self, abbrevs):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def getContact(self, userID, scope=...):
        ...
    def getUserName(self, userID, scope=...):
        ...
    def getUserClanAbbrev(self, userDbID):
        ...
    def getUserRegionCode(self, userDbID):
        ...
    def getUserRating(self, userDbID):
        ...
    def buildGuiUserData(self, user):
        ...
    def getGuiUserData(self, userDbID):
        ...
    def getGuiUserDataWithStatus(self, userDbID):
        ...
    def getGuiUserName(self, userID, formatter=..., scope=...):
        ...
    def getGuiUserRating(self, userDbID, formatter=...):
        ...
    def getUserTags(self, userID, igrType):
        ...
    def syncUsersInfo(self):
        ...
