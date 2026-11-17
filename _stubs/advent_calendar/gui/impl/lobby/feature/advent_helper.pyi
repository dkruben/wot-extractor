# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/advent_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
import logging as logging
from itertools import chain as chain
from typing import Optional as Optional
import BigWorld as BigWorld
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import AdventCalendar as AdventCalendar
from advent_calendar.gui.feature.constants import ADVENT_PRESETS_WITH_DISABLED_ANIMATION as ADVENT_PRESETS_WITH_DISABLED_ANIMATION
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState as DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import RewardType as RewardType
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from advent_calendar_common.advent_calendar_constants import DoorMarkType as DoorMarkType
from constants import SECONDS_IN_DAY as SECONDS_IN_DAY
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.bonuses import TmanTemplateTokensBonus as TmanTemplateTokensBonus, LootBoxTokensBonus as LootBoxTokensBonus, CustomizationsBonus as CustomizationsBonus
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
_logger: Any

def getQuestNeededTokensCount(quest):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAccountTokensAmount(token, itemsCache=None):
    ...
# decorador original: @wg_async
# decorador original: @dependency.replace_none_kwargs(...)
def openAndWaitDoor(dayID, currency='', callback=None, controller=None):
    ...
def pushOpenDoorFailedError():
    ...
def getProgressionRewardType(bonus):
    ...
def getFlattenedBonuses(quests):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDoorState(dayID, firstClosedDayID=None, adventController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getFirstClosedDayID(adventController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getHolidayOpsStartTime(adventController=None):
    ...
def isAdventAnimationEnabled():
    ...
def getAdventCalendarSetting(settingName):
    ...
def setAdventCalendarSetting(settingName, settingValue):
    ...
