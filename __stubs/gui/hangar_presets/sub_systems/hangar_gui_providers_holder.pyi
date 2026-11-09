# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/sub_systems/hangar_gui_providers_holder.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from itertools import chain as chain
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.listener import IPrbListener as IPrbListener
from gui.hangar_presets.obsolete.hangar_gui_config import getHangarGuiConfig as getHangarGuiConfig
from gui.hangar_presets.providers.base_dynamic_gui_provider import EmptyHangarDynamicGuiProvider as EmptyHangarDynamicGuiProvider
from gui.shared.system_factory import collectHangarPresetsReaders as collectHangarPresetsReaders, collectHangarDynamicGuiProviders as collectHangarDynamicGuiProviders
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from gui.hangar_presets.providers.base_dynamic_gui_provider import IHangarDynamicGuiProvider as IHangarDynamicGuiProvider

class HangarGuiProvidersHolder(IHangarGuiController.IHangarGuiProvidersHolder, IPrbListener):
    _EMPTY_GUI_PROVIDER: Any
    __dynamicGuiProviders: Any
    __bonusGuiProviders: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getBonusGuiProvider(self, bonusType):
        ...
    def getCurrentGuiProvider(self, defaultQueueType=...):
        ...
