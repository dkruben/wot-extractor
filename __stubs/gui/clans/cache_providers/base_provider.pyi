# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/cache_providers/base_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from abc import ABCMeta as ABCMeta, abstractmethod as abstractmethod, abstractproperty as abstractproperty
from collections import defaultdict as defaultdict
import typing as typing
from enum import Enum as Enum
from typing import Dict as Dict, Optional as Optional, NamedTuple as NamedTuple
import Event as Event
from adisp import adisp_process as adisp_process
from data_structures import DictObj as DictObj
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.requests import WgcgRequestResponse as WgcgRequestResponse
from gui.wgcg.states import WebControllerStates as WebControllerStates
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.web import IWebController as IWebController
from typing import DefaultDict as DefaultDict
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
_logger: Any
RequestSettings: Any

class UpdatePeriodType(Enum):
    BY_TIME = 'BY_TIME'
    AFTER_BATTLE = 'AFTER_BATTLE'
    NONE = 'NONE'

class IBaseProvider(object):
    def start(self):
        ...
    def stop(self, withClear=False):
        ...

class BaseProvider(IBaseProvider, metaclass=ABCMeta):
    __webController: Any
    _eManager: Any
    onDataReceived: Any
    onDataFailed: Any
    __isStarted: Any
    __data: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self, withClear=False):
        ...
    @abstractproperty
    def _isEnabled(self):
        ...
    @abstractproperty
    def _dataNameContainer(self):
        ...
    @property
    def _fakeDataStorage(self):
        ...
    @abstractmethod
    def _getSettings(self):
        ...
    def _dataReceived(self, dataName, data):
        ...
    def _getData(self, dataName, useFake=False):
        ...
    # decorador original: @adisp_process
    def _requestData(self, dataName, useFake=False):
        ...
    def _getSettingsByDataName(self, dataName):
        ...
    def _updateDataCache(self, dataName, updater):
        ...
    @staticmethod
    def __isRequestingAvailable(settings, dataObj):
        ...
