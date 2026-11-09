# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.battle_pass.battle_pass_helpers import getExtraVideoURL as getExtraVideoURL, getIntroVideoURL as getIntroVideoURL, getInfoPageURL as getInfoPageURL, isIntroEnabled as isIntroEnabled, isIntroVideoEnabled as isIntroVideoEnabled, isExtraIntroVideoEnabled as isExtraIntroVideoEnabled
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.battle_pass.common import isExtraChapterSeen as isExtraChapterSeen, isExtraVideoShown as isExtraVideoShown, isIntroShown as isIntroShown, isIntroVideoShown as isIntroVideoShown, setExtraChapterSeen as setExtraChapterSeen, setExtraVideoShown as setExtraVideoShown, setIntroVideoShown as setIntroVideoShown, showOverlayVideo as showOverlayVideo, showIntroView as showIntroView
from gui.lobby_state_machine.states import LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, SubScopeSubLayerState as SubScopeSubLayerState, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.shared.utils import isRomanNumberForbidden as isRomanNumberForbidden
from helpers import dependency as dependency, int2roman as int2roman
from shared_utils import nextTick as nextTick
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Union as Union
from frameworks_common.state_machine import State as State
_BP = R.aliases.battle_pass
STATES: dict
_INITIAL_STATE_ID: Any

# decorador original: @SubScopeSubLayerState.parentOf
class BattlePassState(ViewLobbyState):
    STATE_ID = 'battlePass'
    VIEW_KEY: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...

class _BattlePassPresenterState(LobbyState):
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def addNavigationTransition(self, targetViewState, transitionType=..., record=True):
        ...
    def getNavigationDescription(self):
        ...
    def _getNavigationDescriptionArgs(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getNavigationInfos(self):
        ...

# decorador original: @BattlePassState.parentOf
class ChapterChoiceBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'chapterChoice'
    VIEW_KEY: Any
    __battlePass: Any
    __gui: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def compareParams(self, params, otherParams):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def goTo(cls, **params):
        ...
    def _getNavigationDescriptionArgs(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getNavigationInfos(self):
        ...
    # decorador original: @nextTick
    def __showIntros(self):
        ...
    # decorador original: @nextTick
    def __onVideoShown(self):
        ...
    # decorador original: @nextTick
    def __onIntroShown(self):
        ...
    def __onExtraVideoShown(self):
        ...
    def __updateSelectedChapter(self):
        ...

# decorador original: @BattlePassState.parentOf
class ProgressionBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'progression'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

# decorador original: @BattlePassState.parentOf
class PostProgressionBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'postProgression'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

# decorador original: @BattlePassState.parentOf
class TankmenBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'tankmenScreen'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

# decorador original: @BattlePassState.parentOf
class BuyPassBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'buyPass'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

# decorador original: @BattlePassState.parentOf
class BuyPassRewardsBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'buyPassRewards'
    VIEW_KEY: Any

# decorador original: @BattlePassState.parentOf
class BuyLevelsBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'buyLevels'
    VIEW_KEY: Any

# decorador original: @BattlePassState.parentOf
class HolidayFinalBattlePassState(_BattlePassPresenterState):
    STATE_ID = 'holidayFinal'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    @classmethod
    def goTo(cls, **params):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _shouldNavigateToProgression(event, battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isHoliday(event, battlePass=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isHolidayComplete(event, battlePass=None):
    ...
