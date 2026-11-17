# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/hangar_gui_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.prb_control.entities.listener import IPrbListener as IPrbListener
from gui.hangar_presets.obsolete.hangar_gui_sf_controller import HangarGuiScaleformController as HangarGuiScaleformController
from gui.hangar_presets.sub_systems.hangar_gui_dynamic_economics import HangarGuiDynamicEconomics as HangarGuiDynamicEconomics
from gui.hangar_presets.sub_systems.hangar_gui_providers_holder import HangarGuiProvidersHolder as HangarGuiProvidersHolder
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from gui.hangar_presets.providers.base_dynamic_gui_provider import IHangarDynamicGuiProvider as IHangarDynamicGuiProvider

class HangarGuiController(IHangarGuiController, IPrbListener):
    __providersHolder: Any
    __dynamicEconomics: Any
    __sfController: Any
    def __init__(self):
        ...
    @property
    def currentGuiProvider(self):
        ...
    @property
    def dynamicEconomics(self):
        ...
    @property
    def sfController(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __getSubSystems(self):
        ...
