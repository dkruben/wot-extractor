# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES as COMP7_HANGAR_ALIASES
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.impl.lobby.comp7_intro_screen import Comp7IntroScreen as Comp7IntroScreen
from comp7.gui.impl.lobby.comp7_no_vehicles_screen import Comp7NoVehiclesScreen as Comp7NoVehiclesScreen
from comp7.gui.impl.lobby.hangar.meta_tab_state import IMetaTabState as IMetaTabState
from comp7.gui.impl.lobby.meta_view.meta_root_view import MetaRootView as MetaRootView
from comp7.gui.impl.lobby.tournaments.wci_view import WciView as WciView
from comp7.gui.impl.lobby.tournaments.ols_view import OlsView as OlsView
from comp7.gui.shared.event_dispatcher import showComp7InfoPage as showComp7InfoPage, showComp7WhatsNewScreen as showComp7WhatsNewScreen, showWciInfoPage as showWciInfoPage, showOlsInfoPage as showOlsInfoPage
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState as ShopState
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype
from gui.impl.lobby.hangar.easy_tank_equip_state import generateEasyTankEquipStates as generateEasyTankEquipStates
from gui.impl.lobby.hangar.states import HangarState as HangarState, EasyTankEquipState as EasyTankEquipState
from gui.lobby_state_machine.states import LobbyState as LobbyState, LobbyStateFlags as LobbyStateFlags, GuiImplViewLobbyState as GuiImplViewLobbyState
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from comp7.gui.impl.lobby.hangar.comp7_hangar import Comp7Hangar as Comp7Hangar
_logger: Any
metaStateNavigationButtons: tuple
Comp7LoadoutState: Any
_: Any
Comp7ShellsLoadoutState: Any
Comp7EquipmentLoadoutState: Any
Comp7EasyTankEquipState: Any

# decorador original: @SubScopeSubLayerState.parentOf
class Comp7ModeState(LobbyState):
    STATE_ID = 'comp7'
    __comp7Controller: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _hijackTransitionCondition(self, _):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7HangarState(SFViewLobbyState):
    STATE_ID = 'hangar'
    VIEW_KEY: Any
    __appLoader: Any
    def __init__(self, flags=...):
        ...
    def registerStates(self):
        ...
    def __getView(self):
        ...

# decorador original: @Comp7HangarState.parentOf
class Comp7RootHangarState(LobbyState):
    STATE_ID = '{root}'
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @Comp7HangarState.parentOf
class Comp7AllVehiclesState(LobbyState):
    STATE_ID = 'allVehicles'
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7NoVehiclesState(GuiImplViewLobbyState):
    STATE_ID = 'noVehicles'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7IntroState(GuiImplViewLobbyState):
    STATE_ID = 'intro'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class Comp7WCIState(GuiImplViewLobbyState):
    STATE_ID = 'wci'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7OLSState(GuiImplViewLobbyState):
    STATE_ID = 'ols'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7PrimeTimeState(SFViewLobbyState):
    STATE_ID = 'primeTime'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7MetaState(GuiImplViewLobbyState):
    STATE_ID = 'meta'
    VIEW_KEY: Any
    __comp7Controller: Any
    def __init__(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _hijackQualificationCondition(self, _):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onQualificationUpdated(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaProgressionState(LobbyState, IMetaTabState):
    STATE_ID = 'progression'
    def registerTransitions(self):
        ...
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaQualificationState(LobbyState, IMetaTabState):
    STATE_ID = 'qualification'
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaRankRewardsState(LobbyState, IMetaTabState):
    STATE_ID = 'rankRewards'
    __guiLoader: Any
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def __getView(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaYearlyRewardsState(LobbyState, IMetaTabState):
    STATE_ID = 'yearlyRewards'
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def compareParams(self, params, otherParams):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaWeeklyQuestsState(LobbyState, IMetaTabState):
    STATE_ID = 'weeklyQuests'
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaShopState(LobbyState, IMetaTabState):
    STATE_ID = 'shop'
    __guiLoader: Any
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def __getView(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaLeaderboardState(LobbyState, IMetaTabState):
    STATE_ID = 'leaderboard'
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7MetaState.parentOf
class Comp7MetaYearlyStatisticsState(LobbyState, IMetaTabState):
    STATE_ID = 'yearlyStatistics'
    @property
    def tabId(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7StylePreviewState(SFViewLobbyState):
    STATE_ID = 'preview/style'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @Comp7ModeState.parentOf
class Comp7VehiclePreviewState(SFViewLobbyState):
    STATE_ID = 'preview/vehicle'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

class _Comp7LoadoutConfirmStatePrototype(_LoadoutConfirmStatePrototype):
    STATE_ID = 'comp7/loadoutConfirmLeave'

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
