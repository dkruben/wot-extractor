# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/framework/ScopeTemplates.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowLayer as WindowLayer
from soft_exception import SoftException as SoftException
GLOBAL_SCOPE: Any
DYNAMIC_SCOPE: Any
VIEW_SCOPE: Any
WINDOW_SCOPE: Any
TOP_WINDOW_SCOPE: Any
DEFAULT_SCOPE = VIEW_SCOPE
LOBBY_SUB_SCOPE: Any
LOBBY_TOP_SUB_SCOPE: Any
WINDOW_VIEWED_MULTISCOPE: Any
VIEW_TYPES_TO_SCOPES: dict

class SCOPE_TYPE(object):
    GLOBAL = 'global'
    DYNAMIC = 'dynamic'
    VIEW = WindowLayer.VIEW
    LOBBY_SUB = WindowLayer.SUB_VIEW
    LOBBY_TOP_SUB = WindowLayer.TOP_SUB_VIEW
    DEFAULT = VIEW
    WINDOW = WindowLayer.WINDOW
    TOP_WINDOW = WindowLayer.TOP_WINDOW
    FULLSCREEN = WindowLayer.FULLSCREEN_WINDOW
    WAITING = WindowLayer.WAITING
    WINDOW_VIEWED_MULTISCOPE = 'WindowViewed'

class SimpleScope(object):
    __slots__: tuple
    __scopeType: Any
    __parentScope: Any
    __dependencedScopes: Any
    def __init__(self, scopeType, parentScope):
        ...
    def __repr__(self):
        ...
    def _setParentScope(self, parentScope):
        ...
    def getScopeType(self):
        ...
    def isInScope(self, scopeType):
        ...
    def getRecommendedScopeData(self, currentScope):
        ...
    def addDependencedScope(self, simpleScope):
        ...
    def isOwnerFor(self, scope):
        ...
    def searchOwnersFor(self, scope):
        ...

class MultipleScope(SimpleScope):
    def __init__(self, scopeType, parentScopes):
        ...

class GlobalScope(SimpleScope):
    def __init__(self, scopeType):
        ...
    def getRecommendedScopeData(self, currentScope):
        ...
