# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wotlda/easy_tank_equip_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import Optional as Optional
from gui.game_control.wotlda.loadout_model import BaseOptDeviceLoadoutModel as BaseOptDeviceLoadoutModel
from gui.game_control.wotlda.response import WotldaResponse as WotldaResponse
from wg_async import wg_await as wg_await, wg_async as wg_async
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType as SupportedWotldaLoadoutType, LAST_UPDATE_TIMESTAMP as LAST_UPDATE_TIMESTAMP
from gui.game_control.wotlda.loadout_model import baseOptDeviceLoadoutSchema as baseOptDeviceLoadoutSchema
from gui.game_control.wotlda.requester import WotldaRequester as WotldaRequester
from gui.game_control.wotlda.cache import EasyTankEquipCache as EasyTankEquipCache
_logger: Any

class _EasyTankEquipProvider(object):
    _loadoutType: Any
    _requester: Any
    _cache: Any
    _isInitialized: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def clear(self):
        ...
    # decorador original: @wg_async
    def updateCacheData(self):
        ...
    def getLoadoutByVehicleID(self, vehicleID):
        ...
