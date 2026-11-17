# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/external_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
from gui.Scaleform.flash_wrapper import FlashComponentWrapper as FlashComponentWrapper
from gui.Scaleform.framework.application import DAAPIRootBridge as DAAPIRootBridge
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
ExternalFlashSettings: Any

class _ExternalComponentState(object):
    UNDEFINED = 0
    CREATED = 1
    CLOSED = 2
    REGISTERED = 4
    UNREGISTERED = 8
    INITED: Any
    DESTROYED: Any

class IExternalFlashComponent(object):
    def setOwner(self, owner):
        ...
    def close(self):
        ...

class ExternalFlashComponent(FlashComponentWrapper, IExternalFlashComponent):
    __settings: Any
    __owner: Any
    __state: Any
    __bridge: Any
    def __init__(self, settings):
        ...
    @property
    def alias(self):
        ...
    @property
    def owner(self):
        ...
    def createExternalComponent(self):
        ...
    def setOwner(self, owner):
        ...
    def close(self):
        ...
    def getSize(self):
        ...
    def setSize(self, width, height):
        ...
    def getScale(self):
        ...
    def setScale(self, scale):
        ...
    def startPlugins(self):
        ...
    def afterCreate(self):
        ...
    def invokeRegisterComponentForReplay(self):
        ...
    def __tryToInvokeRegisterEvent(self, step):
        ...
    def __invokeUnregisterEvent(self):
        ...
