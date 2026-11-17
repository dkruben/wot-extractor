# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/invite_windows.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.meta.ReceivedInviteWindowMeta import ReceivedInviteWindowMeta as ReceivedInviteWindowMeta
from gui.prb_control import prbPeripheriesHandlerProperty as prbPeripheriesHandlerProperty, prbAutoInvitesProperty as prbAutoInvitesProperty
from gui.prb_control.formatters.invites import PrbAutoInviteInfo as PrbAutoInviteInfo
from gui.prb_control.entities.battle_session.legacy.ctx import JoinBattleSessionCtx as JoinBattleSessionCtx
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.prb_getters import getPrebattleAutoInvites as getPrebattleAutoInvites
from gui.shared import actions as actions
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.gui import events_dispatcher as events_dispatcher
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts
__author__ = 'd_savitski'

class _DisableNotify(actions.Action):
    __clientID: Any
    _completed: Any
    def __init__(self, clientID):
        ...
    def invoke(self):
        ...

class _InviteWindow(IGlobalListener, ReceivedInviteWindowMeta):
    _inviteInfo: Any
    def __init__(self, inviteInfo):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onTeamStatesReceived(self, entity, team1State, team2State):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    def cancelInvite(self):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _updateReceivedInfo(self):
        ...

class AutoInviteWindow(_InviteWindow):
    def __init__(self, ctx):
        ...
    # decorador original: @prbPeripheriesHandlerProperty
    def prbPeripheriesHandler(self):
        ...
    # decorador original: @prbAutoInvitesProperty
    def prbAutoInvites(self):
        ...
    # decorador original: @adisp_process
    def acceptInvite(self):
        ...
    def declineInvite(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onPrbAutoInvitesChanged(self):
        ...
