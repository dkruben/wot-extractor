# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/windows_stored_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import functools as functools
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from gui.Scaleform.daapi.view.meta.WindowViewMeta import WindowViewMeta as WindowViewMeta
from gui.doc_loaders.WindowsStoredDataLoader import WindowsStoredDataLoader as WindowsStoredDataLoader
from math_common import round_py2_style_int as round_py2_style_int
from messenger.ext.channel_num_gen import isClientIDValid as isClientIDValid
from soft_exception import SoftException as SoftException
WindowGeometry: Any
_logger: Any
DEF_TARGET_MASK: Any
STORED_DATA_MAX_LENGTH = 64
STORED_DATA_REV = 1
g_windowsStoredData: Any

class DATA_TYPE(object):
    UNIQUE_WINDOW = 1
    CAROUSEL_WINDOW = 2
    CHANNEL_WINDOW = 3
    RANGE: tuple

class TARGET_ID(object):
    CHANNEL_CAROUSEL = 1
    CHAT_MANAGEMENT = 2
    ALL: Any

class stored_window(object):
    __dataType: Any
    __targetID: Any
    __sideEffect: Any
    def __init__(self, dataType, targetID, sideEffect=None):
        ...
    def __call__(self, clazz):
        ...

class WindowStoredData(object):
    __slots__: tuple
    _trusted: Any
    _geometry: Any
    def __init__(self, *args):
        ...
    @classmethod
    def make(cls, window):
        ...
    @classmethod
    def getDataType(cls):
        ...
    def pack(self):
        ...
    def getFindCriteria(self):
        ...
    def isRequiredWindow(self, window):
        ...
    def isTrusted(self):
        ...
    def setTrusted(self, value):
        ...
    def getGeometry(self):
        ...
    def setGeometry(self, value):
        ...

class UniqueWindowStoredData(WindowStoredData):
    __slots__: tuple
    _uniqueName: Any
    _trusted: Any
    def __init__(self, name, *args):
        ...
    def __repr__(self):
        ...
    @classmethod
    def make(cls, window):
        ...
    @classmethod
    def getDataType(cls):
        ...
    def pack(self):
        ...
    def getFindCriteria(self):
        ...
    def isRequiredWindow(self, window):
        ...

class CarouselWindowStoredData(WindowStoredData):
    __slots__: tuple
    _clientID: Any
    _trusted: Any
    def __init__(self, clientID, *args):
        ...
    def __repr__(self):
        ...
    @classmethod
    def make(cls, window):
        ...
    @classmethod
    def getDataType(cls):
        ...
    def pack(self):
        ...
    def getFindCriteria(self):
        ...
    def isRequiredWindow(self, window):
        ...

class ChannelWindowStoredData(WindowStoredData):
    __slots__: tuple
    _protoType: Any
    _channelID: Any
    _trusted: Any
    def __init__(self, protoType, channelID, *args):
        ...
    def __repr__(self):
        ...
    @classmethod
    def make(cls, window):
        ...
    @classmethod
    def getDataType(cls):
        ...
    def pack(self):
        ...
    def getFindCriteria(self):
        ...
    def isRequiredWindow(self, window):
        ...

class _WindowsStoredDataManager(object):
    __storedData: Any
    __targetMask: Any
    __loader: Any
    __supported: Any
    __trustedCriteria: Any
    __isStarted: Any
    def __init__(self, supported):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isTargetEnabled(self, targetID):
        ...
    def addTarget(self, targetID):
        ...
    def removeTarget(self, targetID):
        ...
    def addData(self, targetID, dataType, window):
        ...
    def getData(self, targetID, window):
        ...
    def getMap(self, targetID, dataType):
        ...
    def setTrustedCriteria(self, targetID, criteria):
        ...

def _populateStoredData(targetID, window):
    ...
def _updateStoredData(targetID, dataType, pyWindow):
    ...
