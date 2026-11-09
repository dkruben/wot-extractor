# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_presets/providers/random_dynamic_gui_providers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/providers/random_dynamic_gui_providers.py
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import RandomPresetsGetter
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider
from gui.impl.lobby.hangar.base.vehicle_playlists_helper import RandomVehiclePlaylistsGuiHelper
from gui.impl.lobby.missions.missions_helpers import RandomMissionsGuiHelper, RandomNP2MissionsGuiHelper, WinbackMissionsGuiHelper

class RandomHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.RANDOMS
    _BONUS_TYPES = (ARENA_BONUS_TYPE.REGULAR, ARENA_BONUS_TYPE.EPIC_RANDOM, ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING)
    _MISSIONS_HELPER = RandomMissionsGuiHelper
    _PRESETS_GETTER = RandomPresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper


class WinbackHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.WINBACK
    _BONUS_TYPES = (ARENA_BONUS_TYPE.WINBACK,)
    _MISSIONS_HELPER = WinbackMissionsGuiHelper
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper


class RandomNP2HangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.RANDOM_NP2
    _BONUS_TYPES = (ARENA_BONUS_TYPE.RANDOM_NP2,)
    _MISSIONS_HELPER = RandomNP2MissionsGuiHelper
    _PRESETS_GETTER = RandomPresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper
