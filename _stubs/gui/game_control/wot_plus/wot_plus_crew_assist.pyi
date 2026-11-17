# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/wot_plus_crew_assist.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewvalues as viewvalues
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.game_control.wotlda.cache import CrewCache as CrewCache
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_bus import SharedEvent as SharedEvent
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IWotPlusController as IWotPlusController
from typing import Tuple as Tuple, Dict as Dict, Optional as Optional
_logger: Any

class CrewAssistantCtrl(object):
    CREW_ASSIST_DATA_CHANGED = 'crewAssistDataChanged'
    _wotPlusCtrl: Any
    _platoonCtrl: Any
    _SUPPORTED_PREBATTLE_TYPES: list
    __isEnabled: Any
    _cache: Any
    def __init__(self):
        ...
    @property
    def remoteClientCacheUpdatedAt(self):
        ...
    def deleteClientCacheFile(self):
        ...
    def destroy(self):
        ...
    def fillLoadouts(self, loadouts):
        ...
    def heatCache(self):
        ...
    def start(self):
        ...
    def refresh(self):
        ...
    def isEnabled(self):
        ...
    def hasOrderSets(self, vehIntCD, tankmanRole):
        ...
    def validateOrderSets(self, orderSets):
        ...
    def getOrderSets(self, vehIntCD, tankmanRole):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _formEmptyResponse(self):
        ...
