# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/random_dynamic_gui_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import RandomPresetsGetter as RandomPresetsGetter
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from gui.impl.lobby.hangar.base.vehicle_playlists_helper import RandomVehiclePlaylistsGuiHelper as RandomVehiclePlaylistsGuiHelper
from gui.impl.lobby.missions.missions_helpers import RandomMissionsGuiHelper as RandomMissionsGuiHelper, RandomNP2MissionsGuiHelper as RandomNP2MissionsGuiHelper, WinbackMissionsGuiHelper as WinbackMissionsGuiHelper

class RandomHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.RANDOMS
    _BONUS_TYPES: tuple
    _MISSIONS_HELPER = RandomMissionsGuiHelper
    _PRESETS_GETTER = RandomPresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper

class WinbackHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.WINBACK
    _BONUS_TYPES: tuple
    _MISSIONS_HELPER = WinbackMissionsGuiHelper
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper

class RandomNP2HangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.RANDOM_NP2
    _BONUS_TYPES: tuple
    _MISSIONS_HELPER = RandomNP2MissionsGuiHelper
    _PRESETS_GETTER = RandomPresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper
