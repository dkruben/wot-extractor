# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/obsolete/hangar_gui_sf_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.hangar_presets.obsolete.hangar_gui_helpers import hasCurrentPreset as hasCurrentPreset
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from gui.hangar_presets.obsolete.hangar_gui_config import HangarGuiPreset as HangarGuiPreset
from gui.hangar_presets.obsolete.hangar_presets_getters import IPresetsGetter as IPresetsGetter
from gui.Scaleform.daapi.view.lobby.hangar.Hangar import Hangar as Hangar

class HangarGuiScaleformController(IHangarGuiController.IHangarGuiScaleformController):
    __providersHolder: Any
    __isChangeableComponentsVisible: Any
    __hangar: Any
    def __init__(self, providersHolder):
        ...
    def fini(self):
        ...
    @property
    def currentPresetGetter(self):
        ...
    # decorador original: @hasCurrentPreset(...)
    def isComponentAvailable(self, preset, componentType):
        ...
    def getCurrentPreset(self):
        ...
    def holdHangar(self, hangar):
        ...
    def releaseHangar(self):
        ...
    # decorador original: @hasCurrentPreset(...)
    def updateComponentsVisibility(self, preset=None):
        ...
    def updateChangeableComponents(self, isVisible, force=False):
        ...
    # decorador original: @hasCurrentPreset(...)
    def __getChangeableComponents(self, preset=None):
        ...
