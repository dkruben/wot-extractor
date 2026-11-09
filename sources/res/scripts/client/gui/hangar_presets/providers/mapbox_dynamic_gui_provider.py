# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_presets/providers/mapbox_dynamic_gui_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/providers/mapbox_dynamic_gui_provider.py
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import MapboxPresetsGetter
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider
from gui.impl.lobby.missions.missions_helpers import MapboxMissionsGuiHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import MapboxLobbyHeaderHelper

class MapboxHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.MAPBOX
    _BONUS_TYPES = (ARENA_BONUS_TYPE.MAPBOX,)
    _LOBBY_HEADER_HELPER = MapboxLobbyHeaderHelper
    _MISSIONS_HELPER = MapboxMissionsGuiHelper
    _PRESETS_GETTER = MapboxPresetsGetter
