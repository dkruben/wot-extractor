# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from comp7_light.gui.Scaleform.genConsts.COMP7_LIGHT_HANGAR_ALIASES import COMP7_LIGHT_HANGAR_ALIASES as COMP7_LIGHT_HANGAR_ALIASES
from comp7_light.gui.impl.lobby.comp7_light_intro_screen import Comp7LightIntroScreen as Comp7LightIntroScreen
from comp7_light.gui.impl.lobby.comp7_light_no_vehicles_screen import Comp7LightNoVehiclesScreen as Comp7LightNoVehiclesScreen
from comp7_light.gui.impl.lobby.progression_main_view import ProgressionMainView as ProgressionMainView
from comp7_light.gui.shared.event_dispatcher import showComp7LightInfoPage as showComp7LightInfoPage
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype
from gui.impl.lobby.hangar.easy_tank_equip_state import generateEasyTankEquipStates as generateEasyTankEquipStates
from gui.impl.lobby.hangar.states import HangarState as HangarState, EasyTankEquipState as EasyTankEquipState
from gui.lobby_state_machine.states import LobbyState as LobbyState, LobbyStateFlags as LobbyStateFlags, SubScopeSubLayerState as SubScopeSubLayerState, SFViewLobbyState as SFViewLobbyState, GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyStateDescription as LobbyStateDescription
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IComp7LightController as IComp7LightController
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from comp7_light.gui.impl.lobby.hangar.comp7_light_hangar import Comp7LightHangar as Comp7LightHangar
_logger: Any
Comp7LightLoadoutState: Any
_: Any
Comp7LightShellsLoadoutState: Any
Comp7LightEquipmentLoadoutState: Any
Comp7LightEasyTankEquipState: Any

# decorador original: @SubScopeSubLayerState.parentOf
class Comp7LightModeState(LobbyState):
    STATE_ID = 'comp7Light'
    __comp7LightController: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _hijackTransitionCondition(self, _):
        ...

# decorador original: @Comp7LightModeState.parentOf
class Comp7LightHangarState(SFViewLobbyState):
    STATE_ID = 'hangar'
    VIEW_KEY: Any
    __appLoader: Any
    def __init__(self, flags=...):
        ...
    def registerStates(self):
        ...
    def __getView(self):
        ...

# decorador original: @Comp7LightHangarState.parentOf
class Comp7LightRootHangarState(LobbyState):
    STATE_ID = '{root}'
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @Comp7LightHangarState.parentOf
class Comp7LightAllVehiclesState(LobbyState):
    STATE_ID = 'allVehicles'
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7LightModeState.parentOf
class Comp7LightNoVehiclesState(GuiImplViewLobbyState):
    STATE_ID = 'noVehicles'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7LightModeState.parentOf
class Comp7LightIntroState(GuiImplViewLobbyState):
    STATE_ID = 'intro'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7LightModeState.parentOf
class Comp7LightProgressionState(GuiImplViewLobbyState):
    STATE_ID = 'progression'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7LightModeState.parentOf
class Comp7LightPrimeTimeState(SFViewLobbyState):
    STATE_ID = 'primeTime'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

class _Comp7LightLoadoutConfirmStatePrototype(_LoadoutConfirmStatePrototype):
    STATE_ID = 'comp7Light/loadoutConfirmLeave'

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
