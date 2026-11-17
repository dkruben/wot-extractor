# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/event_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import EventLobbyHeaderHelper as EventLobbyHeaderHelper
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider

class EventHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.EVENT_BATTLES
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = EventLobbyHeaderHelper
    def getLobbyHeaderHelper(self):
        ...
