# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/obsolete/hangar_presets_getters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.hangar_presets.obsolete.hangar_gui_helpers import ifComponentInPreset as ifComponentInPreset
from gui.Scaleform.daapi.view.lobby.hangar.controls_helpers import DefaultHangarControlsHelper as DefaultHangarControlsHelper, RandomHangarControlsHelper as RandomHangarControlsHelper
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags_getters import DefaultQuestFlagsGetter as DefaultQuestFlagsGetter, RankedQuestFlagsGetter as RankedQuestFlagsGetter, MapboxQuestFlagsGetter as MapboxQuestFlagsGetter
from gui.Scaleform.genConsts.HANGAR_CONSTS import HANGAR_CONSTS as HANGAR_CONSTS
from helpers import dependency as dependency
from skeletons.gui.game_control import IMapboxController as IMapboxController, IRankedBattlesController as IRankedBattlesController
from gui.hangar_presets.obsolete.hangar_gui_config import HangarGuiPreset as HangarGuiPreset
from gui.periodic_battles.models import AlertData as AlertData
from gui.Scaleform.daapi.view.lobby.hangar.controls_helpers import IHangarControlsHelper as IHangarControlsHelper
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags_getters import IQuestFlagsGetter as IQuestFlagsGetter

class IPresetsGetter(object):
    def getAmmoInjectViewAlias(self):
        ...
    def getAmmoSetupViewAlias(self):
        ...
    def getCarouselSettings(self):
        ...
    def getHangarAlertBlock(self):
        ...
    def getHangarHeaderBlock(self):
        ...
    def getHangarWidgetAlias(self):
        ...
    def getHangarControlsHelper(self):
        ...
    def getPreset(self):
        ...

class EmptyPresetsGetter(IPresetsGetter):
    _DEFAULT_AMMO_INJECT_VIEW_ALIAS = None
    _DEFAULT_AMMO_SETUP_VIEW_ALIAS = None
    @classmethod
    def getDefaultAmmoInjectViewAlias(cls):
        ...
    @classmethod
    def getDefaultAmmoSetupViewAlias(cls):
        ...
    @classmethod
    def getDefaultCarouselSettings(cls):
        ...
    @classmethod
    def getDefaultHangarAlertBlock(cls):
        ...
    @classmethod
    def getDefaultHangarControlsHelper(cls):
        ...
    @classmethod
    def getDefaultHangarHeaderBlock(cls):
        ...
    @classmethod
    def getDefaultHangarWidgetAlias(cls):
        ...
    @classmethod
    def getDefaultPreset(cls):
        ...
    def getAmmoInjectViewAlias(self):
        ...
    def getAmmoSetupViewAlias(self):
        ...
    def getCarouselSettings(self):
        ...
    def getHangarAlertBlock(self):
        ...
    def getHangarControlsHelper(self):
        ...
    def getHangarHeaderBlock(self):
        ...
    def getHangarWidgetAlias(self):
        ...
    def getPreset(self):
        ...

class BasePresetsGetter(EmptyPresetsGetter):
    _QUEST_FLAGS_GETTER = None
    _HANGAR_CONTROLS_HELPER = None
    _preset: Any
    def __init__(self, preset):
        ...
    # decorador original: @ifComponentInPreset(...)
    def getAmmoInjectViewAlias(self, preset=None):
        ...
    # decorador original: @ifComponentInPreset(...)
    def getCarouselSettings(self, preset=None):
        ...
    # decorador original: @ifComponentInPreset(...)
    def getHangarHeaderBlock(self, preset=None):
        ...
    # decorador original: @ifComponentInPreset(...)
    def getHangarWidgetAlias(self, preset=None):
        ...
    def getHangarControlsHelper(self):
        ...
    def getPreset(self):
        ...
    def _getQuestFlagsGetter(self):
        ...

class DefaultPresetsGetter(BasePresetsGetter):
    _QUEST_FLAGS_GETTER = DefaultQuestFlagsGetter
    _HANGAR_CONTROLS_HELPER = DefaultHangarControlsHelper

class RandomPresetsGetter(DefaultPresetsGetter):
    _HANGAR_CONTROLS_HELPER = RandomHangarControlsHelper

class RankedPresetsGetter(DefaultPresetsGetter):
    _QUEST_FLAGS_GETTER = RankedQuestFlagsGetter
    __rankedController: Any
    def getHangarAlertBlock(self):
        ...

class MapboxPresetsGetter(DefaultPresetsGetter):
    _QUEST_FLAGS_GETTER = MapboxQuestFlagsGetter
    __mapboxController: Any
    def getHangarAlertBlock(self):
        ...

class SpecBattlePresetsGetter(DefaultPresetsGetter):
    GUI_TYPE_TO_QUEST_FLAGS: dict
    _flagsGetter: Any
    def __init__(self, preset, guiType):
        ...
    def _getQuestFlagsGetter(self):
        ...
