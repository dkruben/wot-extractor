# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/special_mode/pre_queue/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.prb_control.entities.base import vehicleAmmoCheck as vehicleAmmoCheck
from gui.prb_control.entities.base.pre_queue.entity import PreQueueEntity as PreQueueEntity, PreQueueSubscriber as PreQueueSubscriber, PreQueueEntryPoint as PreQueueEntryPoint
from gui.prb_control.entities.special_mode.pre_queue.ctx import SpecialModeQueueCtx as SpecialModeQueueCtx
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class SpecialModeSubscriber(PreQueueSubscriber):
    def subscribe(self, entity):
        ...
    def unsubscribe(self, entity):
        ...

class SpecialModeEntryPoint(PreQueueEntryPoint):
    def _getFilterStates(self):
        ...

class SpecialModeEntity(PreQueueEntity):
    settingsCore: Any
    _watcherClass: Any
    __watcher: Any
    def __init__(self, modeFlags, queueType, subscriber, watcherClass):
        ...
    @property
    def storage(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def leave(self, ctx, callback=None):
        ...
    # decorador original: @vehicleAmmoCheck
    def queue(self, ctx, callback=None):
        ...
    def _makeQueueCtxByAction(self, action=None):
        ...
    def _goToQueueUI(self):
        ...
    def _exitFromQueueUI(self):
        ...
    def _isNeedToShowWelcome(self):
        ...
    def _showWelcomeGui(self):
        ...
    def __processWelcome(self):
        ...
