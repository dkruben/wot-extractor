# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/processors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
from adisp import adisp_async as adisp_async
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.processors import Processor as Processor, plugins as plugins, makeError as makeError
from gui.shared.gui_items.processors.plugins import MessageConfirmator as MessageConfirmator, SyncValidator as SyncValidator
from helpers import dependency as dependency
from resource_well.gui.feature.constants import UNAVAILABLE_REWARD_ERROR as UNAVAILABLE_REWARD_ERROR, PurchaseMode as PurchaseMode
from resource_well.gui.feature.resource import processLoadingResources as processLoadingResources, splitResourcesByType as splitResourcesByType, mergeResources as mergeResources
from resource_well.gui.shared.event_dispatcher import showResourcesLoadingConfirm as showResourcesLoadingConfirm, showNextSerialVehiclesConfirm as showNextSerialVehiclesConfirm
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController
from wg_async import wg_async as wg_async, wg_await as wg_await
_RESOURCE_WELL_MESSAGES = R.strings.system_messages.resourceWell

class _ResourceLoadingConfirmator(MessageConfirmator):
    __rewardID: Any
    __resources: Any
    __isReturnOperation: Any
    def __init__(self, rewardID, resources, isReturnOperation):
        ...
    def _gfMakeMeta(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @wg_async
    def _confirm(self, callback):
        ...

class ResourceWellTakeBackProcessor(Processor):
    __resourceWell: Any
    __rewardID: Any
    def __init__(self, rewardID):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class _PutRewardValidator(SyncValidator):
    __resourceWell: Any
    __rewardID: Any
    def __init__(self, rewardID):
        ...
    def _validate(self):
        ...

class _BasePutResourcesProcessor(Processor):
    __resourceWell: Any
    __rewardID: Any
    __resources: Any
    def __init__(self, rewardID, resources, additionalPlugins):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class PutResourcesProcessor(_BasePutResourcesProcessor):
    def __init__(self, rewardID, resources):
        ...

class _NextSerialVehicleConfirmator(MessageConfirmator):
    __rewardID: Any
    def __init__(self, rewardID):
        ...
    def _gfMakeMeta(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @wg_async
    def _confirm(self, callback):
        ...

class NextSerialVehicleProcessor(_BasePutResourcesProcessor):
    __resourceWell: Any
    def __init__(self, rewardID, resources):
        ...
