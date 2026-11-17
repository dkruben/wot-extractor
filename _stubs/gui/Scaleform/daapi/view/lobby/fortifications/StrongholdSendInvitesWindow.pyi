# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdSendInvitesWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from gui.prb_control.entities.base.external_battle_unit.base_external_battle_ctx import SendInvitesExternalBattleUnitCtx as SendInvitesExternalBattleUnitCtx
from gui.Scaleform.daapi.view.lobby.SendInvitesWindow import SendInvitesWindow as SendInvitesWindow
from gui.shared.utils.requesters.abstract import Response as Response
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper as UsersInfoHelper
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.INVITES import INVITES as INVITES

class StrongholdSendInvitesWindow(SendInvitesWindow, UsersInfoHelper):
    def sendInvites(self, accountsToInvite, comment):
        ...
    def __sendInvitesCallback(self, accountsToInvite, response):
        ...
