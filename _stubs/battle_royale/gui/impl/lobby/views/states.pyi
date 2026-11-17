# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from battle_royale.gui.shared.event_dispatcher import showInfoPage as showInfoPage
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.BATTLEROYALE_ALIASES import BATTLEROYALE_ALIASES as BATTLEROYALE_ALIASES
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags, SFViewLobbyState as SFViewLobbyState, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.shared.utils.functions import getViewName as getViewName
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from typing import Optional as Optional

# decorador original: @SubScopeSubLayerState.parentOf
class BattleRoyaleModeState(LobbyState):
    STATE_ID = 'battleRoyale'
    battleRoyaleController: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def _isBattleRoyaleMode(cls, event):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyaleHangarState(ViewLobbyState):
    STATE_ID = 'battleRoyaleHangar'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyaleTournamentQueueState(ViewLobbyState):
    STATE_ID = 'battleRoyaleTournamentBattleQueue'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyaleProgressionState(ViewLobbyState):
    battleRoyaleController: Any
    STATE_ID = 'battleRoyaleProgression'
    VIEW_KEY: Any
    NAVIGATION_BUTTONS: tuple
    def _onExited(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyaleBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = BATTLEROYALE_ALIASES.BR_BATTLE_RESULTS
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getViewKey(self, params=None):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyalePrimeTimeState(SFViewLobbyState):
    STATE_ID = 'battleRoyalePrimeTime'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

# decorador original: @BattleRoyaleModeState.parentOf
class BattleRoyaleVehicleInfoState(SFViewLobbyState):
    STATE_ID = 'battleRoyaleVehicleInfo'
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

def registerStates(lsm):
    ...
def registerTransitions(lsm):
    ...
