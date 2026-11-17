# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/flash_wrapper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import weakref as weakref
from collections import defaultdict as defaultdict
import GUI as GUI
from gui.Scaleform import SCALEFORM_SWF_PATH_V3 as SCALEFORM_SWF_PATH_V3
_logger: Any
_DEFAULT_FLASH_COMPONENT_CLASS = 'Flash'

class InputKeyMode(object):
    DEFAULT = 0
    IGNORE_RESULT = 1
    NO_HANDLE = 2

class FlashComponentWrapper(object):
    __exCbs: Any
    __component: Any
    __flashSize: Any
    __isActive: Any
    __isVisible: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def component(self):
        ...
    @property
    def movie(self):
        ...
    @property
    def moviePath(self):
        ...
    @property
    def movieUid(self):
        ...
    def isVisible(self):
        ...
    def setVisible(self, visible):
        ...
    def afterCreate(self):
        ...
    def beforeDelete(self):
        ...
    def createComponent(self, swf='', className=..., args=None, path=..., **kwargs):
        ...
    def active(self, state):
        ...
    def close(self):
        ...
    def getMember(self, path):
        ...
    def addExternalCallback(self, command, function):
        ...
    def removeExternalCallback(self, command, function=None):
        ...
    def addExternalCallbacks(self, commands):
        ...
    def removeExternalCallbacks(self, *args):
        ...
    def removeAllCallbacks(self):
        ...
    def handleExternalInterfaceCallback(self, command, args):
        ...
    def __doActivate(self, flag):
        ...

class Flash(FlashComponentWrapper):
    def __init__(self, swf='', className='Flash', args=None, path=...):
        ...

class _ExternalInterfaceObj(object):
    __weakObj: Any
    def __init__(self, obj):
        ...
    def __call__(self, command, args):
        ...
