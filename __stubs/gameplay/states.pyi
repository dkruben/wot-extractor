# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import enum as enum
import typing as typing
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import persistent_data_cache as pdc
import wg_async as wg_async
from gameplay.blockers import BlockableTransition as BlockableTransition, BlockingState as BlockingState
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from frameworks_common.state_machine import State as State, StateFlags as StateFlags, StringEvent as StringEvent
from frameworks_common.state_machine import StringEventTransition as StringEventTransition
from gui.game_loading import loading as gameLoading
from gui.game_loading.resources.consts import Milestones as Milestones
from shared_utils import safeCancelCallback as safeCancelCallback
from skeletons.gameplay import GameplayStateID as GameplayStateID, OfflineEventID as OfflineEventID
from skeletons.gameplay import PlayerEventID as PlayerEventID
from skeletons.gameplay import ReplayEventID as ReplayEventID
from gameplay.machine import GameplayStateMachine as GameplayStateMachine
_logger: Any

# decorador original: @enum.unique
class SyncingProgress(enum.IntEnum):
    NOT_STARTED = 0
    SYNCING = 1
    COMPLETE = 2
    CANCELED = 3

class WaitingMainLoopState(State):
    __slots__: tuple
    _callbackId: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _initWaiting(self):
        ...
    def _cancelWaiting(self):
        ...
    def _onCompleteEvent(self):
        ...

class SynchronizationState(State):
    __slots__: tuple
    _PDC_SAVING_TIMEOUT: Any
    _GAME_LOADING_TIMEOUT: Any
    _syncProgress: Any
    _savePDC: Any
    def __init__(self, savePDC=True):
        ...
    def clear(self):
        ...
    @staticmethod
    def _fireSavingPDCEvent():
        ...
    # decorador original: @wg_async.wg_async
    def _onEntered(self, event):
        ...
    # decorador original: @wg_async.wg_async
    def _sync(self):
        ...
    def _onExited(self):
        ...
    def _onCompleteEvent(self):
        ...

class OfflineState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def waitingMainLoop(self):
        ...
    @property
    def synchronization(self):
        ...
    @property
    def login(self):
        ...
    def configure(self):
        ...

class OnlineState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def account(self):
        ...
    @property
    def avatar(self):
        ...
    def configure(self, offline):
        ...

class AccountState(State):
    __slots__: tuple
    def __init__(self, flags=...):
        ...
    @property
    def entering(self):
        ...
    @property
    def showGUI(self):
        ...
    @property
    def exiting(self):
        ...
    def configure(self):
        ...

class AvatarState(State):
    __slots__: tuple
    def __init__(self, flags=...):
        ...
    @property
    def entering(self):
        ...
    @property
    def arenaInfo(self):
        ...
    @property
    def showGUI(self):
        ...
    @property
    def arenaLoaded(self):
        ...
    @property
    def exiting(self):
        ...
    def configure(self):
        ...

class InBattleState(BlockingState):
    __slots__: tuple
    @property
    def prebattleHighlihgts(self):
        ...
    @property
    def prebattle(self):
        ...
    @property
    def battle(self):
        ...
    def configure(self):
        ...

class BattleReplayLoadingState(State):
    __slots__: tuple
    def __init__(self):
        ...
    def enter(self, event):
        ...

class BattleReplayInitState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def loading(self):
        ...
    @property
    def differs(self):
        ...
    @property
    def starting(self):
        ...
    @property
    def nextReplay(self):
        ...
    @property
    def waitingMainLoop(self):
        ...
    @property
    def synchronization(self):
        ...
    def configure(self):
        ...

class BattleReplayPlayingState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def avatar(self):
        ...
    @property
    def finish(self):
        ...
    @property
    def rewind(self):
        ...
    def configure(self, initialization):
        ...
