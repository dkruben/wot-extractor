# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanSendInvitesWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.SendInvitesWindow import SendInvitesWindow as SendInvitesWindow
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.clans import formatters as clans_fmts
from gui.clans.clan_helpers import ClanListener as ClanListener, showClanInviteSystemMsg as showClanInviteSystemMsg
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from gui.wgcg.clan import contexts as clan_ctx
from helpers import i18n as i18n
from messenger.m_constants import USER_TAG as USER_TAG

class ClanSendInvitesWindow(SendInvitesWindow, UsersInfoHelper, ClanListener):
    __clanDbID: Any
    def __init__(self, ctx):
        ...
    # decorador original: @adisp_process
    def sendInvites(self, accountsToInvite, comment):
        ...
    def _populate(self):
        ...
    def _initCooldown(self):
        ...
    def _finiCooldown(self):
        ...
    def _handleSetCoolDown(self, event):
        ...
    def _getTitle(self):
        ...
