# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/BattleSessionList.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from adisp import adisp_process as adisp_process
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattlesListWindow import PrebattlesListWindow as PrebattlesListWindow
from gui.Scaleform.daapi.view.meta.BattleSessionListMeta import BattleSessionListMeta as BattleSessionListMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES import MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES as MESSENGER_CHANNEL_CAROUSEL_ITEM_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE as DATA_TYPE, TARGET_ID as TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window as stored_window
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control import formatters as formatters
from gui.prb_control.entities.battle_session.legacy.ctx import JoinBattleSessionCtx as JoinBattleSessionCtx
from gui.prb_control.entities.battle_session.legacy.requester import AutoInvitesRequester as AutoInvitesRequester
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import FocusEvent as FocusEvent, ChannelCarouselEvent as ChannelCarouselEvent
from gui.shared.utils.functions import getArenaShortName as getArenaShortName
from helpers import dependency as dependency
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from gui.prb_control.items.prb_seqs import AutoInviteItem as AutoInviteItem

# decorador original: @stored_window(...)
class BattleSessionList(PrebattlesListWindow, BattleSessionListMeta):
    lobbyContext: Any
    __webCtrl: Any
    __listRequester: Any
    def __init__(self, ctx=None):
        ...
    def requestToJoinTeam(self, prbID, prbType):
        ...
    def getClientID(self):
        ...
    def onFocusIn(self, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __hideWindow(self, _):
        ...
    # decorador original: @adisp_process
    def __requestToJoin(self, prbID, prbType, prbClusterID):
        ...
    def __onBSListReceived(self, sessions):
        ...
    def __getClanBattleStartTime(self, battleSession):
        ...
    def __updateWindowOpenState(self, flag):
        ...
