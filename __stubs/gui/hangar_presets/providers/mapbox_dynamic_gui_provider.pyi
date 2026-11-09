# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/mapbox_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import MapboxPresetsGetter as MapboxPresetsGetter
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from gui.impl.lobby.missions.missions_helpers import MapboxMissionsGuiHelper as MapboxMissionsGuiHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import MapboxLobbyHeaderHelper as MapboxLobbyHeaderHelper

class MapboxHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.MAPBOX
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = MapboxLobbyHeaderHelper
    _MISSIONS_HELPER = MapboxMissionsGuiHelper
    _PRESETS_GETTER = MapboxPresetsGetter
