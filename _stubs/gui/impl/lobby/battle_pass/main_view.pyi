# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from typing import TYPE_CHECKING as TYPE_CHECKING
import Event as Event
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, StateEvent as StateEvent, visitor as visitor
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.battle_pass.battle_pass_helpers import getChapterForTankmenScreen as getChapterForTankmenScreen
from gui.battle_pass.sounds import BATTLE_PASS_TASKS_SOUND_SPACE as BATTLE_PASS_TASKS_SOUND_SPACE, switchBattlePassSoundFilter as switchBattlePassSoundFilter, getBattlePassEnterSound as getBattlePassEnterSound, getBattlePassExitSound as getBattlePassExitSound, getBattlePassExtraExitSound as getBattlePassExtraExitSound, getBattlePassExtraEnterSound as getBattlePassExtraEnterSound, switchOverlaySoundFilter as switchOverlaySoundFilter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.main_view_model import MainViewModel as MainViewModel
from gui.impl.lobby.battle_pass.battle_pass_buy_levels_view import BuyLevelsPresenter as BuyLevelsPresenter
from gui.impl.lobby.battle_pass.battle_pass_buy_view import BuyPassPresenter as BuyPassPresenter
from gui.impl.lobby.battle_pass.battle_pass_progressions_view import ProgressionPresenter as ProgressionPresenter
from gui.impl.lobby.battle_pass.chapter_choice_view import ChapterChoicePresenter as ChapterChoicePresenter
from gui.impl.lobby.battle_pass.holiday_final_view import HolidayFinalPresenter as HolidayFinalPresenter
from gui.impl.lobby.battle_pass.post_progression_view import PostProgressionPresenter as PostProgressionPresenter
from gui.impl.lobby.battle_pass.tankmen_voiceover_view import TankmenVoiceoverPresenter as TankmenVoiceoverPresenter
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from shared_utils import safeCall as safeCall
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from typing import Optional as Optional
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.states import LobbyState as LobbyState
_logger: Any
_BP = R.aliases.battle_pass
_PRESENTERS: dict
_PARENTS: dict
_UNTRACKED: Any
_NO_CHAPTER_PRESENTERS: Any

class _BattlePassStatesObserver(BaseStateObserver):
    onSubViewSelect: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...

# base nao representavel no stub: ViewComponent[...]
class MainView(IRoutableView):
    __battlePass: Any
    __lsm: Any
    __router: Any
    __statesObserver: Any
    __activePresenterID: Any
    __activeChapterID: Any
    __selectedChapter: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def selectedChapter(self):
        ...
    def updateSelectedChapter(self, chapterID):
        ...
    def getRouterModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onSettingsChanged(self, *_):
        ...
    def __onExtraChapterExpired(self):
        ...
    def __switchSubView(self, presenterID, **kwargs):
        ...
    def __safeCallOnActivePresenter(self, methodName, *args, **kwargs):
        ...
    def __playEnterSounds(self):
        ...
    def __playSwitchSounds(self, originalPresenterID, previousChapter):
        ...
    def __playExitSounds(self):
        ...
    def __isExtraChapterPresenter(self):
        ...

class BattlePassWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
