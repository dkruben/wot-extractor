# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/loading.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import inspect as inspect
import typing as typing
import WWISE as WWISE
import game_loading_bindings as game_loading_bindings
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.game_loading import loggers as loggers
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
from gui.game_loading.settings import GameLoadingSettings as GameLoadingSettings
from gui.game_loading.state_machine.machine import GameLoadingStateMachine as GameLoadingStateMachine
from ResMgr import DataSection as DataSection
_logger: Any
_g_Loader: Any

def startSound():
    ...
def getLoader():
    ...
def tick(stepNumber):
    ...
def initialize(preferences, settings):
    ...
def step():
    ...
