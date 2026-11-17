# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/playlists_states.pyc (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from copy import deepcopy as deepcopy
from enum import Enum as Enum
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.dialogs.vehicle_playlists import showSaveBeforeLeavePlaylistDialog as showSaveBeforeLeavePlaylistDialog
from gui.impl.lobby.hangar.random.sound_manager import PLAY_LISTS_SOUND_SPACE as PLAY_LISTS_SOUND_SPACE
from gui.impl.lobby.hangar.states import HangarState as HangarState, AllVehiclesState as AllVehiclesState
from gui.lobby_state_machine.states import LobbyState as LobbyState, SubScopeSubLayerState as SubScopeSubLayerState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.view_helpers.blur_manager import ImmediateSceneBlurConfig as ImmediateSceneBlurConfig
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.game_control import IVehiclePlaylistsController as IVehiclePlaylistsController, IBlurController as IBlurController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from wg_async import wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, AsyncEvent as AsyncEvent
from gui.shared.events import NavigationEvent as NavigationEvent
from gui.Scaleform.daapi.view.lobby.battle_queue.states import CommonBattleQueueState as CommonBattleQueueState
absolute_import: Any
_logger: Any
EditVehiclePlaylistsState: Any

# gerado do bytecode: classes base desconhecidas
class PlaylistState:
    NEW: Any
    EXISTING: Any

def registerStates(machine):
    ...
def generateVehiclePlayListClasses(parentStateCls=..., parentAllVehicleStateCls=..., parentLobbyState=...):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
