# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS

# decorador original: @ReprInjector.simple(...)
class RequestResultsContext(object):
    __slots__: tuple
    __arenaUniqueID: Any
    __arenaBonusType: Any
    __showImmediately: Any
    __showIfPosted: Any
    __resetCache: Any
    def __init__(self, arenaUniqueID, arenaBonusType=..., showImmediately=True, showIfPosted=False, resetCache=False):
        ...
    def getArenaUniqueID(self):
        ...
    def getArenaBonusType(self):
        ...
    def needToShowImmediately(self):
        ...
    def needToShowIfPosted(self):
        ...
    def resetCache(self):
        ...

# decorador original: @ReprInjector.simple(...)
class RequestEmblemContext(object):
    __slots__: tuple
    __emblemType: Any
    __formationDBID: Any
    __textureID: Any
    def __init__(self, emblemType, formationDBID, textureID=0):
        ...
    def getEmblemType(self):
        ...
    def getFormationDBID(self):
        ...
    def getTextureID(self):
        ...
    def getUniqueID(self):
        ...
