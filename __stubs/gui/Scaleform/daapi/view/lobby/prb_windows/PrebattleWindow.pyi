# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattleWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from adisp import adisp_process as adisp_process
from constants import MODULE_NAME_SEPARATOR as MODULE_NAME_SEPARATOR
from debug_utils import LOG_ERROR as LOG_ERROR
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.meta.PrebattleWindowMeta import PrebattleWindowMeta as PrebattleWindowMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from skeletons.gui.game_control import ICraftmachineController as ICraftmachineController
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE as DATA_TYPE, TARGET_ID as TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window as stored_window
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.prb_control.entities.base.legacy.ctx import SetPlayerStateCtx as SetPlayerStateCtx
from gui.prb_control.entities.base.legacy.listener import ILegacyListener as ILegacyListener
from gui.prb_control.formatters import messages as messages
from gui.prb_control.items import prb_items as prb_items
from gui.prb_control.settings import CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE, PREBATTLE_PLAYERS_SORT_TYPES as PREBATTLE_PLAYERS_SORT_TYPES
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import FocusEvent as FocusEvent
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from messenger import g_settings as g_settings, MessengerEntry as MessengerEntry
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS as MESSENGER_VIEW_ALIAS
from messenger.m_constants import USER_GUI_TYPE as USER_GUI_TYPE, PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from prebattle_shared import decodeRoster as decodeRoster
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

# decorador original: @stored_window(...)
class PrebattleWindow(PrebattleWindowMeta, ILegacyListener):
    lobbyContext: Any
    __craftmacineConrtoller: Any
    usersStorage: Any
    __prbName: Any
    __clientID: Any
    def __init__(self, prbName='prebattle'):
        ...
    def onFocusIn(self, alias):
        ...
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def onSourceLoaded(self):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    # decorador original: @adisp_process
    def requestToReady(self, value):
        ...
    def requestToLeave(self):
        ...
    def showPrebattleSendInvitesWindow(self):
        ...
    def showFAQWindow(self):
        ...
    def getClientID(self):
        ...
    def requestToKickPlayer(self, value):
        ...
    def canSendInvite(self):
        ...
    def isPlayerReady(self):
        ...
    def isPlayerCreator(self):
        ...
    def isReadyBtnEnabled(self):
        ...
    def isLeaveBtnEnabled(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    @property
    def chat(self):
        ...
    def onPlayerAdded(self, entity, playerInfo):
        ...
    def onPlayerRemoved(self, entity, playerInfo):
        ...
    def onPlayerRosterChanged(self, entity, actorInfo, playerInfo):
        ...
    def onPlayerStateChanged(self, entity, roster, accountInfo):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _closeSendInvitesWindow(self):
        ...
    def _isInLegacyPreBattle(self):
        ...
    def _setRosterList(self, rosters):
        ...
    def _makeAccountsData(self, accounts, playerSortKeyType=...):
        ...
    def _handleCurrentVehicleChanged(self):
        ...
    def _onUserActionReceived(self, actionIndex, user, shadowMode):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @adisp_process
    def _doLeave(self, isExit=True, parent=None):
        ...
    def __handlePrbChannelControllerInited(self, event):
        ...
