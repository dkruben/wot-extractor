# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/hangar_presets/fun_hangar_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random_common.fun_constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import FunRandomLobbyHeaderHelper as FunRandomLobbyHeaderHelper
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_vehicle_menu_helper import FunRandomHangarVehicleMenuHelper as FunRandomHangarVehicleMenuHelper
from gui.hangar_presets.providers.base_dynamic_gui_provider import BaseHangarDynamicGuiProvider as BaseHangarDynamicGuiProvider
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper as DefaultMissionsGuiHelper

class FunRandomHangarDynamicGuiProvider(BaseHangarDynamicGuiProvider, FunSubModesWatcher):
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = FunRandomLobbyHeaderHelper
    _MISSIONS_HELPER = DefaultMissionsGuiHelper
    _VEHICLE_MENU_HELPER = FunRandomHangarVehicleMenuHelper
    # decorador original: @hasDesiredSubMode(...)
    def getBattleModifiers(self):
        ...
