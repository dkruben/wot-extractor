# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/requests/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from external_strings_utils import truncate_utf8 as truncate_utf8
from gui.prb_control import settings as prb_settings
from gui.battle_control.requests.settings import AVATAR_REQUEST_TYPE as AVATAR_REQUEST_TYPE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.shared.utils.requesters import RequestCtx as RequestCtx

# decorador original: @ReprInjector.withParent(...)
class SendInvitesCtx(RequestCtx):
    __playerIDs: Any
    __comment: Any
    def __init__(self, playerIDs, comment='', waitingID=''):
        ...
    def __repr__(self):
        ...
    def getPlayerIDs(self):
        ...
    def getComment(self):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...
