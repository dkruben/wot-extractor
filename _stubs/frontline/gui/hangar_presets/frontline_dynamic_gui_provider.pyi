# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/hangar_presets/frontline_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frontline.gui.impl.lobby.missions.missions_helpers import FrontlineMissionsGuiHelper as FrontlineMissionsGuiHelper
from frontline.gui.Scaleform.daapi.view.lobby.hangar.hangar_quest_flags import EpicQuestFlagsGetter as EpicQuestFlagsGetter
from frontline.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import FrontlineLobbyHeaderHelper as FrontlineLobbyHeaderHelper
from frontline.gui.impl.lobby.presenters.frontline_vehicle_menu_helper import FrontlineHangarVehicleMenuHelper as FrontlineHangarVehicleMenuHelper
from gui.hangar_presets.obsolete.hangar_presets_getters import DefaultPresetsGetter as DefaultPresetsGetter
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from gui.impl.lobby.hangar.base.vehicle_playlists_helper import RandomVehiclePlaylistsGuiHelper as RandomVehiclePlaylistsGuiHelper
from gui.impl.lobby.tank_setup.frontline.ammunition_setup import FrontlineAmmunitionSetupView as FrontlineAmmunitionSetupView
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class FrontlinePresetsGetter(DefaultPresetsGetter):
    _QUEST_FLAGS_GETTER = EpicQuestFlagsGetter
    __epicController: Any
    def getHangarAlertBlock(self):
        ...
    def getAmmoSetupViewAlias(self):
        ...

class FrontlineHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.EPIC
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = FrontlineLobbyHeaderHelper
    _MISSIONS_HELPER = FrontlineMissionsGuiHelper
    _PRESETS_GETTER = FrontlinePresetsGetter
    _VEHICLE_PLAYLISTS_HELPER = RandomVehiclePlaylistsGuiHelper
    _VEHICLE_MENU_HELPER = FrontlineHangarVehicleMenuHelper
