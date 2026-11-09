# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/providers/spec_battle_dynamic_gui_providers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.obsolete.hangar_presets_getters import SpecBattlePresetsGetter as SpecBattlePresetsGetter
from gui.hangar_presets.providers.base_dynamic_gui_provider import EmptyHangarDynamicGuiProvider as EmptyHangarDynamicGuiProvider
from gui.hangar_presets.providers.default_dynamic_gui_provider import BaseHangarDynamicGuiProvider as BaseHangarDynamicGuiProvider
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.vehicle_menu_helper import DefaultHangarVehicleMenuHelper as DefaultHangarVehicleMenuHelper
from gui.impl.lobby.missions.missions_helpers import DefaultMissionsGuiHelper as DefaultMissionsGuiHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.prb_control.entities.base.legacy.entity import BaseLegacyEntity as BaseLegacyEntity
SpecBattleGuiSettings: Any
DEFAULT_SPEC_GUI_SETTINGS: Any

class SpecBattleHangarDynamicGuiProvider(BaseHangarDynamicGuiProvider):
    GUI_TYPE_TO_SPEC_SETTINGS: dict
    _presetGetter: Any
    _guiSettings: Any
    def __init__(self, config, guiType=...):
        ...
    def createAllBonusTypes(self):
        ...
    def createByPrbEntity(self, prbEntity):
        ...
    def getBattleModifiers(self):
        ...
    def getLobbyHeaderHelper(self):
        ...
    def getMissionsHelper(self):
        ...
    def getVehicleMenuHelper(self):
        ...
    def getPresetsGetter(self):
        ...
    def getSuggestedBonusType(self):
        ...
