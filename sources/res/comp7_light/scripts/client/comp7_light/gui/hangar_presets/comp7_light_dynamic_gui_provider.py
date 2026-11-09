# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/hangar_presets/comp7_light_dynamic_gui_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/hangar_presets/comp7_light_dynamic_gui_provider.py
from __future__ import absolute_import
from comp7_light.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import Comp7LightLobbyHeaderHelper
from comp7_light.gui.impl.lobby.missions.missions_helpers import Comp7LightMissionsGuiHelper
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider

class Comp7LightHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.COMP7_LIGHT
    _BONUS_TYPES = (ARENA_BONUS_TYPE.COMP7_LIGHT,)
    _LOBBY_HEADER_HELPER = Comp7LightLobbyHeaderHelper
    _MISSIONS_HELPER = Comp7LightMissionsGuiHelper
