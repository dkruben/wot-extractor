# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/default_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import DefaultPresetsGetter as DefaultPresetsGetter
from gui.hangar_presets.providers.base_dynamic_gui_provider import BaseHangarDynamicGuiProvider as BaseHangarDynamicGuiProvider
from gui.impl.lobby.hangar.base.vehicle_playlists_helper import DefaultVehiclePlaylistsGuiHelper as DefaultVehiclePlaylistsGuiHelper
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.vehicle_menu_helper import DefaultHangarVehicleMenuHelper as DefaultHangarVehicleMenuHelper
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper as DefaultMissionsGuiHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.prb_control.prb_helpers import DefaultVehicleAutoSearchHelper as DefaultVehicleAutoSearchHelper

class DefaultHangarDynamicGuiProvider(BaseHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.UNKNOWN
    _LOBBY_HEADER_HELPER = DefaultLobbyHeaderHelper
    _MISSIONS_HELPER = DefaultMissionsGuiHelper
    _PRESETS_GETTER = DefaultPresetsGetter
    _VEHICLE_MENU_HELPER = DefaultHangarVehicleMenuHelper
    _VEHICLE_PLAYLISTS_HELPER = DefaultVehiclePlaylistsGuiHelper
    _VEHICLE_AUTO_SEARCH_HELPER = DefaultVehicleAutoSearchHelper
    _presetGetter: Any
    def __init__(self, config):
        ...
    def getPresetsGetter(self):
        ...
