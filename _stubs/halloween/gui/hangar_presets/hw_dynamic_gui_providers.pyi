# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/hangar_presets/hw_dynamic_gui_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from halloween.gui.scaleform.daapi.view.lobby.header.helpers.controls_helpers import HalloweenLobbyHeaderHelper as HalloweenLobbyHeaderHelper

class HalloweenHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = HalloweenLobbyHeaderHelper

class HalloweenMediumHangarDynamicGuiProvider(HalloweenHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN_MEDIUM
    _BONUS_TYPES: tuple

class HalloweenHardHangarDynamicGuiProvider(HalloweenHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN_HARD
    _BONUS_TYPES: tuple
