# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/calendar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import time as time
import typing as typing
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from math_common import decimal_round as decimal_round
from shared_utils import first as first, nextTick as nextTick
from wg_async import AsyncEvent as AsyncEvent, AsyncScope as AsyncScope, BrokenPromiseError as BrokenPromiseError, TimeoutError as TimeoutError, delay as delay, wg_async as wg_async, wg_await as wg_await
from skeletons.gui.server_events import IEventsCache as IEventsCache
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from skeletons.gui.game_control import IWalletController as IWalletController
from account_helpers.AccountSettings import AdventCalendar as AdventCalendar
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_TOKEN as ADVENT_CALENDAR_TOKEN
from advent_calendar.gui.impl.gen.view_models.views.lobby.components.advent_calendar_events import EventType as EventType
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState as DoorState, DoorViewModel as DoorViewModel, Mark as Mark
from advent_calendar.gui.impl.gen.view_models.views.lobby.main_view_model import MainViewModel as MainViewModel, StatePhase as StatePhase, TooltipConstants as TooltipConstants
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionState as ProgressionState
from advent_calendar.gui.impl.lobby.feature.advent_helper import getAccountTokensAmount as getAccountTokensAmount, getAdventCalendarSetting as getAdventCalendarSetting, getDoorState as getDoorState, getFirstClosedDayID as getFirstClosedDayID, getQuestNeededTokensCount as getQuestNeededTokensCount, isAdventAnimationEnabled as isAdventAnimationEnabled, pushOpenDoorFailedError as pushOpenDoorFailedError, setAdventCalendarSetting as setAdventCalendarSetting
from advent_calendar.gui.impl.lobby.feature.currency_provider import StandardCurrencyProvider as StandardCurrencyProvider
from advent_calendar.gui.impl.lobby.feature.progression_reward_packers import getProgressionBonusPacker as getProgressionBonusPacker
from advent_calendar.gui.impl.lobby.feature.sound_helper import ADVENT_CALENDAR_MAIN_WINDOW_SOUND as ADVENT_CALENDAR_MAIN_WINDOW_SOUND
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_all_rewards_tooltip import AdventCalendarAllRewardsTooltip as AdventCalendarAllRewardsTooltip
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip as AdventCalendarSimpleTooltip, createAdventCalendarSimpleTooltip as createAdventCalendarSimpleTooltip
from advent_calendar.gui.shared.event_dispatcher import showAdventCalendarIntroWindow as showAdventCalendarIntroWindow, showPurchaseDialogWindow as showPurchaseDialogWindow, showRewardWindow as showRewardWindow
from advent_calendar.gui.shared.events import AdventCalendarEvent as AdventCalendarEvent
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from advent_calendar_common.advent_calendar_constants import DoorMarkType as DoorMarkType
from gui.game_control.links import URLMacros as URLMacros
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from typing import Dict as Dict, List as List, Optional as Optional
from advent_calendar.gui.impl.lobby.feature.currency_provider import CurrencyProvider as CurrencyProvider
_logger: Any
CONFIG_TO_MODEL_MARK_MAP: dict
QUEST_COMPLETED_TIMEOUT = 20
_INVALID_IDX = -1
FADE_IN_ANIMATION_TIME = 2

# base nao representavel no stub: ViewComponent[...]
class CalendarView:
    __adventController: Any
    __eventsCache: Any
    _wallet: Any
    _COMMON_SOUND_SPACE = ADVENT_CALENDAR_MAIN_WINDOW_SOUND
    __UPDATE_DOOR_ANIMATION_DELTA_TIME = 2
    __OPEN_DOOR_ANIM_TIME = 3
    _currencyProvider: Any
    __tooltips: Any
    __progressionRewardInProgressIdx: Any
    __selectedDayId: Any
    __selectedCurrency: Any
    __lastHighlightDoorAnimTime: Any
    __lastOpenDoorTime: Any
    __waitSuccessfulOpenDoor: Any
    __worldDrawCallbackID: Any
    __scope: Any
    __doorOpenedQuestCompletedEvent: Any
    def __init__(self, currencyProvider):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @staticmethod
    def _getProgressionBonusPacker():
        ...
    def _onClose(self, *_, **__):
        ...
    @staticmethod
    def _getPostActivePhaseSubTitle():
        ...
    def __updateModel(self):
        ...
    def __fillDoors(self, model):
        ...
    def __createDoorModel(self, dayID, firstClosedDayID, isHighlightDoorAnimationAvailable):
        ...
    def __getPhaseState(self):
        ...
    def __createProgressionInfo(self, viewModel):
        ...
    def __createProgressionRewardModels(self, quest, prevState, prevRequiredTokensAmount):
        ...
    # decorador original: @args2params(...)
    def __onOpenDoorAnimStarted(self, dayId):
        ...
    # decorador original: @args2params(...)
    def __onOpenDoorAnimEnded(self, dayId):
        ...
    # decorador original: @args2params(...)
    def __onShowPurchaseDialogWindow(self, dayId):
        ...
    # decorador original: @wg_async
    def __showPurchaseDialogWindow(self, dayId, price):
        ...
    # decorador original: @wg_async
    def __showRewardScreen(self, dayId):
        ...
    def __showProgressionRewardWindow(self):
        ...
    def __openAdventDoor(self, dayId):
        ...
    def __changeBlurState(self, event):
        ...
    def __getProgressionRewardInProgressIdx(self, progressionRewards):
        ...
    # decorador original: @wg_async
    def __updateProgressionRewards(self, event):
        ...
    def __onDoorOpened(self):
        ...
    def __onProgressionAnimationCompleted(self):
        ...
    # decorador original: @nextTick
    def __releaseAdventWindowUpdates(self):
        ...
    def __blockAdventWindowUpdates(self):
        ...
    def __onSettingsChange(self):
        ...
    def __onDoorsStateChanged(self):
        ...
    def __onWalletChanged(self, _):
        ...
    def __onBalanceUpdated(self):
        ...
    def __onInfoClick(self):
        ...
    # decorador original: @adisp_process
    def __onOpenDownloadLink(self):
        ...
    def __openIntro(self, isFirstTime=False):
        ...
    def __onIntroCloseStarted(self, _):
        ...
    def __worldDrawCallback(self):
        ...

class CalendarWindow(LobbyWindow):
    def __init__(self, currencyProvider=None, parent=None):
        ...
