# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/stronghold_event_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
from collections import defaultdict as defaultdict
import typing as typing
import Event as Event
import wg_async as wg_async
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled as getStrongholdEventEnabled
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.game_control.reactive_comm import Subscription as Subscription
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IReactiveCommunicationService as IReactiveCommunicationService
_logger: Any

class FrozenVehiclesConstants(CONST_CONTAINER):
    ALL_VEHICLES_FROZEN = 'ALL_VEHICLES_FROZEN'
    E_VEHICLE_FREEZE = 'vehicle_freeze'
    E_VEHICLE_FREEZE_ALL = 'vehicle_freeze_all'
    E_VEHICLE_UNFREEZE = 'vehicle_unfreeze'
    E_VEHICLE_UNFREEZE_ALL = 'vehicle_unfreeze_all'
    E_SPARE_PARTS_CHANGED = 'spare_parts_changed'

class FrozenVehiclesRequester(object):
    __slots__: tuple
    __RCService: Any
    __cache: Any
    __isStarted: Any
    __subscription: Any
    __eventsManager: Any
    onUpdated: Any
    def __init__(self):
        ...
    @property
    def isStarted(self):
        ...
    @property
    def canStart(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getCache(self):
        ...
    def getSparePartsBalance(self):
        ...
    def getFrozenVehicles(self, spaID):
        ...
    def getUnfreezePrice(self, vehicleCD):
        ...
    def isCacheEmpty(self):
        ...
    def removeFromFrozenVehicle(self, playerSpaID, vehicleCD):
        ...
    def setInitialDataAndStart(self, data):
        ...
    def _onMessage(self, message):
        ...
    def __onClosed(self, reason):
        ...
    # decorador original: @wg_async.wg_async
    def __subscribe(self):
        ...
    def __clearSubscription(self):
        ...
    @staticmethod
    def __getChannelName():
        ...
    @staticmethod
    def __defaultCache():
        ...
