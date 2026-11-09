# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random_common.fun_constants import FunSubModeImpl as FunSubModeImpl
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import generateBasicHangarStateClasses as generateBasicHangarStateClasses, generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutStatePrototype as _LoadoutStatePrototype, _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype, _ShellsLoadoutStatePrototype as _ShellsLoadoutStatePrototype, _EquipmentLoadoutStatePrototype as _EquipmentLoadoutStatePrototype, _InstructionsLoadoutStatePrototype as _InstructionsLoadoutStatePrototype, _ConsumablesLoadoutStatePrototype as _ConsumablesLoadoutStatePrototype
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SFViewLobbyState as SFViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES as FUNRANDOM_ALIASES
from helpers import dependency as dependency
from skeletons.gui.game_control import IFunRandomController as IFunRandomController
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.shared.events import NavigationEvent as NavigationEvent
FunRandomHangarState: Any
DefaultFunRandomHangarState: Any
_: Any
FunRandomLoadoutState: Any
FunRandomShellsLoadoutState: Any

class _HangarStateProto(SFViewLobbyState):
    STATE_ID = 'funRandomHangar'
    VIEW_KEY: Any
    __funRandomController: Any
    def registerTransitions(self):
        ...
    def __hijackTransitionCondition(self, _):
        ...

class _FunRandomLoadoutStateProto(_LoadoutStatePrototype, FunSubModesWatcher):
    __desiredSubImpl: Any
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __invalidateSubMode(self, *_):
        ...

class _FunRandomLoadoutConfirmStateProto(_LoadoutConfirmStatePrototype):
    STATE_ID = 'funRandomLoadoutConfirmLeave'

class _FunRandomShellsLoadoutStatePrototype(_ShellsLoadoutStatePrototype, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def isStateReachable(self, event):
        ...

class _FunRandomEquipmentLoadoutStatePrototype(_EquipmentLoadoutStatePrototype, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def isStateReachable(self, event):
        ...

class _FunRandomInstructionsLoadoutStatePrototype(_InstructionsLoadoutStatePrototype, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def isStateReachable(self, event):
        ...

class _FunRandomConsumablesLoadoutStatePrototype(_ConsumablesLoadoutStatePrototype, FunSubModesWatcher):
    # decorador original: @hasDesiredSubMode(...)
    def isStateReachable(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
