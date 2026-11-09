# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/PrebattleUserCMHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import AppealCMHandler as AppealCMHandler
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.prb_control.entities.base.legacy.ctx import KickPlayerCtx as KickPlayerCtx
from gui.prb_control.entities.base.legacy.listener import ILegacyListener as ILegacyListener
from gui.shared.system_factory import registerLobbyContexMenuHandler as registerLobbyContexMenuHandler
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
KICK_FROM_PREBATTLE = 'kickPlayerFromPrebattle'

class PrebattleUserCMHandler(AppealCMHandler, ILegacyListener):
    _isCreator: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    def fini(self):
        ...
    def onPlayerRemoved(self, entity, playerInfo):
        ...
    # decorador original: @adisp_process
    def kickPlayerFromPrebattle(self, databaseID):
        ...
    def _addMutedInfo(self, options, userCMInfo):
        ...
    def _addPrebattleInfo(self, options, userCMInfo):
        ...
    def _canKickPlayer(self):
        ...

def kickPlayerFromPrebattle(cm):
    ...
