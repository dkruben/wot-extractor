# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/number_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from builtins import str as str
from Event import Event as Event
from gui.game_control.reactive_comm import Subscription as Subscription
from helpers import dependency as dependency
from resource_well.gui.feature.resource_well_helpers import getNumberChannelName as getNumberChannelName
from skeletons.gui.game_control import IReactiveCommunicationService as IReactiveCommunicationService
from wg_async import AsyncSemaphore as AsyncSemaphore, wg_async as wg_async, wg_await as wg_await, BrokenPromiseError as BrokenPromiseError
from typing import Optional as Optional
_logger: Any
_NO_VEHICLES_VALUE = 0

class ResourceWellNumberRequester(object):
    __reactiveCommunication: Any
    onUpdated: Any
    __rewardID: Any
    __subscription: Any
    __remainingValues: Any
    __givenValues: Any
    __initialValues: Any
    __isActive: Any
    __semaphore: Any
    def __init__(self, rewardID, semaphore):
        ...
    @property
    def isActive(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def clear(self):
        ...
    def setInitialValues(self, initialValues):
        ...
    def getValuesLeft(self):
        ...
    def getRemainingValues(self):
        ...
    def getGivenValues(self):
        ...
    def isDataAvailable(self):
        ...
    # decorador original: @wg_async
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onMessage(self, message):
        ...
    def __onClosed(self, *_):
        ...
    def __getChannelName(self):
        ...
