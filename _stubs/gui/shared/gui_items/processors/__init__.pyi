# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import logging as logging
import typing as typing
from builtins import zip as zip
from collections import namedtuple as namedtuple
import AccountCommands as AccountCommands
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE as SM_TYPE, ResultMsg as ResultMsg
from gui.shared.gui_items.processors import plugins as proc_plugs
from gui.shared.utils import code2str as code2str
from helpers import dependency as dependency
from helpers import i18n as i18n
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

# base nao representavel no stub: namedtuple(...)
class GroupedServerResponse:
    def __new__(cls, *args, **kwargs):
        ...

class Processor(object):
    itemsCache: Any
    PLUGIN_RES_CODE = -33
    SILENCED_FAILS: tuple
    plugins: Any
    requestCtx: Any
    responseCtx: Any
    def __init__(self, plugins=None):
        ...
    def getPluginsByType(self, pluginType):
        ...
    def addPlugin(self, plugin):
        ...
    def addPlugins(self, plugins):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __validate(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __confirm(self, callback):
        ...
    def _request(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def request(self, callback=None):
        ...
    def _getResCodeHandler(self, code, baseHandler):
        ...
    def _lockedVehicleHandler(self):
        ...

class ItemProcessor(Processor):
    item: Any
    def __init__(self, item, plugins=None):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...

class GroupedRequestProcessor(Processor):
    __request: Any
    __params: Any
    __groupID: Any
    __groupSize: Any
    def __init__(self, request, *args, **kwargs):
        ...
    def _request(self, callback):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...
    def _makeSuccessData(self, *args, **kwargs):
        ...
    def _makeErrorData(self, *args, **kwargs):
        ...
    def _lockedVehicleHandler(self):
        ...

class VehicleItemProcessor(ItemProcessor):
    vehicle: Any
    allowableTypes: Any
    def __init__(self, vehicle, module, allowableTypes):
        ...

def makeSuccess(userMsg='', msgType=..., auxData=None, msgData=None, msgPriority=None):
    ...
def makeError(userMsg='', msgType=..., auxData=None, msgData=None, msgPriority=None):
    ...
def makeI18nSuccess(sysMsgKey='', auxData=None, *args, **kwargs):
    ...
def makeI18nError(sysMsgKey='', defaultSysMsgKey='', auxData=None, *args, **kwargs):
    ...
