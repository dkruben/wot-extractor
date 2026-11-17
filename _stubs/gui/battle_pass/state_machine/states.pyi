# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_pass/state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from future.utils import viewitems as viewitems
from battle_pass_common import BattlePassRewardReason as BattlePassRewardReason, get3DStyleProgressToken as get3DStyleProgressToken
from frameworks_common.state_machine import ConditionTransition as ConditionTransition, State as State, StateEvent as StateEvent, StateFlags as StateFlags
from gui.battle_pass.battle_pass_helpers import asBPVideoName as asBPVideoName, getStyleForChapter as getStyleForChapter, getStyleInfoForChapter as getStyleInfoForChapter, makeChapterMediaName as makeChapterMediaName, makeProgressionStyleMediaName as makeProgressionStyleMediaName, showBPFullscreenVideo as showBPFullscreenVideo
from gui.battle_pass.state_machine import lockNotificationManager as lockNotificationManager
from gui.battle_pass.state_machine.state_machine_helpers import isProgressionComplete as isProgressionComplete, packToken as packToken, processRewardsToChoose as processRewardsToChoose
from gui.impl.gen import R as R
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showBattlePass as showBattlePass, showBattlePassAwardsWindow as showBattlePassAwardsWindow, showBattlePassRewardsSelectionWindow as showBattlePassRewardsSelectionWindow
from gui.shared.events import LobbySimpleEvent as LobbySimpleEvent
from helpers import dependency as dependency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from gui.battle_pass.state_machine.machine import BattlePassStateMachine as BattlePassStateMachine
from typing import Dict as Dict, List as List, Optional as Optional

class BattlePassRewardStateID(CONST_CONTAINER):
    LOBBY = 'lobby'
    LOBBY_START = 'lobby.start'
    LOBBY_WAIT = 'lobby.wait'
    LOBBY_FINAL = 'lobby.final'
    VIDEO = 'video'
    CHOICE = 'choice'
    CHOICE_ITEM = 'choice.item'
    CHOICE_STYLE = 'choice.style'
    CHOICE_PREVIEW = 'choice.preview'
    REWARD = 'reward'
    REWARD_STYLE = 'reward.style'
    REWARD_ANY = 'reward.any'

class StateMachineEventID(object):
    OPEN_PREVIEW = 'choice.event.open_preview'
    CLOSE_PREVIEW = 'choice.event.close_preview'

class LobbyState(State):
    __slots__: tuple
    __notificationManager: Any
    __battlePass: Any
    def __init__(self):
        ...
    @property
    def lobbyStart(self):
        ...
    @property
    def lobbyWait(self):
        ...
    @property
    def lobbyFinal(self):
        ...
    def configure(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

class ChoiceState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def choiceItem(self):
        ...
    def configure(self):
        ...

class ChoiceItemState(State):
    __slots__: tuple
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...

class PreviewState(State):
    __slots__: tuple
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onHidePreview(self, _):
        ...

class VideoState(State):
    __battlePass: Any
    __slots__: tuple
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...

class RewardState(State):
    __slots__: tuple
    def __init__(self):
        ...
    @property
    def rewardStyle(self):
        ...
    @property
    def rewardAny(self):
        ...
    def configure(self):
        ...

class RewardStyleState(State):
    __slots__: tuple
    __battlePass: Any
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...

class RewardAnyState(State):
    __slots__: tuple
    __guiLoader: Any
    __battlePass: Any
    __needShowBuy: Any
    def __init__(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onAwardClose(self, chapterID, newLevel, reason):
        ...
    def __onAwardExit(self, chapterID, newLevel):
        ...
    def __onShowBuy(self, chapterID):
        ...
