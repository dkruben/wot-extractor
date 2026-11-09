# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/hangar_presets/frontline_dynamic_gui_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/hangar_presets/frontline_dynamic_gui_provider.py
from __future__ import absolute_import
from constants import QUEUE_TYPE, ARENA_BONUS_TYPE
from frontline.gui.impl.lobby.missions.missions_helpers import FrontlineMissionsGuiHelper
from frontline.gui.Scaleform.daapi.view.lobby.hangar.hangar_quest_flags import EpicQuestFlagsGetter
from frontline.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import FrontlineLobbyHeaderHelper
from frontline.gui.impl.lobby.presenters.frontline_vehicle_menu_helper import FrontlineHangarVehicleMenuHelper
from gui.hangar_presets.obsolete.hangar_presets_getters import DefaultPresetsGetter
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider
from gui.impl.lobby.hangar.base.vehicle_playlists_helper import RandomVehiclePlaylistsGuiHelper
from gui.impl.lobby.tank_setup.frontline.ammunition_setup import FrontlineAmmunitionSetupView
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class FrontlinePresetsGetter(DefaultPresetsGetter):
    _QUEST_FLAGS_GETTER = EpicQuestFlagsGetter
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def getHangarAlertBlock(self):
        return self.__epicController.getAlertBlock()

    def getAmmoSetupViewAlias(self):
        return FrontlineAmmunitionSetupView.__name__


class FrontlineHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.EPIC
    _BONUS_TYPES = (ARENA_BONUS_TYPE.EPIC_BATTLE, ARENA_BONUS_TYPE.EPIC_BATTLE_TRAINING)
    _LOBBY_HEADER_HELPER = FrontlineLobbyHeaderHelper
    _MISSIONS_HELPER = FrontlineMissionsGuiHelper
    _PRESETS_GETTER = FrontlinePresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper
    _VEHICLE_MENU_HELPER = FrontlineHangarVehicleMenuHelper
