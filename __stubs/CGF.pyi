# wot-extractor: STUB do modulo 'CGF', SEM CODIGO no cliente (nativo do motor, em C++, ou ausente).
# So lista os membros que o codigo Python usa (207 ficheiro(s)); assinaturas e tipos sao
# desconhecidos (*args/**kwargs e Any). Os comentarios dizem como cada membro e usado.

from typing import Any

def AccessReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 132x com 1-3 argumentos posicionais
def ActivateReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 140x com 1-25 argumentos posicionais
ActiveOnly: Any  # usado sem chamada 51x
CGF_COMPONENT_MARKER: Any  # usado sem chamada 1x
CGF_REPLICABLE_COMPONENT_MARKER: Any  # usado sem chamada 1x
def CommandQueue(*args: Any, **kwargs: Any) -> Any: ...  # chamado 137x com 1 argumento(s) posicional(is)
ComponentAccessor: Any  # usado sem chamada 4x
def ComponentLink(*args: Any, **kwargs: Any) -> Any: ...  # chamado 38x com 0-2 argumentos posicionais
def CreateReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 7x com 1-2 argumentos posicionais
def DeactivateReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 89x com 1-4 argumentos posicionais
Domain: Any  # usado sem chamada 248x
def DynamicComponentAccess(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)
GameObject: Any  # usado sem chamada 173x; importado com 'from CGF import' em 2 ficheiro(s)
def Has(*args: Any, **kwargs: Any) -> Any: ...  # chamado 12x com 1 argumento(s) posicional(is)
HierarchyComponent: Any  # usado sem chamada 27x; importado com 'from CGF import' em 1 ficheiro(s)
INVALID_UUID: Any  # usado sem chamada 8x
def IterateReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 52x com 2-6 argumentos posicionais
def No(*args: Any, **kwargs: Any) -> Any: ...  # chamado 3x com 1 argumento(s) posicional(is)
def OptRo(*args: Any, **kwargs: Any) -> Any: ...  # chamado 12x com 1 argumento(s) posicional(is)
def OptRw(*args: Any, **kwargs: Any) -> Any: ...  # chamado 26x com 1 argumento(s) posicional(is)
def PeriodicIterateReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 7-14 argumentos posicionais
PropertyType: Any  # usado sem chamada 435x
def ReactHas(*args: Any, **kwargs: Any) -> Any: ...  # chamado 15x com 1 argumento(s) posicional(is)
def ReactRo(*args: Any, **kwargs: Any) -> Any: ...  # chamado 82x com 1 argumento(s) posicional(is)
def ReactRw(*args: Any, **kwargs: Any) -> Any: ...  # chamado 166x com 1 argumento(s) posicional(is)
def Reactions(*args: Any, **kwargs: Any) -> Any: ...  # chamado 115x com 0-23 argumentos posicionais
def RegisterSystem(*args: Any, **kwargs: Any) -> Any: ...  # chamado 111x com 1-2 argumentos posicionais; keywords: domain, perTickUpdate, predicate, updateAfter, updateBefore, updatePeriod
def RemoveReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 3x com 1-2 argumentos posicionais
def Ro(*args: Any, **kwargs: Any) -> Any: ...  # chamado 96x com 1 argumento(s) posicional(is)
def Rw(*args: Any, **kwargs: Any) -> Any: ...  # chamado 162x com 1 argumento(s) posicional(is)
System: Any  # usado sem chamada 111x
TransformComponent: Any  # usado sem chamada 72x; importado com 'from CGF import' em 3 ficheiro(s)
TransformUpdateSystem: Any  # usado sem chamada 32x
def addNetworkEntity(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 3 argumento(s) posicional(is)
def cachePrefabs(*args: Any, **kwargs: Any) -> Any: ...  # chamado 5x com 1 argumento(s) posicional(is)
def cancelCreateRequest(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def createBoolLink(*args: Any, **kwargs: Any) -> Any: ...  # chamado 6x com 2 argumento(s) posicional(is)
def createFloatLink(*args: Any, **kwargs: Any) -> Any: ...  # chamado 10x com 2 argumento(s) posicional(is)
def findHierarchySingleton(*args: Any, **kwargs: Any) -> Any: ...  # chamado 5x com 1 argumento(s) posicional(is)
def findInHierarchyWithComponent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 6x com 2-3 argumentos posicionais; keywords: includingRoot
def findInHierarchyWithReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 2 argumento(s) posicional(is)
def findParentWithComponent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 6x com 2 argumento(s) posicional(is)
def findParentWithReaction(*args: Any, **kwargs: Any) -> Any: ...  # chamado 21x com 2 argumento(s) posicional(is)
def findSingleton(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 2 argumento(s) posicional(is)
def gameObject(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def getSystem(*args: Any, **kwargs: Any) -> Any: ...  # chamado 35x com 2 argumento(s) posicional(is)
def linkMatrixTranslation(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 1 argumento(s) posicional(is)
def loadAndCreatePrefab(*args: Any, **kwargs: Any) -> Any: ...  # chamado 18x com 3-4 argumentos posicionais
def loadAndCreatePrefabWithParent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 26x com 3-4 argumentos posicionais
def loadAndCreatePrefabWithParentUUID(*args: Any, **kwargs: Any) -> Any: ...  # chamado 3x com 5 argumento(s) posicional(is)
def loadGameObjectIntoHierarchy(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 3 argumento(s) posicional(is)
def postEvent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 16x com 2 argumento(s) posicional(is)
def registerComponent(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 8 argumento(s) posicional(is)
def registerModule(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 1 argumento(s) posicional(is)
def registerModulePath(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def removeGameObject(*args: Any, **kwargs: Any) -> Any: ...  # chamado 9x com 1 argumento(s) posicional(is)
def removeNetworkEntity(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s) posicional(is)
def removePrefabsFromCache(*args: Any, **kwargs: Any) -> Any: ...  # chamado 4x com 1 argumento(s) posicional(is)
def resetLink(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 1 argumento(s) posicional(is)
def setLinkObject(*args: Any, **kwargs: Any) -> Any: ...  # chamado 2x com 2 argumento(s) posicional(is)

def __getattr__(name: str) -> Any: ...  # outros membros nao observados
