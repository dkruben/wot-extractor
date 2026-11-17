# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from advent_calendar.gui.impl.gen.view_models.views.lobby.reward_view_model import AwardDayState as AwardDayState, OpenDoorStatus as OpenDoorStatus, RewardViewModel as RewardViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import isAdventAnimationEnabled as isAdventAnimationEnabled, openAndWaitDoor as openAndWaitDoor
from advent_calendar.gui.impl.lobby.feature.bonus_grouper import RewardBonusGrouper as RewardBonusGrouper, RewardsBonusGroups as RewardsBonusGroups
from advent_calendar.gui.impl.lobby.feature.bonus_packers import getRewardBonusPacker as getRewardBonusPacker
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip as AdventCalendarSimpleTooltip
from advent_calendar.gui.shared import events as events
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.server_events.bonuses import BattleTokensBonus as BattleTokensBonus, LootBoxTokensBonus as LootBoxTokensBonus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from helpers import dependency as dependency
from typing import Any as Any, Dict as Dict, List as List, Tuple as Tuple
from gui.impl.backport import TooltipData as TooltipData
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
_logger: _Any
_EXCLUDED_CLASSES: tuple
_BONUSES_ORDER: tuple

class RewardView(ViewImpl):
    _adventController: _Any
    _tooltips: _Any
    _isProgressionReward: _Any
    _currency: _Any
    def __init__(self, *args, **kwargs):
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
    def _isLootBoxInBonuses(self, bonuses):
        ...
    def _onLoading(self, dayId, isProgressionReward, bonuses, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @staticmethod
    def _getSortedBonuses(bonuses):
        ...
    @staticmethod
    def _getRewardBonusPacker():
        ...
    def _getEvents(self):
        ...
    def _onClose(self, *args, **kwargs):
        ...
    def _onOpenBoxes(self):
        ...
    def _onSetBlur(self, event):
        ...
    def _onRequestOpenDoor(self, event):
        ...
    def _requestOpenDoor(self, doorId):
        ...
    def _processServerDoorOpen(self, dayId, result):
        ...

class RewardWindow(LobbyWindow):
    def __init__(self, dayId, isProgressionReward, data, currency='', parent=None):
        ...

def sortBonuses(groupedBonuses, excluded=..., excludedCls=..., bonusesOrder=...):
    ...
