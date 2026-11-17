# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/hangar_presets/fort_rush_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fort_rush.gui.impl.lobby.user_missions.fort_rush_missions_helper import FortRushMissionsGuiHelper as FortRushMissionsGuiHelper
from fort_rush_common.fort_rush_constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from fort_rush.gui.scaleform.daapi.view.lobby.header.helpers.controls_helpers import FortRushLobbyHeaderHelper as FortRushLobbyHeaderHelper
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider

class FortRushHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.FORT_RUSH
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = FortRushLobbyHeaderHelper
    _MISSIONS_HELPER = FortRushMissionsGuiHelper
