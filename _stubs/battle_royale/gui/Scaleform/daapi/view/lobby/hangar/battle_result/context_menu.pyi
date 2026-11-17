# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/battle_result/context_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from stats_params import BATTLE_ROYALE_STATS_ENABLED as BATTLE_ROYALE_STATS_ENABLED
from helpers import dependency as dependency
from gui.shared import utils as utils, events as events, g_eventBus as g_eventBus
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.shared import event_dispatcher as shared_events
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from messenger.storage import UsersStorage as UsersStorage, MessengerStorageDescriptor as MessengerStorageDescriptor
from messenger.proto import proto_getter as proto_getter
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS

class VEHICLE(object):
    USER_INFO = 'userInfo'
    ADD_TO_FRIEND = 'addToFriends'
    CREATE_PRIVATE_CHANNEL = 'createPrivateChannel'
    COPY_TO_CLIP_BOARD = 'copyToClipBoard'
    CREATE_BR_SQUAD = 'createBattleRoyaleSquad'
    ADD_TO_IGNORED = 'addToIgnored'
    REMOVE_FROM_FRIENDS = 'removeFromFriends'
    REMOVE_FROM_IGNORED = 'removeFromIgnored'

class BRBattleResultContextMenu(AbstractContextMenuHandler):
    __lobbyContext: Any
    usersStorage: Any
    __playerName: Any
    __playerDBId: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def showUserInfo(self):
        ...
    def addToFriend(self):
        ...
    def createPrivetChannel(self):
        ...
    def copyToClipBoard(self):
        ...
    def createBRSquad(self):
        ...
    def addToIgnored(self):
        ...
    def removeFromFriends(self):
        ...
    def removeFromIgnored(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def __isEnabledInRoaming(self, dbID):
        ...
