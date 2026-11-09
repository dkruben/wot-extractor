# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/wot_plus_assistant.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.game_control.wot_plus.wot_plus_crew_assist import CrewAssistantCtrl as CrewAssistantCtrl
from gui.game_control.wot_plus.wot_plus_opt_device_assist import OptionalDevicesAssistantCtrl as OptionalDevicesAssistantCtrl
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType as SupportedWotldaLoadoutType, LAST_UPDATE_TIMESTAMP as LAST_UPDATE_TIMESTAMP
from gui.game_control.wotlda.requester import WotldaRequester as WotldaRequester
from gui.game_control.wotlda.response import WotldaResponse as WotldaResponse
from typing import Set as Set
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
_logger: Any

class WotPlusAssistant(object):
    _LOADOUT_TYPES_TO_REQUEST: set
    _optDeviceAssistant: Any
    _crewAssistant: Any
    _requester: Any
    _isStarted: Any
    _loadoutsObtained: Any
    _waitingForResponse: Any
    def __init__(self):
        ...
    @classmethod
    def addLoadoutType(cls, loadoutType):
        ...
    @property
    def optDeviceAssistant(self):
        ...
    @property
    def crewAssistant(self):
        ...
    def start(self):
        ...
    def heatCache(self):
        ...
    def clear(self):
        ...
    def clearWithCacheDelete(self):
        ...
    # decorador original: @wg_async.wg_async
    def subscriptionValidated(self):
        ...
    # decorador original: @wg_async.wg_async
    def _fetchLoadouts(self, loadoutTypes):
        ...
    def destroy(self):
        ...

def registerAllowedPrebattleType(prbType, loadoutType):
    ...
