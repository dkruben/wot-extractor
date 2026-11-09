# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/hangar_presets/hw_dynamic_gui_providers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/hangar_presets/hw_dynamic_gui_providers.py
from __future__ import absolute_import
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider
from halloween_common.halloween_constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from halloween.gui.scaleform.daapi.view.lobby.header.helpers.controls_helpers import HalloweenLobbyHeaderHelper

class HalloweenHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN
    _BONUS_TYPES = (ARENA_BONUS_TYPE.HALLOWEEN,)
    _LOBBY_HEADER_HELPER = HalloweenLobbyHeaderHelper


class HalloweenMediumHangarDynamicGuiProvider(HalloweenHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN_MEDIUM
    _BONUS_TYPES = (ARENA_BONUS_TYPE.HALLOWEEN_MEDIUM,)


class HalloweenHardHangarDynamicGuiProvider(HalloweenHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.HALLOWEEN_HARD
    _BONUS_TYPES = (ARENA_BONUS_TYPE.HALLOWEEN_HARD,)
