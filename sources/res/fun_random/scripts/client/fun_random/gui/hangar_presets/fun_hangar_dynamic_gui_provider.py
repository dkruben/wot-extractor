# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/hangar_presets/fun_hangar_dynamic_gui_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/hangar_presets/fun_hangar_dynamic_gui_provider.py
from __future__ import absolute_import
from fun_random_common.fun_constants import ARENA_BONUS_TYPE
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import FunRandomLobbyHeaderHelper
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_vehicle_menu_helper import FunRandomHangarVehicleMenuHelper
from gui.hangar_presets.providers.base_dynamic_gui_provider import BaseHangarDynamicGuiProvider
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper

class FunRandomHangarDynamicGuiProvider(BaseHangarDynamicGuiProvider, FunSubModesWatcher):
    _BONUS_TYPES = (
     ARENA_BONUS_TYPE.FUN_RANDOM,)
    _LOBBY_HEADER_HELPER = FunRandomLobbyHeaderHelper
    _MISSIONS_HELPER = DefaultMissionsGuiHelper
    _VEHICLE_MENU_HELPER = FunRandomHangarVehicleMenuHelper

    @hasDesiredSubMode(abortAction='getDefaultBattleModifiers')
    def getBattleModifiers(self):
        return self.getDesiredSubMode().getModifiersDataProvider().getModifiers()
