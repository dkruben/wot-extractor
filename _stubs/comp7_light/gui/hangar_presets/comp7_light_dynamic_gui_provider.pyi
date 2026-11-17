# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/hangar_presets/comp7_light_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7_light.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import Comp7LightLobbyHeaderHelper as Comp7LightLobbyHeaderHelper
from comp7_light.gui.impl.lobby.missions.missions_helpers import Comp7LightMissionsGuiHelper as Comp7LightMissionsGuiHelper
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider

class Comp7LightHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.COMP7_LIGHT
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = Comp7LightLobbyHeaderHelper
    _MISSIONS_HELPER = Comp7LightMissionsGuiHelper
