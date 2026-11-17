# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/login_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates
from gui.game_loading.state_machine.models import ImageViewSettingsModel as ImageViewSettingsModel
from gui.game_loading.state_machine.states.slide import StaticSlideState as StaticSlideState
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources

class LoginScreenState(StaticSlideState):
    __slots__: tuple
    _nextSlideDuration: Any
    def __init__(self, images, nextSlideDuration, viewSettings):
        ...
    @property
    def nextSlideDuration(self):
        ...
    def _onEntered(self, event):
        ...
