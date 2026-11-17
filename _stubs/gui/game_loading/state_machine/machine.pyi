# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import wraps as wraps
import wg_async as wg_async
from frameworks_common.state_machine import StateMachine as StateMachine, StringEvent as StringEvent
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.cdn.images import CdnImagesResources as CdnImagesResources
from gui.game_loading.resources.consts import LoadingTypes as LoadingTypes
from gui.game_loading.resources.local.base import LocalResources as LocalResources
from gui.game_loading.state_machine.const import GameLoadingStatesEvents as GameLoadingStatesEvents, GameLoadingStates as GameLoadingStates, DEFAULT_WAITING_TIMEOUT as DEFAULT_WAITING_TIMEOUT
from gui.game_loading.state_machine.states.base import BaseTickingState as BaseTickingState, BaseGroupTickingStates as BaseGroupTickingStates
from gui.game_loading.state_machine.states.init_client import ClientInitState as ClientInitState
from gui.game_loading.state_machine.states.login_screen import LoginScreenState as LoginScreenState
from gui.game_loading.state_machine.states.player_loading import PlayerLoadingState as PlayerLoadingState
from gui.game_loading.state_machine.states.idle import IdleState as IdleState
from gui.game_loading.state_machine.states.transitions import LoginScreenTransition as LoginScreenTransition, LoginScreenTransitionWithLastShownImage as LoginScreenTransitionWithLastShownImage, PlayerLoadingTransition as PlayerLoadingTransition, ClientInitToPlayerLoadingTransition as ClientInitToPlayerLoadingTransition, LoginScreenToPlayerLoadingTransition as LoginScreenToPlayerLoadingTransition, IdleTransition as IdleTransition
from frameworks_common.state_machine import StateEvent as StateEvent
from gui.game_loading.settings import GameLoadingSettings as GameLoadingSettings
from gui.game_loading.preferences import GameLoadingPreferences as GameLoadingPreferences
_logger: Any

class GameLoadingStateMachine(StateMachine):
    __slots__: tuple
    _cdnImages: Any
    _logos: Any
    _isGameLoadingComplete: Any
    def __init__(self):
        ...
    @property
    def isGameLoadingComplete(self):
        ...
    # decorador original: @_ifNotRunning(...)
    def setGameLoadingComplete(self):
        ...
    def stop(self):
        ...
    # decorador original: @_ifNotRunning(...)
    def post(self, event):
        ...
    def configure(self, preferences, settings):
        ...
    # decorador original: @_ifNotRunning(...)
    def onConnected(self):
        ...
    # decorador original: @_ifNotRunning(...)
    def onDisconnected(self):
        ...
    # decorador original: @_ifNotRunning(...)
    def tick(self, stepNumber):
        ...
    # decorador original: @_ifNotRunning(...)
    def loginScreen(self):
        ...
    # decorador original: @_ifNotRunning(...)
    def playerLoading(self, retainMilestones=False):
        ...
    # decorador original: @_ifNotRunning(...)
    def idle(self):
        ...
    @property
    def isLoading(self):
        ...
    # decorador original: @wg_async.wg_async
    def wait(self, timeout=...):
        ...

def _ifNotRunning(result=None):
    ...
