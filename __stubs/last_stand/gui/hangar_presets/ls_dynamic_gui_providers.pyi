# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/hangar_presets/ls_dynamic_gui_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from last_stand.gui.impl.lobby.vehicle_menu_helper import LSHangarVehicleMenuHelper as LSHangarVehicleMenuHelper
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from last_stand.gui.scaleform.daapi.view.lobby.header.helpers.controls_helpers import LSLobbyHeaderHelper as LSLobbyHeaderHelper
from last_stand.gui.prb_control import LSVehicleAutoSearchHelper as LSVehicleAutoSearchHelper

class LSHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.LAST_STAND
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = LSLobbyHeaderHelper
    _VEHICLE_MENU_HELPER = LSHangarVehicleMenuHelper
    _VEHICLE_AUTO_SEARCH_HELPER = LSVehicleAutoSearchHelper

class LSMediumHangarDynamicGuiProvider(LSHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.LAST_STAND_MEDIUM
    _BONUS_TYPES: tuple

class LSHardHangarDynamicGuiProvider(LSHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.LAST_STAND_HARD
    _BONUS_TYPES: tuple
