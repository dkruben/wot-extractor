# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/contexts/cgf_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from constants import IS_CELLAPP as IS_CELLAPP, IS_CLIENT as IS_CLIENT
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.context import VScriptContext as VScriptContext, vse_get_property as vse_get_property, vse_event_out as vse_event_out
from visual_script.dependency import dependencyImporter as dependencyImporter
helpers: Any

class GameObjectWrapper(object):
    go: Any
    def __init__(self, go):
        ...

class CGFGameObjectContext(VScriptContext):
    gameObject: Any
    __arena: Any
    def __init__(self, gameObject, aspect):
        ...
    # decorador original: @vse_get_property(...)
    def getSelf(self):
        ...
    # decorador original: @vse_get_property(...)
    def getArena(self):
        ...
    # decorador original: @vse_event_out(...)
    def onGameObjectClick(self):
        ...
    # decorador original: @vse_event_out(...)
    def onGameObjectHoverIn(self):
        ...
    # decorador original: @vse_event_out(...)
    def onGameObjectHoverOut(self):
        ...
    # decorador original: @vse_event_out(...)
    def onTriggerEvent(self, eventName):
        ...

def getCurrentAspect():
    ...
def createContext(go):
    ...
def getPlanTags():
    ...
