# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/logos_loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StringEvent as StringEvent, StateFlags as StateFlags
from gui.game_loading import loggers as loggers
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates, GameLoadingStatesEvents as GameLoadingStatesEvents, TickingMode as TickingMode
from gui.game_loading.state_machine.states.base import BaseViewResourcesTickingState as BaseViewResourcesTickingState
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import getFullClientVersion as getFullClientVersion
from gui.game_loading.resources.models import LogoModel as LogoModel, LocalImageModel as LocalImageModel
from gui.game_loading.resources.local.base import LocalResources as LocalResources
_logger: Any

class LogosLoadingState(BaseViewResourcesTickingState):
    __slots__: tuple
    _ageRatingPath: Any
    def __init__(self, logos, ageRatingPath):
        ...
    @property
    def lastShownImage(self):
        ...
    def _view(self, resource):
        ...
