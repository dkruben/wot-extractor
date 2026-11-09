# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/loadouts_assistant/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import List as List, Set as Set
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType as SupportedWotldaLoadoutType

class LoadoutsAssistantCtx(CommonWebRequestCtx):
    _LOADOUT_TYPES: Any
    _clientCacheUpdatedAt: Any
    def __init__(self, clientCacheUpdatedAt):
        ...
    def getRequestType(self):
        ...
    def getClientCacheUpdatedAt(self):
        ...
    def getLoadoutTypes(self):
        ...
    def getLoadoutTypesForRequest(self):
        ...
    def isAuthorizationRequired(self):
        ...

class EasyTankEquipCtx(LoadoutsAssistantCtx):
    _LOADOUT_TYPES: set

class GenericLoadoutAssistanceCtx(LoadoutsAssistantCtx):
    def addLoadoutTypes(self, types):
        ...
