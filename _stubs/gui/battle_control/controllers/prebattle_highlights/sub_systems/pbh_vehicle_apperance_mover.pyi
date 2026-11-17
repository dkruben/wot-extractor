# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/pbh_vehicle_apperance_mover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from copy import copy as copy
import typing as typing
import BigWorld as BigWorld
from CGF import TransformComponent as TransformComponent
from gui.battle_control.controllers.prebattle_highlights.pbh_helpers import getPointTransformComponent as getPointTransformComponent
from gui.battle_control.controllers.prebattle_highlights.sub_systems.base_sub_system import BasePbhSubSystem as BasePbhSubSystem
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from wg_async import AsyncScope as AsyncScope, AsyncEvent as AsyncEvent, wg_await as wg_await, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, AsyncReturn as AsyncReturn
from typing import Optional as Optional, List as List, Dict as Dict
from skeletons.gui.battle_session import IBattleContext as IBattleContext
_logger: Any

class PbhVehicleAppearanceMover(BasePbhSubSystem):
    __sessionProvider: Any
    __winnersGetter: Any
    __sizeGetter: Any
    __onVehiclesDataReadyEvent: Any
    __presentingVehiclesData: Any
    __originalMatrixProviders: Any
    __vehicleEntities: Any
    __startCallbackID: Any
    __vehiclesWaitingCallbackID: Any
    __scope: Any
    __event: Any
    def __init__(self, readyCallback, winnersGetter, sizeGetter, onVehiclesDataReadyEvent):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def isReady(self):
        ...
    def startFlow(self):
        ...
    def stopFlow(self):
        ...
    def clear(self):
        ...
    def getPresentingVehiclesData(self):
        ...
    # decorador original: @wg_async
    def historicalOutfitCompliance(self, level):
        ...
    def _vehiclesWaiter(self):
        ...
    def __getVehicleEntities(self):
        ...
    def __moveVehicles(self):
        ...
    def __resetVehiclePositions(self):
        ...
