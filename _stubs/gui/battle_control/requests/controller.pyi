# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/requests/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from debug_utils import LOG_WARNING as LOG_WARNING
from ids_generators import Int32IDGenerator as Int32IDGenerator
from helpers import i18n as i18n
from messenger import MessengerEntry as MessengerEntry, g_settings as g_settings
from gui.shared.utils.requesters.abstract import RequestsByIDProcessor as RequestsByIDProcessor
from gui.shared.utils.requesters.RequestsController import RequestsController as RequestsController
from gui.shared.rq_cooldown import RequestCooldownManager as RequestCooldownManager, REQUEST_SCOPE as REQUEST_SCOPE
from gui.battle_control.requests.settings import AVATAR_REQUEST_TYPE as AVATAR_REQUEST_TYPE, DEFAULT_COOLDOWN as DEFAULT_COOLDOWN

class _AvatarCooldownManager(RequestCooldownManager):
    def __init__(self):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...
    def _showSysMessage(self, msg):
        ...

class _AvatarRequester(RequestsByIDProcessor):
    # base nao representavel no stub: namedtuple(...)
    class _Response:
        def isSuccess(self):
            ...
    def __init__(self):
        ...
    def getSender(self):
        ...
    def _doCall(self, method, *args, **kwargs):
        ...
    def _makeResponse(self, code=0, errMsg='', data=None, ctx=None):
        ...

class AvatarRequestsController(RequestsController):
    __handlers: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def sendInvites(self, ctx, callback=None):
        ...
    def _getHandlerByRequestType(self, requestTypeID):
        ...
    def _getRequestTimeOut(self):
        ...
