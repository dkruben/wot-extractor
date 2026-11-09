# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/ranked_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import RankedPresetsGetter as RankedPresetsGetter
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import RankedLobbyHeaderHelper as RankedLobbyHeaderHelper

class RankedHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.RANKED
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = RankedLobbyHeaderHelper
    _PRESETS_GETTER = RankedPresetsGetter
