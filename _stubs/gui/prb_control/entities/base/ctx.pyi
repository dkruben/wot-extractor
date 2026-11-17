# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from external_strings_utils import truncate_utf8 as truncate_utf8
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE, convertFlagsToNames as convertFlagsToNames, CTRL_ENTITY_TYPE_NAMES as CTRL_ENTITY_TYPE_NAMES, INVITE_COMMENT_MAX_LENGTH as INVITE_COMMENT_MAX_LENGTH, REQUEST_TYPE as REQUEST_TYPE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.shared.utils.requesters import RequestCtx as RequestCtx

# decorador original: @ReprInjector.withParent(...)
class PrbCtrlRequestCtx(RequestCtx):
    __slots__: tuple
    __entityType: Any
    __entityID: Any
    __isForced: Any
    __flags: Any
    __ctrlType: Any
    def __init__(self, **kwargs):
        ...
    def getCtrlType(self):
        ...
    def getCtrlTypeName(self):
        ...
    def getEntityType(self):
        ...
    def getEnityID(self):
        ...
    def setForced(self, flag):
        ...
    def isForced(self):
        ...
    def getFlags(self):
        ...
    def addFlags(self, flags):
        ...
    def hasFlags(self, flags):
        ...
    def removeFlags(self, flags):
        ...
    def clearFlags(self):
        ...
    def getFlagsToStrings(self):
        ...

# decorador original: @ReprInjector.simple(...)
class PrbAction(object):
    __slots__: tuple
    actionName: Any
    mmData: Any
    accountsToInvite: Any
    extData: Any
    def __init__(self, actionName, mmData=0, accountsToInvite=None, extData=None):
        ...

# decorador original: @ReprInjector.simple(...)
class LeavePrbAction(object):
    __slots__: tuple
    isExit: Any
    ignoreConfirmation: Any
    parent: Any
    def __init__(self, isExit=True, ignoreConfirmation=False, parent=None):
        ...

# decorador original: @ReprInjector.withParent(...)
class SendInvitesCtx(PrbCtrlRequestCtx):
    __databaseIDs: Any
    __comment: Any
    def __init__(self, databaseIDs, comment, waitingID=''):
        ...
    def getDatabaseIDs(self):
        ...
    def getComment(self):
        ...
    def getRequestType(self):
        ...

class CreatePrbEntityCtx(PrbCtrlRequestCtx):
    __slots__: tuple
    __initCtx: Any
    def __init__(self, ctrlType=..., entityType=0, flags=..., initCtx=None):
        ...
    def getInitCtx(self):
        ...
    def clear(self):
        ...
